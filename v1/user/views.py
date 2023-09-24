from django.shortcuts import render, reverse
from .forms import  UserForm, UserUpdateForm
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.views.generic import View, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import User
from v1.donation.models import Donation

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration/register.html'

    def get(self,request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(email= email, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
        return render(request,self.template_name, {'form':form})

class UserDetail(DetailView):
    model = User
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        donations = Donation.objects.filter(donated_by=context['user']).select_related('bank').order_by('-created_at')
        total_donations = donations.count()
        context['donations'] = donations
        context['total_donations'] = total_donations
        return context


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/user_update.html'

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False
    
    def get_success_url(self):
        slug = self.get_object().username
        return reverse('user-profile', kwargs={'slug': slug})
