from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import HttpRequest
from .forms import FeebackForm


# Create your views here.
def index(request: HttpRequest):
    if request.method == 'POST':
        form = FeebackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/done')
    form = FeebackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})


def done(request: HttpRequest):
    return render(request, 'feedback/done.html')
