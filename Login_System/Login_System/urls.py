"""
URL configuration for Login_System project.

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
from django.urls import path, include
from Loginify import views

urlpatterns = [
    path('', views.hello_world, name='home'),  # ADD THIS LINE
    path('admin/', admin.site.urls),
    path('app/', views.hello_world, name='hello'),
    path('app/signup/', views.signup, name='signup'),
    path('app/login/', views.login, name='login'),
    path('app/all-users/', views.get_all_users, name='all_users'),
    path('app/user/<str:email>/', views.get_user_by_email, name='user_detail'),
    path('app/update/<str:username>/', views.update_user, name='update_user'),
    path('app/delete/<str:email>/', views.delete_user, name='delete_user'),
]
