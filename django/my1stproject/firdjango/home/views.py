from django.shortcuts import render
from django.http import *
# Create your views here.
def index(req,para):
    if para=='January':
        return HttpResponse("<h1>hey!</h1>")
    else:
        return HttpResponseNotFound("<h2>!Sorry path not found</h2>")
def default(req):
    return HttpResponse('right developer!')
    