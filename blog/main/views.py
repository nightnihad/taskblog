from django.shortcuts import render
from .models import Article
# Create your views here.

def main_page(request):
    return render(request,template_name='main.html')

def index(request,id):
    article = Article.objects.filter(id=id)
    return render(request,'article.html',{'article':article,id:id})

def create_article(request):
    #category = 
    return render()