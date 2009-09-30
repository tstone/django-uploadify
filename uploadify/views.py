from django.http import HttpResponse
import django.dispatch

upload_recieved = django.dispatch.Signal(providing_args=['data'])

def upload(request, *args, **kwargs):
    if request.method == 'POST':
        if request.FILES:
            upload_recieved.send(sender='uploadify', data=request.FILES['Filedata'])
    return HttpResponse('True')


