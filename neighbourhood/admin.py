from django.contrib import admin
from .models import Posts,Business,Contacts,UserProfile,Neighbourhood
# Register your models here.]

admin.site.register(Posts)
admin.site.register(UserProfile)
admin.site.register(Contacts)
admin.site.register(Business)
admin.site.register(Neighbourhood)

