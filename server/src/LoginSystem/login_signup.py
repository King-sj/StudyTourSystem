__all__ = ['login_signup_blueprint']
from .signUp import generate_captcha, register_account, login as login_account
from flask import Blueprint, jsonify, request
from src.smtp import send_email
login_signup_blueprint = Blueprint('login_signup', __name__)


@login_signup_blueprint.route("/captcha", methods=['GET', 'POST'])
async def getCaptcha():
  data = request.json
  if not data:
    return jsonify({"err": 'not found request body'})

  email = data['email']
  # TODO(SJ) add email check
  print("captcha : ", email)
  captcha = await generate_captcha(email)
  send_email(email, "BUPT", """
      您的验证码为{}
      """.format(captcha)
             )
  print('captcha:', captcha)
  return jsonify({"res": 'ok'})


@login_signup_blueprint.route("/signup", methods=['GET', 'POST'])
async def register():
  data = request.json
  if not data:
    return jsonify({"err": 'not found request body'})
  account = data['email']
  captcha = data['captcha']
  psw = data['password']
  res = await register_account(account, psw, captcha)
  print(res)
  return jsonify({"res": res})


@login_signup_blueprint.route("/login", methods=['GET', 'POST'])
async def login():
  data = request.json
  if not data:
    return jsonify({
        'err': 'not found request body',
        'login': False
    })
  account = data['email']
  psw = data['password']
  res = await login_account(account, psw)
  print(res)

  if (not res[0]):
    return jsonify({
        'err': 'account or password error',
        'login': res[0]
    })
  return jsonify({
      'token': res[1],
      'login': res[0]
  })
