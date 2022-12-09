from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)

