from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^home/$',views.home,name = 'home'),
    url(r'^contacts/$', views.find_contact, name= 'contact'),
    url(r'^post/$', views.new_post, name='new_post'),
    url(r'^profile_form/$', views.new_profile, name='new_profile'),
    url(r'^hoods/$', views.neighbourhood, name ='neighbourhood'),
    url(r'^new_neighbourhood/(?P<id>\d+)/$', views.new_neighbourhood, name='new_neighbourhood'),
    url(r'^hood_deets/(?P<id>\d+)/$', views.neighbourhood_details, name='hood_deets'),
    url(r'^profile/(?P<id>\d+)/$', views.profile, name = 'profile'),
    url(r'^neighbourhood/(?P<id>\d+)/$',views.find_neighbourhood, name ='neighbourhood')
   
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)