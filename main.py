from flask import Flask, render_template,  request
import requests

def sendMsgTelegram(msg):
    TOKEN = '6990045057:AAFj6StkQ3A-GAimfNp2JWH133lldSdGJrg'
    chat_id = "1659836007"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url).json()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_message', methods=['POST'])
def process_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        phone = request.form.get('phone', '')
        message = request.form['message']
        msg_making = "Name: "+name+"\nEmail: "+email+"\nSubject: "+subject+"\nPhone: "+phone+"\nMessage: "+message
        print(msg_making)
        sendMsgTelegram(msg_making)
        return render_template('index.html', message_sent=True)

    return 'Invalid request method'



if __name__ == '__main__':
    app.run(debug=False)