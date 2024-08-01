from django.db import models
from django.contrib.auth.models import User
from mytraveladmin.models import Packages
# Create your models here.
    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=255, null=True, blank=True)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    date = models.CharField(max_length=200,null=True, blank=True)
    Month = models.CharField(max_length=200,null=True,blank=True)
    cvv = models.CharField(max_length=4, null=True, blank=True)
    bank = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.package.name} - {self.card_name}"
    
class Confirm_booking(models.Model):
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    email = models.EmailField()
    datetime = models.DateTimeField()
    person = models.IntegerField()
    child = models.IntegerField()
    message = models.CharField(max_length=250)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking by {self.user.username}"