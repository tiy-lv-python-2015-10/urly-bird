from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.views.generic import View, ListView, DetailView, CreateView
from bookmarks.models import Bookmark
from bookmarks.forms import BookmarkForm
from django.views.generic import TemplateView
from django.shortcuts import render_to_response

# Create your views here.
class ListBookMarks(ListView):
    model = Bookmark
    queryset = Bookmark.objects.order_by('-timestamp')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context

class BookmarkDetail(DetailView):
    model = Bookmark


class CreateBookmark(CreateView):
    model = Bookmark
    form_class = BookmarkForm
    success_url = reverse_lazy('list_bookmarks')
    template_name = 'bookmarks/bookmark_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateBookmark, self).form_valid(form)

def welcome_page(request):
   return render_to_response('bookmarks/welcome_page.html')







