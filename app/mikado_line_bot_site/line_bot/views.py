"""Mikado Line Bot views.
"""
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from linebot.exceptions import (
    InvalidSignatureError
)

from line_bot.handler import handler

@csrf_exempt
def index(request):
    """index page.
    """
    # get X-Line-Signature header value
    if request.method == 'POST':
        signature = request.headers['X-Line-Signature']
        body = request.body.decode(request.encoding)
        # handle webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            print("Invalid signature. Please check your channel access token/channel secret.")
            return HttpResponseBadRequest
        return HttpResponse("ok")
    return HttpResponseBadRequest
