from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
class ComingView(TemplateView):
    template_name = 'construction/comingsoon.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(ComingView, self).dispatch(*args, **kwargs)


def comingsoon(request):
    if not request.user.is_authenticated:
        return render(request, 'construction/comingsoon.html', '')
    else:
        return HttpResponseRedirect('/portfolio_home/')
