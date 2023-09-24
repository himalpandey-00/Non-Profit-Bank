from django.db import models
from v1.user.models import User
from v1.bank.models import Bank

# Item Model
class Item(models.Model):
    name = models.CharField(max_length= 255)
    point = models.IntegerField()
    unit = models.CharField(max_length=127)

    def __str__(self):
        return self.name + ', Point: ' + str(self.point)

# Donation Model.
class Donation(models.Model):
    donated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    display_name = models.CharField(max_length=255)
    bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    no_of_item = models.IntegerField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_by')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.display_name + ": " + self.item.name + " "+ str(self.no_of_item) + "x"

    def total_reputation_earned(self):
        return self.item.point * self.no_of_item

class UserBank(models.Model):
    PermChoices = [
        (0, 'View'),
        (1, 'Create'),
        (2, 'Update'),
        (3, 'Delete')
    ]
    bank = models.ForeignKey(Bank, on_delete=models.DO_NOTHING, related_name='bank')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user')
    perm = models.IntegerField(choices=PermChoices, default=0)

    def __str__(self):
        return self.bank.name + ", " + self.user.email + ": " + str(self.perm)

    class Meta:
        unique_together = ['user', 'bank']
    