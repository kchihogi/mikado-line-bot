"""Mikado Line Bot views.
"""
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

from linebot import WebhookHandler

from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
        MessageEvent, TextMessage
)

from line_bot.line_events import MessageEventHandler

handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """MessageEvent
    """
    MessageEventHandler(event).replay()
