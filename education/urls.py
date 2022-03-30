from django.contrib import admin
from django.urls import path

app_name = 'education'
from education import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.learn, name='index'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses')
]
