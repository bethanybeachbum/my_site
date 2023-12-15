from django.urls import path
# the dot says import files from the same folder
from . import views

# this creates a URLconf
urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]
