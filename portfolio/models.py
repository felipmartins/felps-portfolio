from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(
        upload_to="portfolio/static/img/skill",
    )

    class Meta:
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=100)
    start_end_date = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    class Meta:
        verbose_name = "Educação"
        verbose_name_plural = "Educações"

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_end_date = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Experiência"
        verbose_name_plural = "Experiências"

    def __str__(self):
        return self.role


class Recommendation(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Recomendação"
        verbose_name_plural = "Recomendações"

    def __str__(self):
        return self.name
