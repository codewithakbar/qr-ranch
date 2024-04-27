from django.db import models
from django.utils.text import slugify


class Maktablar(models.Model):

    name = models.CharField(max_length=233, verbose_name="Maktab nomi")
    direktor_name = models.CharField(max_length=233, verbose_name="Direktor nomi")
    slug = models.SlugField(unique=True, max_length=255, verbose_name="Slug")
    full_link = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Maktablar, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    
