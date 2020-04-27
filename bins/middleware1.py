from django.conf import settings
from django.shortcuts import redirect, render


class ML:
    def __init__(self, get_response):
        self.get_response = get_response
        print(get_response)

    def __call__(self, request):
        # print(request, "ok")
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        first add login-url in settings.py
            LOGIN_REDIRECT_URL = '/map/'
            LOGIN_URL = '/account/login/'

        :param request:
        :param view_func:
        :param view_args:
        :param view_kwargs:
        :return:
        """

        assert hasattr(request, 'user')
        '''
        In older versions of Django request.user.is_authenticated was a method. It's now an attribute and no longer requires parenthesis. If you change your code to:
        if request.user.is_authenticated:
        '''
        # print(request.user.is_authenticated, settings.LOGIN_REDIRECT_URL)
        # print(request.path_info)
        if not request.user.is_authenticated:
            # return redirect(settings.LOGIN_REDIRECT_URL)
            # https: // docs.djangoproject.com / en / 3.0 / topics / http / shortcuts /
            # return redirect('map.')
            return render(request, 'stock/login.html')
        else:
            print('user has login')






