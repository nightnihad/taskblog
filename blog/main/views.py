from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from pytz import timezone
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.forms import UserCreationForm
from main.forms import ArticleForm, CommentsForm, LoginForm
from .models import Article, Category, Comments,About,Contactus
# Create your views here.

# Bizimle elaqe sehifesi ucun sadece admin panelden deyisile bilen content
def contact_us(request):
    contact = Contactus.objects.first()
    return render(request,'contact.html',{'contact':contact})

# Haqqimizda sehifesi ucun sadece admin panelden deyisile bilen content
def about(request):
    aboutdata = About.objects.first()
    return render(request,'about.html',{'aboutdata':aboutdata})
def categories(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'category.html',context)

# cateqoriyalar uygun meqaleler yukleyen funksiya, sadece olaraq articles valuable olaraq bos cixir deye funksiyada kronik bir xeta var
def get_category(request,id):
    # category = Category.objects.filter(id=id)
    print(id)
    category = Category.objects.filter(id=id)
    print(category)
    articles = Article.objects.filter(category__in = [id])
    print(articles)
    context = {'articles' : articles}
    return render(request,'category_detail.html',context)

# meqalelere comment etmek ucun funksiya. commenti sadece istifadeciler yaza biler ve comment etdikden sonra article sehifesine yonlendirir
def to_comment(request,id):
    if request.user.is_authenticated:
        article = get_object_or_404(Article,id=id)
        if request.method == 'POST':
            author = get_object_or_404(User,username=request.user)
            comment_subject = request.POST.get('subject')
            comment_article = article
            comment_author = author
            comment = Comments(author = comment_author,subject = comment_subject,article = comment_article)
            comment.save()
            return redirect('article',id)
        return HttpResponse('sss')
    return HttpResponse('Qeydiyyatdan kecmelisiz')
            


# article index sehifesidir. burda articlelari silmek, comment etmek ucun form ve like etmek mumkundur
def index(request,id):
    article = get_object_or_404(Article,id=id)
    form = CommentsForm()
    comments = article.comments.all()
    context = {
        'form':form,
        'article':article,id:id,
        'comments':comments
    }
    return render(request,'article.html',context)


# artikl yazmaq ucun view
def create_article(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ArticleForm(data = request.POST or None)
            if form.is_valid():
                article = Article()
                article.author = request.user
                category = form.cleaned_data['category']
                categories = Category.objects.filter(name__in = category)
                for categories_name in categories:
                    article.category.add(categories_name)
                article.title  = form.cleaned_data['title']
                article.subject = form.cleaned_data ['subject']
                article.likes = 0
                tz= timezone('Asia/Baku')
                article.created = datetime.now(tz)
                article.save()
                return redirect('/')
            else:
                return HttpResponse('doldurdugunuz melumatlar dogru deyil')
        else:
            form = ArticleForm()
            return render(request,'create.html',{'ArticleForm':form})
    else:
        return  HttpResponse('Siz qeydiyyatdan kecmemisiz')
    
# artikllari like etmek ucun view. burda istenilen istifadeci olmayan sexsler bele like ede bilir
def to_like(request,id):
        article = Article.objects.filter(id = id).first()
        if article is None:
            return HttpResponse('bosluq xetasi')
        article.likes +=1
        article.save()
        return redirect('article',id)
    
# artikllari silmek ucun view
def delete_article(request,id):
    article = get_object_or_404(Article,id=id)
    if request.user == article.author:
        article.delete()
        return redirect('/')
    else:
        return HttpResponse('siz bunu bilmersiz')

# commentleri silmek ucun view
def delete_comment(request,id):
    comment = get_object_or_404(Comments,id = id)
    if request.user == comment.author:
        comment.delete()
        return redirect('/')
    else:
        return HttpResponse('siz bu commenti sile bilmersiz')

# esas sehifeye artikklari yerlesdirmek ucun view
def main_page(request):
    article = Article.objects.all()
    return render(request,"main.html",{"article":article})

# register sehifesi ucun view
def register(request):
    form = UserCreationForm()
    if request.user.is_authenticated:
        return HttpResponse('sizin hesabiniz var')
    else:
        if request.method == 'POST':
            form =UserCreationForm(data= request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            return HttpResponse('duzgun qeydiyyatdan kecmemisiz')
    return render(request,'register.html',{'form':form})

# login sehifesi ucun view
@csrf_protect
def login(request):
    form = LoginForm()
    if request.user.is_authenticated:
        return HttpResponse('siz giris etmisiz')
    else:
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user_data = authenticate(username=username,password=password)
                if user_data is None:
                    return HttpResponse('hesabiniz yoxdur')
                else:
                    auth_login(request,user_data)
                    return redirect('/')
            else:
                return HttpResponse('is valid deyil')

        return render(request,"login.html",{'form':form})

# logout sehifesi ucun views
@login_required(login_url="/")
def logout_user(request):
    logout(request)
    return redirect('/')
        
        