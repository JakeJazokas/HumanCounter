from django.shortcuts import render

# Create your views here.
def web_interface(request):
    return render(request, 'web_interface.html', {})
