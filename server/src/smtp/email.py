__all__ = ['send_email']
from flask_mail import Mail, Message
from flask import render_template, request, jsonify
from src.utils.global_var import app


def send_email(to: str, subject: str, body: str, username: str = "用户"):
  mail = Mail(app)
  msg = Message(subject, recipients=[to])
  msg.html = render_template("email_template.html",
                             user=username, msg=body)
  mail.send(msg)
  if app.config['DEBUG']:
    print("Sent")
