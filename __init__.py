from django.db.models import signals
from django.dispatch import dispatcher
from django.contrib.comments.models import Comment

import html5lib
from html5lib import sanitizer


def sanitize_comment(sender, instance, **kwargs):
    p = html5lib.HTMLParser(tokenizer=sanitizer.HTMLSanitizer)
    # childNodes[0] -> html, childNodes[1] -> body, the 6:-7 drops the open/close body tags
    instance.comment = p.parse(instance.comment).childNodes[0].childNodes[1].toxml()[6:-7]

signals.pre_save.connect(sanitize_comment, sender=Comment)
