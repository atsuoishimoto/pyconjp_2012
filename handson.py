# -*- coding: utf-8 -*-

from flask import Flask, request, session, render_template
from flask import redirect, url_for

# Flaskのアプリケーション オブジェクトを作成
app = Flask(__name__)


# http://localhost:5000/でアクセスされる関数
@app.route('/')
def index_html():
    return """
<!doctype html>
<ul>
    <li><a href="/message_form">メッセージ追加</a></li>
    <li><a href="/show">メッセージ表示</a></li>
</ul>
"""

# /message_formでアクセスされる関数
@app.route('/message_form')
def message_form():
    # テンプレートファイル templates/message_form.htmlを表示
    return render_template('message_form.html')


# /add_messageでリクエストのメッセージを登録
@app.route('/add_message', methods=['POST'])
def add_message():
    # Sessionにメッセージを登録
    msgs = session.get('messages', [])
    msgs.append(request.form['message'])
    session['messages'] = msgs[-10:]
    return redirect(url_for('show_messages'))


# /showでリクエストのメッセージを登録
@app.route('/show')
def show_messages():
    # テンプレートファイル templates/show_messages.htmlを表示
#    return render_template('show_messages.html',
#                           messages=reversed(session['messages']))
    import cProfile
    localvars = {}
    cProfile.runctx("""ret = render_template('show_messages.html',
                           messages=reversed(session['messages']))""",
                           globals(), localvars, sort='cumulative') 

    return localvars["ret"]

def main():
    app.secret_key = "secret"
    app.logger.setLevel
    app.run(debug = True)
    
if __name__ == '__main__':
    main()
