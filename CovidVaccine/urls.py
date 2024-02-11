from django.contrib import admin
from django.urls import path, include
from myapp import views
admin.autodiscover()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
]
