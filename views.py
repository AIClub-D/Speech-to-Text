from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def main(request):
    if request.method=="GET":
        str="다시 말씀해주세요.."
        return HttpResponse(str)

    #넘겨받은 값을 그대로 반환
    elif request.method=="POST":
        response=request.POST['sentence']
        return HttpResponse(response)