from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse

EXEMPT_URLS=[
    reverse('login'),
    reverse('register'),
    reverse('firstpage'),
]

class LoginRequiredMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        

    def __call__(self,request):
        path=request.path_info

        if not request.user.is_authenticated and path not in EXEMPT_URLS:
            return redirect(settings.LOGIN_URL)

        response=self.get_response(request)
        return response        