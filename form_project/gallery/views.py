from django.shortcuts import render
from django.views.generic import View, CreateView
from .forms import GalleryUploadForm
from django.http import HttpResponseRedirect
from .models import Gallery



class CreateGalleryView(CreateView):
    model = Gallery
    form_class = GalleryUploadForm
    template_name = 'gallery/load_file.html'
    success_url = '/load_image'


# class GalleryView(View):
#     def get(self, request):
#         form = GalleryUploadForm()
#         return render(request, 'gallery/load_file.html', {'form': form})
#
#     def post(self, request):
#         form = GalleryUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_image = Gallery(image=form.cleaned_data['image'])
#             new_image.save()
#             return HttpResponseRedirect('load_image')
#         return render(request, 'gallery/load_file.html', {'form': form})
