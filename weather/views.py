from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import weather_searches
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from django.template.response import TemplateResponse



baseurl = "https://www.timeanddate.com/weather/?query="
basemain = "https://www.timeanddate.com/"


# Create your views here.
@csrf_exempt
def weather_city(request):
    search = request.POST.get('city')
    if search:
        weather_searches.objects.create(text=search)
        soup = requests.get(baseurl + search).text
        soup = BeautifulSoup(soup, 'lxml')
        links = soup.find("td")
        link = links.find('a')
        soup = requests.get(basemain + link['href']).text
        fulldata = BeautifulSoup(soup, 'lxml')
        data = fulldata.find("section", {"class": "bk-wt"})
        if data:
            return HttpResponse(data)

    return render(request, 'weather/index.html', )
