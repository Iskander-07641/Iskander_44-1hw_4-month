from django.db import models


class ParserRezka(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    rating = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.title
