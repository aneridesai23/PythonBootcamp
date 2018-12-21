"""generic_nasa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from nasa.views import NasaCommentListView, NasaCreateView, NasaUpdateView, NasaDetailView, NasaDeleteView

urlpatterns = [
    path('admin', admin.site.urls),
    path('nasa_create', NasaCreateView.as_view(), name='nasa_create'),
    path('nasa_list', NasaCommentListView.as_view(), name='nasa_list'),
    path('nasa_update/<int:id>/', NasaUpdateView.as_view(), name='nasa_update'),
    path('nasa_detail/<int:id>/', NasaDetailView.as_view(), name='nasa_detail'),
    path('nasa_delete/<int:id>/', NasaDeleteView.as_view(), name='nasa_delete'),
]