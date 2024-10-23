from django.shortcuts import render

# Create your views here.
def livestream(request):
    return render(request,"livestream.html")
