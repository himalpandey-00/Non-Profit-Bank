from django.shortcuts import render
from django.views import generic
from v1.user.models import User

class LeaderboardListView(generic.ListView):
    template_name = 'leaderboard/list.html'
    paginate_by = 5

    def get_queryset(self):
        return User.objects.filter(reputation__gte=101).order_by('-reputation')