from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect

# process function source leetcode


# Create your views here.
@csrf_exempt
def text_input(request):
    return render(request, 'textutils.html')


@csrf_exempt
def text_process(request):
    search = request.POST.get('task')
    if search:
        return render(request, 'calculator_result.html', {'result': calculates(search), })
    return render(request, 'calculator_index.html', )
