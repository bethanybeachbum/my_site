from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
# from django.http import HttpResponse
from django.urls import reverse
# from django.template.loader import render_to_string

# Create your views here.
# / root view
def starting_page(request): 
    return render(request, "blog/index.html", {
    })
    
def posts(request):
    return render(request, "blog/all-posts.html",)

def post_detail(request, slug):
    return render(request, "blog/post-detail.html" )

# / posts view
# / posts slug view
