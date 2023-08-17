from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Author, Entry
from django.utils import timezone
from .forms import EntryForm, HotelForm


# def blog(request):
#     return render(request, "blog/blog.html")


def new_post(request):
    if request.method == 'GET':
        context = {'form': EntryForm()}
        return render(request, "blog/new_post.html", context)
    elif request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.pub_date = timezone.now()
            form.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('blog')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/new_post.html', {'form': form})


def blog_home(request):
    posts = Entry.objects.all()
    context = {'posts': posts}
    return render(request, "blog/blog.html", context)


def edit_post(request, id):
    post = get_object_or_404(Entry, id=id)

    if request.method == 'GET':
        context = {'form': EntryForm(instance=post), 'id': id}
        return render(request, 'blog/post_form.html', context)

    elif request.method == 'POST':
        form = EntryForm(request.POST, instance=post)
        if form.is_valid():
            post.published_at = timezone.now()
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('blog')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form': form})


def delete_post(request, id):
    post = get_object_or_404(Entry, pk=id)
    context = {'post': post}

    if request.method == "GET":
        return render(request, 'blog/post_confirm_delete.html', context)
    elif request.method == "POST":
        post.delete()
        messages.success(request, 'The post has been deleted successfully.')
        return redirect('blog')


def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'successfully uploaded.')
            return redirect('blog')
    else:
        form = HotelForm()
    return render(request, 'blog/hotel_image_form.html', {'form': form})

