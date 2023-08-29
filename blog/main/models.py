from django.db import models
from django.contrib.auth.models import User


# Kateqoriyalar modeli

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def  __str__(self):
        return self.name
    
#Cateqoriyaya aid olan meqalaleleri elde etmek ucun funksiya

    def get_article(self):
        return Article.objects.filter(category=self)
    
#Meqaleler modeli


class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subject = models.TextField(max_length=100000)
    category  = models.ManyToManyField(Category)
    likes = models.BigIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, editable=False,null=True, blank=True) 
    updated = models.DateTimeField(default=None, editable=True,null=True, blank=True)
    
    def __str__(self):
        return self.title
    
# Kommentler modeli

class Comments(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.TextField(max_length=10000)
    time = models.DateTimeField(auto_now_add=True,editable=False,null=True,blank=True)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    likes = models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.article.title + 'meqalesine aid comment'

class About(models.Model):
    subject = models.TextField(max_length=10000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Haqqimizda'
    
class Contactus(models.Model):
    subject = models.TextField(max_length=100)
    number = models.IntegerField()   
    address = models.CharField(max_length=100)

    def __str__(self):
        return 'Bizimle'
    
    
