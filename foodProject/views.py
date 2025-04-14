from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello from Django.:.")

def info(request):
    return HttpResponse("About Page...!")