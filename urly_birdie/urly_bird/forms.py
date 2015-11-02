from django import forms
from urly_bird.models import Bookmark


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('title', 'url', 'description')
