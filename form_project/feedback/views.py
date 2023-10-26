from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views.generic import ListView, DetailView, TemplateView, FormView, View, CreateView, UpdateView


class FeedBackViewUpdate(UpdateView):
    model = Feedback
    # здесь форму настроить нельзя, только наличие полей
    fields = ['name']
    # Форму можно не указаывать, форма сформируется на основе model
    # Предпочтительней использовать form_class, чтобы настраивать форму
    # form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

class FeedBackView(CreateView):
    model = Feedback
    # здесь форму настроить нельзя, только наличие полей
    fields = '__all__'
    # Форму можно не указаывать, форма сформируется на основе model
    # Предпочтительней использовать form_class, чтобы настраивать форму
    # form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivanov I. I.'
        context['date'] = '25.10.23'
        return context


class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedbacks'
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     filter_qs = queryset.filter(rating__gt=4)
    #     return filter_qs


class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
    context_object_name = 'feedback'


# class FeedBackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})


# class FeedBackUpdateView(View):
#     def get(self, request, id_feedback):
#         feed = Feedback.objects.get(id=id_feedback)
#         form = FeedbackForm(instance=feed)
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request, id_feedback):
#         feed = Feedback.objects.get(id=id_feedback)
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(f'/{id_feedback}')
#         return render(request, 'feedback/feedback.html', context={'form': form})

# class DetailFeedBack(TemplateView):
#     template_name = 'feedback/detail_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feedback'] = Feedback.objects.get(id=context['id_feedback'])
#         return context


# class ListFeedBack(TemplateView):
#     template_name = 'feedback/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feedbacks'] = Feedback.objects.all()
#         return context
