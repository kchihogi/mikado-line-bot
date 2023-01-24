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
        MessageEvent, TextMessage, ImageMessage, VideoMessage, AudioMessage, FileMessage, LocationMessage, StickerMessage
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
def handle_text_message(event):
    """MessageEvent-text
    """
    MessageEventHandler(event).text_message_replay()

@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    """MessageEvent-image
    """
    MessageEventHandler(event).image_message_replay()

@handler.add(MessageEvent, message=VideoMessage)
def handle_video_message(event):
    """MessageEvent-video
    """
    MessageEventHandler(event).video_message_replay()

@handler.add(MessageEvent, message=AudioMessage)
def handle_audio_message(event):
    """MessageEvent-audio
    """
    MessageEventHandler(event).audio_message_replay()

@handler.add(MessageEvent, message=FileMessage)
def handle_file_message(event):
    """MessageEvent-file
    """
    MessageEventHandler(event).file_message_replay()

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    """MessageEvent-location
    """
    MessageEventHandler(event).location_message_replay()

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    """MessageEvent-Sticker
    """
    MessageEventHandler(event).sticker_message_replay()
