from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='project/', null=True)
    repo_url = models.URLField()
    skills = models.ManyToManyField(Skill, related_name='projects', blank=True)

    def __str__(self):
        return self.title
