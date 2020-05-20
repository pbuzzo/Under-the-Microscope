from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from microapp.forms import CustomUserCreationForm


def index(request):
    return render(request, 'index.html')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
