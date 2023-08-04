from django.shortcuts import render

# Create your views here.

def imageinsert(request):
    return render(request, 'image_insert.html')