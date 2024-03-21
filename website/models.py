from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    def __str__(self):
        return (f"{self.user.username}'s Profile")


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return (f"{self.amount} - {self.category if self.category else 'No Category'} - {self.date} ")


class Income(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return (f"{self.amount} - {self.date} ")
