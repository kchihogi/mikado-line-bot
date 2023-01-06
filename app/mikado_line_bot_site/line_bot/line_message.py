"""This module controls a message to replay.
"""
import json
import urllib.request

# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

REPLY_ENDPOINT_URL = "https://api.line.me/v2/bot/message/reply"
ACCESSTOKEN = '***先ほど発行したアクセストークンをここに貼り付け***'
HEADER = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ACCESSTOKEN
}

class LineMessage():
    """Controler of a line message.
    """
    def __init__(self, messages):
        self.messages = messages

    def reply(self, reply_token):
        """reply a message.

        Args:
            reply_token (_type_): token from the line host server.
        """
        body = {
            'replyToken': reply_token,
            'messages': self.messages
        }
        print(body)
        req = urllib.request.Request(REPLY_ENDPOINT_URL, json.dumps(body).encode(), HEADER)
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read()
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err.reason)

    def dummy(self):
        """dummy method.
        """
        print("Hello World.")
