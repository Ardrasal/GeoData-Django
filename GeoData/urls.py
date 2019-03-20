from django.contrib import admin
from django.urls import path, include
from heatmap import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('api/', include('api.urls')),
]
