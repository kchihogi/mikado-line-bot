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

from linebot.models import (
    TextSendMessage, Event
)

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

class EventHandler():
    """This class is super class for line envet objects.
    """
    def __init__(self, event:Event):
        self.event = event
        self.type = event.type
        self.mode = event.mode #active/standby

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

    def replay(self):
        """replay message to user.
        """
        event = super().get_event()
        if "active" == super().get_mode():
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
