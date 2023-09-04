from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    info = models.TextField(blank=True)
    price = models.IntegerField()
    color = models.ForeignKey("Color", on_delete=models.PROTECT)
    storage = models.IntegerField()
    categories = models.ManyToManyField("Category", blank=True, related_name="products")
    image = models.ImageField(upload_to="images/", default="images/default.png")


    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail_url", kwargs={'pk': self.pk})

    class Meta:
        ordering = ['price']


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"



class Color(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    

class Order(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name