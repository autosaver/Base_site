from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.
@csrf_exempt
def home(request):
    return render(request, 'mycarthome.html', )

def search(request):
    return render(request, 'mycarthome.html', )
