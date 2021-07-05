from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_http_methods


# @require_http_methods(['GET'])
def testPost(request):
    dic = {}
    print(request)
    urls = ["http://47.101.213.106:8080/pic/5.jpg",
            "http://47.101.213.106:8080/pic/6.jpg",
            "http://47.101.213.106:8080/pic/7.jpg",
            "http://47.101.213.106:8080/pic/8.jpg",
            "http://47.101.213.106:8080/pic/9.jpg",
            "http://47.101.213.106:8080/pic/3.jpg",
            "http://47.101.213.106:8080/pic/4.jpg",
            "http://47.101.213.106:8080/pic/2.jpg",
            "http://47.101.213.106:8080/pic/10.jpg",
            "http://47.101.213.106:8080/pic/1.jpg"]
    dic["urls"] = urls
    print(dic)
    return JsonResponse(dic)


def hello(request):
    return HttpResponse("Hello world ! ")

from toolservice.tools.rouge_metric import test_rouge
def use_rouge(request):
    content = eval(request.body)
    print(content)
    cand = content['candidates'].split('\n')
    ref = content['refrences'].split('\n')
    lang = 'zh'
    a = test_rouge(cand, ref, lang)
    return JsonResponse({'data':a})
