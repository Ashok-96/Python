from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
months={
    "January":'',
    "February":'',
    "March":'',
    "April":'',
    "May":'',
    "June":'',  
    "July":'',
    "August":'',
    "September":'',
    "October":'',
    "November":'',
    "December":''
    
}
def index(req):
   return render(req, 'index.html')
   """" month=''
    for i in months.keys():
        month+=f'<li><a href="./{i}/">{i}</a></li>'
    list_of_months=f'''<ol>{month}</ol>
    '''
    return HttpResponse(f'{list_of_months}')"""
def display(req,month):
    return HttpResponse(f'<h2>{month}</h2>')