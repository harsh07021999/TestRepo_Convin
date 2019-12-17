from django.shortcuts import render

# Create your views here.
from .models import MyModel

# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='home.html',
                  context = {"test":MyModel.objects.all})