from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'myresponsivedesignapp/rdhome.html', context)

def productsresponsive(request):
    context = {}
    return render(request, 'myresponsivedesignapp/rdproduct.html', context)

def peopleresponsive(request):
    context = {}
    return render(request, 'myresponsivedesignapp/rdpeople.html', context)

def contactus(request):
    context = {}
    return render(request, 'myresponsivedesignapp/rdcontactus.html', context)