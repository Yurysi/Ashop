from django.forms import ModelForm
from .models import Entry, Hotel

# class EntryForm(ModelForm):
#     class Meta:
#         fields = ['blog', ' headline', 'body_text', 'pub_date', 'authors', 'rating']
class EntryForm(ModelForm):

    class Meta:
        model = Entry
        fields = ['title', 'content', 'authors', 'categories']


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']