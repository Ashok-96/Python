from django.urls import path
from . import views
urlpatterns=[
    path("",views.index),
    path("<str:month>/",views.display, name='challenges'),
    path("<int:num>/",views.displays)
]