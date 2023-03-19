from django.urls import path
from . import views
urlpatterns=[
    path("",views.index),
    path("<int:month>",views.months_num),
    path("<str:month>",views.display),
]