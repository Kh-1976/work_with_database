from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(default='')
    price = models.IntegerField(default=0)
    image = models.ImageField(default=None)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True)

    def __str__(self):
        return self.name

