from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app1/index.html')

def home(request):
    return render(request, 'app1/home.html')