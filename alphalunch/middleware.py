from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class SecretCheckMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        with open('secret.txt', 'r') as f:
            self.SECRET = f.read().rstrip()
        super(SecretCheckMiddleware, self).__init__(get_response)


    def process_request(self, request):
        try:
            secret = request.GET['s']
            if secret != self.SECRET:
                raise Exception()
        except:
            return HttpResponse('Permission Denied.')
        return None
