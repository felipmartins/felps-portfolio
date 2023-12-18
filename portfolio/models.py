from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(
        upload_to="portfolio/static/img/skill",
    )

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=100)
    start_end_date = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_end_date = models.CharField(max_length=100)

    def __str__(self):
        return self.role


class Recommendation(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
