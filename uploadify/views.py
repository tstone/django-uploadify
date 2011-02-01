from django.http import HttpResponse
import django.dispatch

upload_received = django.dispatch.Signal(providing_args=['data'])

def upload(request, *args, **kwargs):
    if request.method == 'POST':
        if request.FILES:
            upload_received.send(sender='uploadify', data=request.FILES['Filedata'])
    return HttpResponse('True')


