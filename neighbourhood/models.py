from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=30)
    neighbourhood_location = models.CharField(max_length=30)
    occupation_count = models.CharField(max_length=30)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.neighbourhood_name

    
    def create_neighbourhood(self):
        return self.save()

    def delete_neighbourhood(self):
        return self.delete()

    @classmethod
    def find_neighbourhood(neighbourhood_id):
        find_neighbourhood = Neighbourhood.objects.filter(neighbourhood_id = id)
        return find_neighbourhood
    @classmethod
    def update_neighbourhood(cls, id, neighbourhood_name):
        update_neighbourhood = Neighbourhood.objects.filter(id=id).update(neighbourhood_name = neighbourhood_name)
        return update_neighbourhood

    @classmethod
    def update_occupants(cls, id, occupation_count):
        update_occupants = Neighbourhood.objects.filter(id=id).update(occupation_count = occupation_count)
        return update_occupants()




class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    neighbourhood = models.ForeignKey(Neighbourhood)
    email_address = models.EmailField()

    def __str__(self):
        return self.name

class Business(models.Model):
    business_name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    business_email_address = models.EmailField()

    def __str__(self):
        return self.business_name

    def create_business(self):
        return self.save()
    
    def delete_business(self):
        return self.delete()

    @classmethod
    def find_business(business_id):
        find_business = Business.objects.filter(business_id = business_id)
        return find_business
    @classmethod
    def update_business(cls, id, business_name):
        update_business = Business.objects.filter(id=id).update(business_name =business_name)
        return update_business
    # @classmethod
    # def search_business(cls,search_term):
    #     business = cls.objects.filter(neighbourhood_neighbourhood_name__icontains=search_term)
    #     return business

class Contacts(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    email_address = models.EmailField()
    neighbourhood = models.ForeignKey(Neighbourhood)

    def __str__(self):
        return self.name

class Posts(models.Model):
    user = models.ForeignKey(UserProfile) 
    post = models.TextField(max_length=250)

    def __str__(self):
        return self.post    