from django.shortcuts import render, render_to_response, get_object_or_404
from django.db.models import Q

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost, Art, Category
from django.views.generic import *
from django.urls import reverse

def index(request):
    return HttpResponse('hola')

def detail(request, slug):
    return HttpResponse("You're looking at question %s." % slug)

def results(request, slug):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % slug)

def vote(request, pk):
    return HttpResponse("You're voting on question %s." % pk)
##############################
class ArchiveView(ListView):
    template_name = 'blog/archive.html'
    context_object_name = 'posts'
    #c = Context({ 'posts': posts })
    
    def get_queryset(self):
        return BlogPost.objects.all()

    def get_context_data(self, **kwargs):
        return render('template_name','context')
    
    
    #return HttpResponse(t.render(c))


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

class CategoryView(DetailView):
    model = Category
    template_name = 'blog/art_list.html'
    #context_object_name =

class ArtView(DetailView):
    model = BlogPost
    template_name = 'blog/art_detail.html'
    #context_object_name =

class HomeView(ListView):
    model = Art
    template_name = 'blog/art_list.html'
    #context_object_name =
