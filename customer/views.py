from django.shortcuts import render

# Create your views here.

def wishlist(request):
    return render(request, 'wishlist.html')

def basket(request):
    return render(request, "basket.html")