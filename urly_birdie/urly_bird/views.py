from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils import timezone
from django.views.generic import CreateView, ListView, View, DetailView, UpdateView, DeleteView
from urly_bird.forms import BookmarkForm
from urly_bird.models import Bookmark, Click


class ListBookmarks(ListView):
    model = Bookmark
    queryset = Bookmark.objects.annotate(num=Count('click__bookmark')).order_by('-num')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context


class ListUserBookmarks(ListView):
    model = Bookmark
    template_name = 'urly_bird/bookmark_user_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Bookmark.objects.filter(human__username=self.request.user.username).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_load'] = timezone.now()
        return context
"""
class AnyUserBookmarks(ListView):
    model = Bookmark
    template_name = 'urly_bird/zzzzz.html'

    def dispatch(self, request, *args, **kwargs):
        thing = args

    def get_queryset(self):
        return Bookmark.objects.filter(human__username=thing)
"""

class CreateBookmark(CreateView):
    model = Bookmark
    form_class = BookmarkForm
    success_url = reverse_lazy('list_bookmarks')

    def form_valid(self, form):
        form.instance.human = self.request.user
        return super(CreateBookmark, self).form_valid(form)


class BookmarkDetail(DetailView):
    model = Bookmark


class UpdateBookmark(UpdateView):
    model = Bookmark
    form_class = BookmarkForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('list_bookmarks')

    def form_valid(self, form):
        form.instance.human = self.request.user
        return super(UpdateBookmark, self).form_valid(form)


class DeleteBookmark(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list_bookmarks')


def link(request, link_id):
    bkmrk_id = Bookmark.decode_id(link_id)
    bookmark = get_object_or_404(Bookmark, pk=bkmrk_id)
    if request.user.is_authenticated():
        Click.objects.create(human=request.user, bookmark=bookmark)
    else:
        Click.objects.create(bookmark=bookmark)
    return redirect(bookmark.url)

def user_list(request, user_name):
    bookmarks = get_list_or_404(Bookmark.objects.all().filter(human__username=user_name))
    return render(request, 'urly_bird/any_user_list.html', {'bookmarks': bookmarks})