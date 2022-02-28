from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.forms import ModelForm
from django import forms
from platformdirs import user_cache_dir

# Create your models here.

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_posts")
    email = models.CharField(max_length=30)
    hour = models.DateTimeField(default=timezone.now)
    avatar = models.CharField(max_length=200, default=None, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form_item', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form_item', 'placeholder': 'Last name'}),
            'avatar': forms.TextInput(attrs={'class': 'form_item', 'placeholder': 'Add your avatar'})
        }