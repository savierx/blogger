from django.shortcuts import render, render_to_response, get_object_or_404
from django.db.models import Q

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost, Art, Category

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))

#cms
def category(request, slug):
    """Given a category slug, display all items in a category."""
    category = get_object_or_404(Category, slug=slug)
    art_list = Art.objects.filter(category=category)
    heading = "Category: %s" % category.label
    return render_to_response("blog/art_list.html", locals())


def search(request):
    """
    Return a list of stories that match the provided search term
    in either the title or the main content.
    """
    if 'q' in request.GET:
        term = request.GET['q']
        art_list = Art.objects.filter(Q(title__contains=term) | Q(markdown_content__contains=term))
        heading = "Search results"
    return render_to_response("blog/art_list.html", locals())

