from django.urls import path
from api.views import *

urlpatterns = [
    path('add/', BookCreate.as_view()),
    path('all/', BookList.as_view()),
    path('update/<int:pk>', Bookupdate.as_view()),
    path('delete/<int:pk>', BookDelete.as_view()),
    
]