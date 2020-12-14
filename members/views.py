from myblog.models import Category, Profile
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm #, SignInForm 
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'portfolio_url', 'fb_url', 'insta_url', 'twitter_url', 'linkedin_url', 'pinterest_url']
    
    success_url = reverse_lazy('home')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

# User Registration 
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name =  'registration/register.html'
    success_url = reverse_lazy('login')



# Update User Profile
class UserUpdateView(generic.UpdateView):
    form_class = EditProfileForm
    template_name =  'registration/edit_profile.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UserUpdateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] =  cat_menu
        return context

    def get_object(self):
        return self.request.user

    success_url = reverse_lazy('home')
    
class PasswordsUpdateView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change-password.html'
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})
    
