from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import HttpRequest
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView


class FeedBackView(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})


class FeedBackUpdateView(View):
    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
        return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivanov I. I.'
        context['date'] = '25.10.23'
        return context


class ListFeedBack(TemplateView):
    template_name = 'feedback/list_feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedbacks'] = Feedback.objects.all()
        return context

class DetailFeedBack(TemplateView):
    template_name = 'feedback/detail_feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedback'] = Feedback.objects.get(id=context['id_feedback'])
        return context