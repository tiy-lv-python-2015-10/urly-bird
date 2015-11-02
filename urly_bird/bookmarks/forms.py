from django import forms
from django.forms import Textarea
from bookmarks.models import Bookmark


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('title', 'description', 'bookmark_url')
        widgets = {
            'message': Textarea(attrs={'rows': 2})
        }
