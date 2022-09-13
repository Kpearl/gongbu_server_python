from django.http import HttpResponse


def login(request):
    return HttpResponse("login")

def join(request):
    return HttpResponse("join")