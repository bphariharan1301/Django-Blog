from .forms import SignUpForm, EditProfileForm, PasswordChangingForm 
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

# Create your views here.

# User Registration 
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name =  'registration/register.html'
    success_url = reverse_lazy('login')

# Update User Profile
class UserUpdateView(generic.UpdateView):
    form_class = EditProfileForm
    template_name =  'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsUpdateView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change-password.html'
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})
    
