"""Mikado Line Bot views.
"""
import json

# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


from django.conf import settings

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

# from utils import message_creater
# from line_bot.line_message import LineMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
