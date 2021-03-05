from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

@app.route('/')
def home():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기
    return render_template('home.html')


@app.route('/service_intro')
def service_intro():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기
    return render_template('service_intro.html')

# render_template 사용해보기
# == 사용자에게 보여줄 데이터를 HTML에 담기
@app.route('/service')
def service():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기


    
    return render_template('service.html')

@app.route('/answer')
def answer():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기


    
    return render_template('answer.html')
@app.route('/login')
def login():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기


    
    return render_template('login.php')

@app.route('/callback')
def callback():
    # HTML 반환해주기
    # 반드시 templates 폴더 안에 위치해야합니다.
    # render_template 불러와주기


    
    return render_template('callback.php')

# 파일 수정 시, 자동으로 반영해주는 코드
# 서버 껐다킬 필요 없음.
# 이제부터 python app.py로 서버 실행!
if __name__ == '__main__':
    app.run(debug=True)