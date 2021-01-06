# Data-Structure-Chatbot

## Platform
front-end : LINE API, LINE Login(LIFF), Rich Menu, Flex Message<br>
back-end : Heroku<br>
All the information about data structure come from [here](https://github.com/iitsmel/iitsmel.io).<br>
<br>

## Problems I've encountered & currently solved
- unable to successfully verify Webhook URL<br>
enter following commands works for me<br>
> git add .<br>
> git commit -am "your previous input"<br>
<br>
"your previous input" is what you entered the very first time.<br>
<br>

> git push heroku main<br>
> heroku logs --tail<br>
<br>
"heroku logs --tail" will show all logs in terminal.<br>
<br>
This step is not necessery but very handy and convinent when you don't want to switch
to Heroku Application log page.<br>
<br>

- a little bit confused about flex message<br>
Here's my conclution about flex message:
<br>

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

<br>
Make sure to put "from linebot.models import FlexSendMessage" in code.<br>
"line_bot_api.reply_message" will give you the leverage to be able to send a message through bot.<br>
" event.reply_token" means that the bot will reply to this specific token.<br>
Finally, here's the flex message part.<br>
"alt_text" is a must because whatever you type in or put behind will represent the user's reply(to the bot).<br>
By recognizing this reply, the bot will send a flex message.<br>
In other words, "alt_text" is sort of a trigger word.<br>
"contents" is what your flex message should look like.<br>
So there you go, can't make a flex message out of empty alt_text and contents.<br>

<br>

## Language
Python
<br>

## Colors Section
thoughts : Panton COLOR OF THE YEAR 2021, FRIENDS<br>

![](https://i.imgur.com/JI0JsJo.png)
- PANTONE 17-5104 Ultimate Gray #939597
- PANTONE 13-0647 Illuminating #F5DF4D

<br>

![](https://i.imgur.com/181dnHc.png)
- background : #FFF580
- shade : #00009E
- word : #42A2D6

<br>

![](https://i.imgur.com/cBVIqR5.png)
- background : #9C8CD4
- shade : #665236
- word : #D2C385

<br>

![](https://i.imgur.com/H8VdspH.png)
- background : #FFDC00
- shade : #9A0006
- word : #FF4238
