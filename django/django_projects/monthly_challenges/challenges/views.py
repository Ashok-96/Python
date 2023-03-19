from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound,Http404
from django.urls import reverse
# Create your views here.
months={
    "January":'One month without alcohol and soda.',
    "February":'One month of being total Vegan.',
    "March":'One month of sugar detox.',
    "April":'One month of running 1 mile each day.',
    "May":'One month of yoga every day.',
    "June":'One month of social media detox.',  
    "July":'One month of caffeine detox.',
    "August":'One month of eating only at home or home-cooked meal.',
    "September":'One month of no Netflix and TV',
    "October":'One month of daily reading for at least 30 minutes',
    "November":'One month of daily mindfulness meditation for at least 20 minutes',
    "December":'One month of doing a random act of kindness'
    
}
monthk=list(months.keys())

def months_num(req,month):
    id=monthk[month-1]
    try:
        return HttpResponseRedirect(f"./{id}")
    except IndexError as msg:
       raise Http404()
        
    
def display(req,month):
   try: 
        return render(req,'challenges.html',{
        'month':month,
        'challenge':months[month]
    })
   except:
       raise Http404()


        

def index(req):
    return render(req,'index.html',{
        "months":monthk
    })

