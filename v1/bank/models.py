from django.db import models

class BankType(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Bank(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    bank_type = models.ForeignKey(BankType, on_delete=models.DO_NOTHING)
    description = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class FeaturedBank(models.Model):
    bank = models.OneToOneField(Bank, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.bank.name

    