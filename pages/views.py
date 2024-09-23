from django.http import HttpResponse

# Create your views here.

def homeView (request):
    message = 'hello world!'

    return HttpResponse(message)

def aboutView(request):
    message = 'This is about section about our project'    

    return HttpResponse(message)


def contactView(request):
    message = 'This is contact'    

    return HttpResponse(message)



def cartView(request):
    message = 'This is cart'    

    return HttpResponse(message)


