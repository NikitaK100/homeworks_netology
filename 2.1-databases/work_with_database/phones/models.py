from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(max_length=11)
    image = models.CharField(max_length=255)
    release_date = models.CharField(max_length=20)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)


    def __str__(self,):
        return str(self.name)