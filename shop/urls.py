from django.urls import path
from .views import home, person_detail

urlpatterns = [
    path('person/', home, name='home'),  
    path('person/<int:id>/', person_detail, name='person_detail'),
]
