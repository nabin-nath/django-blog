from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('article/', include('article.urls')),
    path('', views.home)
]
