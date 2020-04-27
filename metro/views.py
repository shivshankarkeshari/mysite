from django.shortcuts import render

# Create your views here.


def ok(request):
    return render(request, 'stock/home_page.html')
