from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply

app = Flask(__name__)

@app.route("/") #just to test Heroku cloud services
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    replies  = fetch_reply(msg, phone_no)

# Create reply
    resp = MessagingResponse()
    for reply in replies:
        resp.message(reply.text)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
