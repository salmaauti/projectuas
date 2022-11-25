from django.shortcuts import render

# Create your views here.
def index (request):
    konteks = {}
    return render(request, 'market/index.html', konteks)

