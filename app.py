from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        # Escapar el input del usuario para prevenir XSS
        escaped_input = escape(user_input)
        if user_input != escaped_input:
            message = 'Posible intento de XSS detectado.'
        else:
            message = 'Input seguro: ' + escaped_input
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
