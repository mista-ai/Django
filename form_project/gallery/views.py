from django.shortcuts import render
from django.views.generic import View


class GalleryView(View):
    def get(self, request):
        return render(request, 'gallery/load_file.html')

    def post(self, request):
        pass
