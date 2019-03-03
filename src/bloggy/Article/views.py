from django.shortcuts import render
from .form import article_form
from .models import article
# Create your views here.
from django.views.generic import (
   ListView,
   CreateView,
   DetailView,
   DeleteView,
   UpdateView,
)

def article_list_view(request):
    form = article_form(request.POST)
    if request.method=="POST":
        #form.save()
        article.objects.create(title)
    
    context = {
       "title": form.title,
    }
    return render(request,'article_detail.html',context)