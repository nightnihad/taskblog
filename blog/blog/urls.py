"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main_page,name='homepage'),
    path('detail_article/<int:id>',views.to_comment,name = 'detail_article'),
    path('article/<int:id>',views.index,name = 'article'),
    path('to_like/<int:id>',views.to_like,name = 'to_like'),
    path('delete_comment/<int:id>',views.delete_comment,name ='delete_comment'),
    path('delete_article/<int:id>',views.delete_article,name ='delete_article'),
    path('get_category/<int:id>',views.get_category,name='get_category'),
    path('categories/',views.categories,name='categories'),
    path('create_article/',views.create_article,name = 'create_article'),
    path('register/',views.register,name = 'register'),
    path('logout/',views.logout_user,name = 'logout'),
    path('about/',views.about,name = 'about'),
    path('contact',views.contact_us,name = 'contact'),
    path('login/',views.login,name = 'login')
]
