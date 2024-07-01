from flask import Flask, jsonify, make_response, request
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('EMAIL')

mail = Mail(app)

@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    receiver_email = data.get('receiver_email')
    subject = data.get('subject')
    body_text = data.get('body_text')

    if not receiver_email or not subject or not body_text:
        return jsonify({'message': 'All fields are required: receiver_email, subject, body_text'}), 400

    try:
        msg = Message(subject, recipients=[receiver_email], body=body_text)
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'Internal Server Error'}), 500

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

if __name__ == '__main__':
    app.run(debug=True)