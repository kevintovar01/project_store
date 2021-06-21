from django.db import models

# Create your models here.

class CategoryProduct(models.Model):
    name = models.CharField(max_length=120)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='category_product'
        verbose_name_plural='categorys_ptoducts'

    def __str__(self):
        return self.name


class ProductModels(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(upload_to='store', blank=True, null=True)
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)


    create = models.DateField( auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return self.name