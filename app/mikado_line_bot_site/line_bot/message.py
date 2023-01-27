"""This module loads message templates.
"""
from enum import Enum
import string

class Templates:
    """Cache message templates on memory
    """
    class Lang(Enum):
        all = 0
        en = 1
        ja = 2

    def __init__(self):
        self.en=None
        self.ja=None

    def load(self, lang:Lang=Lang.all):
        if self.Lang.en == lang or self.Lang.all == lang:
            pass
if self.Lang.en == lang or self.Lang.all == lang:
        pass


with open('mail_template.txt') as f:
    t = string.Template(f.read())

mail_text = t.substitute(name='山田', contents='今日は良い天気ですね。')
print(mail_text)
