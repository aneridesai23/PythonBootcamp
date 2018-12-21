# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from nasa.models import NasaComments

# Create your views here	

class NasaCreateView(CreateView):
	model = NasaComments
	fields = ['comment', 'rating', 'image_url', 'date']
	success_url = reverse_lazy('nasa_list')

class NasaCommentListView(ListView):
	model = NasaComments

class NasaDetailView(DetailView):
	model = NasaComments
	pk_url_kwarg = "id"

class NasaUpdateView(UpdateView):
	model = NasaComments
	fields = ['comment', 'rating', 'image_url', 'date']
	success_url = reverse_lazy('nasa_list')
	pk_url_kwarg = "id"

class NasaDeleteView(DeleteView):
	model = NasaComments
	success_url = reverse_lazy('nasa_list')
	pk_url_kwarg = "id"