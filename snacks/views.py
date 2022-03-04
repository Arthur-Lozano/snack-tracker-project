from re import template
from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy

from snacks.models import Snack

# Create your views here.
class SnackListView(ListView):
    template_name = "snack-list.html"
    model = Snack


class SnackDetailView(DetailView):
    template_name = "snack-detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "snack-create.html"
    model = Snack
    fields = ["title", "description", "purchaser"]


class SnackUpdateView(UpdateView):
    template_name = "snack-update.html"
    model = Snack
    fields = ["title", "description", "purchaser"]


class SnackDeleteView(DeleteView):
    template_name = "snack-delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")
