from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
# from django.http import HttpResponse
from django.urls import reverse
# from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from .models import Post, Author


def starting_page(request):
    posts = Post.objects.all().order_by("-date")[:3]

    
    authors = Author.objects.all().order_by("last_name")
    num_posts = posts.count()
    #  sorted_posts = sorted(all_posts, key = get_date)
    #  latest_posts = sorted_posts[-3]
    num_authors = authors.count()
    
    return render(request, "blog/index.html", {
                  "posts" : posts,
                  "total_number_of_books": num_posts,
                  "total_number_of_authors": num_authors
                  })

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html",{
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })

def posts(request):
    all_posts = Post.get_objects.all().order_by("-date")
    return render(request, "blog/all-posts.html",{
        "all_posts": all_posts
    })

