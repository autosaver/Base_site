from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import BaseList
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.
@csrf_exempt
def baseview(request):
    search = request.POST.get('task')
    if search:
        BaseList.objects.create(added_date=timezone.now(), text=search)
    Todo_list = BaseList.objects.all().order_by("-added_date")
    return render(request, 'base.html', {"Todo_list": Todo_list, })

@csrf_exempt
def deltask(request, todo_id):
    BaseList.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/todo")
