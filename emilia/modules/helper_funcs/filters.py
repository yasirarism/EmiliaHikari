from telegram import Message
from telegram.ext import BaseFilter

from emilia import SUPPORT_USERS, SUDO_USERS


class CustomFilters(object):
    class _MimeType(BaseFilter):
        def __init__(self, mimetype):
            self.mime_type = mimetype
            self.name = "CustomFilters.mime_type({})".format(self.mime_type)

        def filter(self, message: Message):
            return bool(message.document and message.document.mime_type == self.mime_type)

    mime_type = _MimeType

    class _HasText(BaseFilter):
        def filter(self, message: Message):
            return bool(message.text or message.sticker or message.photo or message.document or message.video)

    has_text = _HasText()
