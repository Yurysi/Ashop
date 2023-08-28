from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import new_post, blog_home, edit_post, delete_post, hotel_image_view

urlpatterns = [
    path('', blog_home, name='blog'),
    path('new_post/', new_post, name='new_post'),
    path('edit/<int:id>/', edit_post, name='post-edit'),
    path('delete/<int:id>', delete_post, name='post-delete'),
    path('image_upload/', hotel_image_view, name='image_upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
