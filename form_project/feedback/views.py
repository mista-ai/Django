from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import HttpRequest


# Create your views here.
def index(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST['name']
        if len(name) == 0 or len(name) > 20:
            return render(request, 'feedback/feedback.html', context={'got_error': True})
        print(name)
        return HttpResponseRedirect('/done')
    return render(request, 'feedback/feedback.html', context={'got_error': False})

def done(request: HttpRequest):
    return render(request, 'feedback/done.html')
