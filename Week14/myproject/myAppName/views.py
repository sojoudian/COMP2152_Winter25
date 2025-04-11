from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello, world! This is your first Django view.")