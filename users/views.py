from django.http import HttpResponse
from rest_framework.decorators import action

from users.serializers import UsersSerializer

@action(methods=['POST'], detail=False)
def login(request):
    return HttpResponse("login")


@action(methods=['POST'], detail=False)
def join(request):
    serializer = UsersSerializer(request.body)
    serializer.is_valid()
    serializer.save()
    return HttpResponse("join")
