from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
import configparser
from linebot.models import (
    MessageEvent,TextMessage,FlexSendMessage,TextSendMessage,QuickReply,QuickReplyButton,MessageAction
)
import psycopg2
import requests
import json

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

    inputtext = str(event.message.text)
    inputtext = inputtext.lower()

    if 'sorting' in inputtext:
        if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
            flexsort = json.load(open('sort.json','r',encoding='utf-8'))
            line_bot_api.reply_message(event.reply_token, FlexSendMessage('sorting',flexsort))


    elif 'tree' in inputtext :
        if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
            flextree = json.load(open('tree.json','r',encoding='utf-8'))
            line_bot_api.reply_message(event.reply_token, FlexSendMessage('tree',flextree))


    elif 'hash' in inputtext:
        if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
            flexhash = json.load(open('hash.json','r',encoding='utf-8'))
            line_bot_api.reply_message(event.reply_token, FlexSendMessage('sorting',flexhash))

    

if __name__ == "__main__":
    app.run()

