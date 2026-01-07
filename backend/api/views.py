from django.shortcuts import HttpResponse

# Create your views here.
def demo(_request):
    return HttpResponse("API is working!")