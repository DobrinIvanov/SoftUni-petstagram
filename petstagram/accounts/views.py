from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from petstagram.accounts.forms import PetstagramUserCreateForm
from petstagram.accounts.models import PetstagramUser


# Create your views here.


def login_user(request):
    return render(request, 'accounts/login-page.html')


class UserRegisterView(views.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')
    # REGISTER VIEW
# def register_user(request):
#     return render(request, 'accounts/register-page.html')


def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


def details_user(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')
