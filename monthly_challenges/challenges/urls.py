from django.urls import path
# the dot says import files from the same folder
from . import views

# this creates a URLconf
urlpatterns = [
    path("",views.index, name="index"), 
    path("<int:month>",views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"), # we can use the name using reverse()
    
]
