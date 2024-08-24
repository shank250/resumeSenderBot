from flask import Flask, send_file, request
import datetime

app = Flask(__name__)

@app.route('/pixel.png')
def track_open():
    email = request.args.get('email')
    print(email)
    with open('tracking.log', 'a') as f:
        f.write(f"{email} opened at {datetime.datetime.now()}\n")
    return send_file('pixel.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)