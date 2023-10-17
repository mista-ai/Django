from django.shortcuts import render


# Create your views here.

def get_beautiful_table_index(request):
    return render(request, 'beautiful_table/index.html')
