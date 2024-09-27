from flask import Flask, render_template, request  # type: ignore
import math
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO) 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hesablama', methods=['POST'])
def hesablama():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        result = f"İki fərqli real kök: x1 = {x1}, x2 = {x2}"
    elif D == 0:
        x = -b / (2*a)
        result = f"İki eyni real kök: x = {x}"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-D) / (2*a)
        result = f"İki kompleks kök: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
