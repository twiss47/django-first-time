from django.urls import path
from shop.views import home, check_age, region

urlpatterns = [
    path('home/', home, name='home'),
    path('check_age/<int:age>/', check_age, name='check_age'),
    path('region/<str:region>/', region, name='region'),

]
