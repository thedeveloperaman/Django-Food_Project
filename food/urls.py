from django.urls import path
from . import views
app_name = 'food'
urlpatterns = [
   path('',views.home, name = 'home'),
   path('additem/',views.additem, name='additem'),
   path('<int:id>/',views.details, name='details'),
   path('logout/',views.logout, name='logout'),
]