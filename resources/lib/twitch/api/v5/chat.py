# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/v5/reference/chat/

from twitch import keys
from twitch.queries import V5Query as Qry
from twitch.queries import query


@query
def get_emoticons_by_set(emotesets=None):
    q = Qry('chat/emoticon_images')
    q.add_param(keys.EMOTESETS, emotesets, None)
    return q


@query
def get_badges_by_channel(channel_id):
    q = Qry('chat/{channel_id}/badges')
    q.add_urlkw(keys.CHANNEL_ID, channel_id)
    return q


@query
def get_all_emoticons():
    q = Qry('chat/emoticons')
    return q
