from rest_framework.authentication import BaseAuthentication

class MyAuth(BaseAuthentication):
    # request: Request
    def authenticate(self, request):
        pass
    def authenticate_header(self, request):
        pass