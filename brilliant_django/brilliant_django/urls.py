"""
URL configuration for brilliant_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# import views 
from ecart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', views.demo),
    path('', views.demo2, name='homepage'),
    path('squared/', views.squared_num),
    path('uppercased/', views.uppercased),
    path('demo3/', views.demo3),
    path('demo_form/', views.demo_form),
    path('register/', views.user_registration, name='register'),
    path('login/', views.login_fun, name='login'),
    path('setcookie/', views.setcookie),
    path('page_vists/', views.cookie_vists),
    path('cookie_homepage/', views.cookie_homepage, name='cookie_homepage'),
    path('cookie_login/', views.cookie_login, name='cookie_login'),
    path('cookie_logout/', views.cookie_logout, name='cookie_logout'),
    path('cookie_register/', views.cookie_register, name='cookie_register'),
    path('cookie_auth_homepage/', views.cookie_auth_homepage, name='cookie_auth_homepage'),
    path('setsession/', views.setsession, name='setsession'),
]
