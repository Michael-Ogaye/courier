from flask import Flask, render_template, request
import trycourier

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    # Get the new subscriber's email and name from the request
    email = request.form['email']
    name = request.form['name']

    # TODO: save the new subscriber to your database or mailing list

    # Send a welcome email using the courier API
    courier = trycourier.Client(auth_token='YOUR_AUTH_TOKEN')
    message = {
        'to': email,
        'subject': 'Welcome to our newsletter!',
        'body': f'Hi {name}, thanks for subscribing to our newsletter!'
    }
    response = courier.send(message)

    # Send a push notification using the courier API
    notification = {
        'event': 'new_subscription',
        'user': email,
        'data': {
            'name': name
        }
    }
    response = courier.track(**notification)

    return 'OK'

if __name__ == '__main__':
    app.run()
