from django.db import models
from uuid import uuid4


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    uuid = models.UUIDField(
        default=uuid4,
        editable=False,
        unique=True,
        primary_key=True,
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (
            f"{self.title} - {self.user} - Pendente ⏱️"
            if not self.is_completed
            else f"{self.title} - {self.user} - Concluída ✅"
        )
