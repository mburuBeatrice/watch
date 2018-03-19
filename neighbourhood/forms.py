from django import forms
from .models import Neighbourhood,Business,Posts,UserProfile

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['neighbourhood_name','neighbourhood_location'] 

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neighbourhood']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['post', 'user']
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name','neighbourhood','email_address']