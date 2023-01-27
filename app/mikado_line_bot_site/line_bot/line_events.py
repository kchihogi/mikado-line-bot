"""This module handles line event objects.

# Message event
# Unsend event
# Follow event
# Unfollow event
# Join event
# Leave event
# Member join event
# Member leave event
# Postback event
# Video viewing complete event
# Beacon event
# Account link event
# Device link event
# Device unlink event
# LINE Things scenario execution event

link: https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects
"""

from django.conf import settings

from linebot import LineBotApi
from linebot.exceptions import LineBotApiError

from linebot.models import (
    Event, TextSendMessage
)

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

class EventHandler():
    """This class is super class for line envet objects.
    """
    def __init__(self, event:Event):
        self.event = event
        self.type = event.type
        self.mode = event.mode #active/standby
        self.send = None

    def replay(self):
        """replay message to user.
        """
        event = self.get_event()
        if "active" == self.get_mode():
            line_bot_api.reply_message(event.reply_token, self.send)

    def get_event(self):
        """get event

        Returns:
            linebot.models.Event: an event object
        """
        return self.event

    def get_type(self):
        """get type

        Returns:
            String: an event type.
        """
        return self.type

    def get_mode(self):
        """get mode

        Returns:
            String: Channel state. The state should be "active" or "standby".
        """
        return self.mode

class MessageEventHandler(EventHandler):
    """Message event

    Args:
        EventBase (EventBase): EventBase class.
    """

    def text_message_replay(self):
        """make a response of user text message.
        """
        event = super().get_event()
        self.send = TextSendMessage(text=event.message.text)
        self.replay()

    def image_message_replay(self):
        """make a response of user image message.
        """
        # event = super().get_event()
        self.send = TextSendMessage(text="image?")
        self.replay()

    def video_message_replay(self):
        """make a response of user video message.
        """
        # event = super().get_event()
        self.send = TextSendMessage(text="videoe?")
        self.replay()

    def audio_message_replay(self):
        """make a response of user audio message.
        """
        # event = super().get_event()
        self.send = TextSendMessage(text="audio?")
        self.replay()

    def file_message_replay(self):
        """make a response of user file message.
        """
        # event = super().get_event()
        self.send = TextSendMessage(text="file?")
        self.replay()

    def location_message_replay(self):
        """make a response of user location message.
        """
        # event = super().get_event()
        self.send = TextSendMessage(text="location?")
        self.replay()

    def sticker_message_replay(self):
        """make a response of user sticker message.
        """
        # event = super().get_event()
        self.send = TextSendMessage(text="sticker?")
        self.replay()

class FollowEventHandler(EventHandler):
    """Follow and Unfollow event

    Args:
        EventBase (EventBase): EventBase class.
    """

    def follow_replay(self):
        """make a response of user text message.
        """
        event = super().get_event()
        try:
            profile = line_bot_api.get_profile(event.source.user_id)
            print(f"display_name:{profile.display_name}")
            print(f"user_id:{profile.user_id}")
            print(f"picture_url:{profile.picture_url}")
            print(f"status_message:{profile.status_message}")
            print(f"language:{profile.language}")
            msg=f"{profile.display_name}さん、はじめまして。"
            self.send = TextSendMessage(text=msg)
            self.replay()
        except LineBotApiError as err:
            print(f"Message:{err.message}({err.status_code})")

    def unfollow(self):
        """make a response of user text message.
        """
        event = super().get_event()
        print(f"unfollow envent. user:{event.source.user_id}")
