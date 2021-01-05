from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
import configparser
from linebot.models import MessageEvent,TextMessage,FlexSendMessage,TextSendMessage,QuickReply,QuickReplyButton,MessageAction

import os
import psycopg2
import requests
import json
import datetime
import re

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))



@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    line_bot_api.reply_message(
        event.reply_token,
        FlexSendMessage(alt_text= 'hi', 
                contents = { 'type': 'bubble', 'direction': 'ltr',
                    'hero': {
                        'type': 'image',
                        'url': 'https://example.com/cafe.jpg',
                        'size': 'full',
                        'aspectRatio': '20:13',
                        'aspectMode': 'cover',
                        'action': { 'type': 'uri', 'uri': 'http://example.com', 'label': 'label' }
                    }
                }
        )
    )

if __name__ == "__main__":
    app.run()

