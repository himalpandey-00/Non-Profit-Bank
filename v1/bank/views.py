from django.shortcuts import render
from django.views import generic
from .models import Bank, FeaturedBank
from v1.donation.models import UserBank, Donation
from django.db.models import Q

class Home(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        bank = Bank.objects.filter(is_active=True)
        featured_bank = FeaturedBank.objects.filter(is_active=True).select_related('bank')[:4]
        donations = Donation.objects.all().order_by('-created_at')[:4]
        query_set = {
            'bank' : bank,
            'featured_bank' : featured_bank,
            'donations': donations
        }
        return query_set

class BankList(generic.ListView):
    template_name = "bank/bank_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Bank.objects.filter(is_active=True)
    
class BankDetail(generic.DetailView):
    model = Bank

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if UserBank.objects.filter(
                Q(user=self.request.user), 
                Q(bank=context['bank']), 
                Q(perm=1) | Q(perm=2) | Q(perm=3)).exists():
                context['perm'] = True
        else:
            context['perm'] = False
        representatives = UserBank.objects.filter(Q(bank=context['bank'])).select_related('user')
        donations = Donation.objects.filter(bank=context['bank']).order_by('-created_at')
        context['donations'] = donations
        context['representatives'] = representatives
        return context