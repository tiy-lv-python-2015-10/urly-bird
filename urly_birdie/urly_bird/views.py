from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import CreateView, ListView
from urly_bird.forms import BookmarkForm
from urly_bird.models import Bookmark


class ListBookmarks(ListView):
    model = Bookmark
    queryset = Bookmark.objects.order_by('-created_at')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context

class CreateBookmark(CreateView):
    model = Bookmark
    form_class = BookmarkForm
    success_url = reverse_lazy('list_bookmarks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBookmark, self).form_valid(form)
"""
class ShortUrlUpdate(UpdateView):
    pass

class ShortUrlDelete(DeleteView):
    pass

"""