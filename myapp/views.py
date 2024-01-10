from django.shortcuts import render, redirect
from myapp.models import Quote
from django.http import HttpResponse
from django.contrib import messages
from myapp.models import Logo
from myapp.models import Cust_logo
from myapp.models import Why
from myapp.models import Happy_cust
from myapp.models import Prod_serv
from myapp.models import Round_neck
from myapp.models import Polo
from myapp.models import Jersey
from myapp.models import Hoodie
from myapp.models import Cap
# Create your views here.

    # pull data from database
    # Transform
    # Send emails

def index(request):
    logos = Logo.objects.all()
    return render(request, 'index1.html',{"logos":logos})

def index(request):
    cust_logo = Cust_logo.objects.all()
    return render(request, 'index1.html', {"cust_logo": cust_logo})

def index(request):
    why = Why.objects.all()
    return render(request, 'index1.html', {"why": why})

def index(request):
    happy_cust = Happy_cust.objects.all()
    return render(request, 'index1.html', {"happy_cust": happy_cust})

def index(request):
    prod_serv = Prod_serv.objects.all()
    return render(request, 'index1.html', {"prod_serv": prod_serv})
    
def product(request):
    return render(request, 'product.html')

def about(request):
    return render(request, 'about1.html')

def blog(request):
    return render(request, 'blog.html')

def round_neck(request):
    return render(request, 'RoundNeckTshirt.html')

def round_neck(request):
    round_neck = Round_neck.objects.all()
    return render(request, 'RoundNeckTshirt.html', {"round_neck": round_neck})

def polo(request):
    return render(request, 'polo.html')

def polo(request):
    polo = Polo.objects.all()
    return render(request, 'polo.html', {"polo": polo})

def jersey(request):
    return render(request, 'jersey.html')

def jersey(request):
    jersey = Jersey.objects.all()
    return render(request, 'jersey.html', {"jersey": jersey})

def hoodie(request):
    return render(request, 'hoodie.html')

def hoodie(request):
    hoodie = Hoodie.objects.all()
    return render(request, 'hoodie.html', {"hoodie": hoodie})

def cap(request):
    return render(request, 'cap.html')

def cap(request):
    cap = Cap.objects.all()
    return render(request, 'cap.html', {"cap": cap})

def screen(request):
    return render(request, 'screen.html')

def sublimation(request):
    return render(request, 'sublimation.html')

def embroidery(request):
    return render(request, 'Embroidery.html')

def dtf(request):
    return render(request, 'dtf.html')



# Get a free Quote form

def quoteform(request):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        contact_number=request.POST.get('contact_number')
        email=request.POST.get('email')
        product_type=request.POST.get('product_type')
        
        qf=Quote(name=name, address=address, contact_number=contact_number, email=email, product_type=product_type)
        
        qf.save()
        messages.success(request, 'We will contact you asap')
    return render(request, 'index1.html')

def quotedata(request):
    return render(request, 'quotedata.html')

def quotedata(request):
    quote = Quote.objects.all()
    return render(request, 'quotedata.html', {"quote": quote})
