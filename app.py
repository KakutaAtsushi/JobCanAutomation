import ssl

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('./static/openssl/server.crt', './static/openssl/server.key')

app = Flask(__name__)

LINE_API_SECRET = 'd68ef49da1c787941c2586b079560462'
LINE_API_ACCESS_TOKEN = 'pHJVkgryk5rrT85hLtMCh++S02PByBekeGIjc1hEJdYJegF6AEKVWyg1x14OWMBINRzHrnjnDtswVldz3SWZyQCtT9P' \
                        '/2KSSd0rHTyNVF/df6CDtxyEdgahljbx2q7+1og+r4nWP1bSpxXKdqwJ/YwdB04t89/1O/w1cDnyilFU= '

line_bot_api = LineBotApi(LINE_API_ACCESS_TOKEN)
handler = WebhookHandler(LINE_API_SECRET)


@app.route("/", methods=["GET"])
def index():
    return "success";


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "出勤":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="出勤しました"))
    if event.message.text == "退勤":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="退勤しました"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=334, ssl_context=context,
            threaded=True,
            debug=True)
