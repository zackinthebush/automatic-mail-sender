from flask import Flask, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)
mail = Mail(app)

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
)

mail = Mail(app)

@app.route('/')
def send_email():
    message = Message('Hello from the other side!', sender=os.environ.get('MAIL_USERNAME'), recipients=['ymessaoudi47@outlook.com'])
    message.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
    mail.send(message)
    return 'Email sent!'

if __name__ == '__main__':
   app.run()
