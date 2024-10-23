from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse,NoReverseMatch

# Create your models here.
class categ(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return'{}'.format(self.name)

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])
    
class product(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    img = models.ImageField(upload_to='products')
    desc = models.TextField()
    stock = models.IntegerField(default=0)
    available = models.BooleanField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(categ,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])
    

    def __str__(self):
        return '{}'.format(self.name)
    
