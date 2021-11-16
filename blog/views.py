from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date')
    # To count all the blocks instead of 5 create this line
    # blog_count = Blog.objects.count() // and add the variable into the below code instead of [:5]
    blogs = Blog.objects.order_by('-date')[:5]  #Give me the last 5 positions of the DB entries
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

#S5L46 Adding blog details number to the URL
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    #return render(request, 'blog/detail.html', {'id':blog_id})
    return render(request, 'blog/detail.html', {'blog': blog})
