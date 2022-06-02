from django.views import generic
from .models import Post

class AbooutPage(generic.DetailView):
    template_name = 'about.html'