from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Donation, UserBank, Bank
from .forms import DonationCreateForm
from django.views import generic
from django.urls import reverse_lazy, reverse
from v1.user.models import User
from django.db.models import Q

# Logic to Create Donation validating the UserPermission.
class CreateDonation(LoginRequiredMixin, UserPassesTestMixin,SuccessMessageMixin, CreateView):
    model = Donation
    form_class = DonationCreateForm
    success_message = 'Donation Added Successfully. Say thanks to donor three times.'
    
    def form_valid(self, form):
        donation = form.save(commit=False)
        bank = get_object_or_404(Bank, id=self.kwargs['pk'])
        donation.added_by = self.request.user
        if form.cleaned_data['donated_by'] != "":
            donor = User.objects.get(email=form.cleaned_data['donated_by'])
            donor.reputation += donation.total_reputation_earned()
            donor.save()
            donation.donated_by = donor
        donation.bank = bank
        donation.save()
        return super().form_valid(form)
    
    def test_func(self):
        user_bank = UserBank.objects.filter(Q(user=self.request.user), Q(bank=Bank.objects.get(id=self.kwargs['pk'])), Q(perm=1) | Q(perm=2) | Q(perm=3))
        if user_bank.exists():
            return True
        return False
    
    def get_success_url(self):
        return reverse('bank-detail', kwargs={'pk': self.kwargs['pk']})

class ListDonation(generic.ListView):
    paginate_by = 10

    def get_queryset(self):
        return Donation.objects.all().order_by('-created_at')