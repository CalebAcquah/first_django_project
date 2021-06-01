from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

# Create your views here.

def mydict(request):
    data = [
        "Name" "Caleb Acquah",
        "Track" "Backend(Python)",
        "Message" "Hi, mentor, you're doing a great job"  
]
    return JsonResponse(data)

