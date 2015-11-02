from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from users.forms import RegistrationForm


class Register(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, *args, **kwargs):
        form = RegistrationForm(self.request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_name = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('bookmark_create'))

        return render(self.request, 'registration/register.html', {'form': form})
