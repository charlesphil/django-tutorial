from django.shortcuts import render
from .models import Post


# Blog home page route
def home(request):
    # Calls all blog posts from database and passes it into the posts key to
    # the page via Jinja
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# Blog about page route
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
