from django.shortcuts import render

# Create your views here.
def dodge(request):
    return render(request,'dodge.html')