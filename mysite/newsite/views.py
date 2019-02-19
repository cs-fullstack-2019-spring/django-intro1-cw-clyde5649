from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a bad request you will be redirect.")

def music(request):
    return HttpResponse("usher,mrwale, mrMeek.")

def usher(request):
    return HttpResponse("r&b King.")

def mrMeek(request):
    return HttpResponse("got the flow.")

def mrwale(request):
    return HttpResponse("the best alive")