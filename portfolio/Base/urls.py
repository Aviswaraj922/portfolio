from django.urls import path 
from . import views



    # path('my-linkedin/', views.linkedin_profile, name='linkedin_profile'),



urlpatterns=[
    path('',views.contact),
    path('contact/',views.contact,name="savecontact"),
        path('my-linkedin/', views.linkedin_profile, name='linkedin_profile'),

]
