# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, u r @ index.")

def detail(request, sentence_id):
    return HttpResponse("this is sentence number %s." % sentence_id)

