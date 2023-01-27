"""Define webhook from line server with WebhookHandler.
"""
from django.conf import settings

from linebot import WebhookHandler
from linebot.models import (
        MessageEvent, FollowEvent, UnfollowEvent,
        TextMessage,
        ImageMessage,
        VideoMessage,
        AudioMessage,
        FileMessage,
        LocationMessage,
        StickerMessage
)

from line_bot.line_events import (
    MessageEventHandler,
    FollowEventHandler
)

handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

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

@handler.add(FollowEvent)
def handle_follow(event):
    """FollowEvent
    """
    FollowEventHandler(event).follow_replay()

@handler.add(UnfollowEvent)
def handle_unfollow(event):
    """UnfollowEvent
    """
    FollowEventHandler(event).unfollow()
