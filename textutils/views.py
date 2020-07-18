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
    value = request.POST.get("string")
    string = "Original String capitalized : " + value.capitalize()
    string += "<br> Number of characters in this string are : " + str(len(value))
    string += "<br> Number of vowels in this string are : " + str(
        value.count('a') + value.count('e') + value.count('i') + value.count('o') + value.count('u'))
    result = {'result': string, }
    return render(request, 'textutils_result.html', result)
