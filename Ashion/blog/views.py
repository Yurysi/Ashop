from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Author, Entry
from datetime import date
from .forms import EntryForm

def blog(request):
    return render(request, "blog/blog.html")

def new_post(request):
    if request.method == 'GET':
        context = {'form': EntryForm()}
        return render(request, "blog/new_post.html", context)
    elif request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            return render(request, 'blog/new_post.html', {'form': form})
def blog_home(request):
    posts = Entry.objects.all()
    context = {'posts': posts}
    return render(request, "blog/blog.html", context)
