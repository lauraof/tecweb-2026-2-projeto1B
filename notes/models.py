from django.db import models

class Tag(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nome}'

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id}. {self.title}'