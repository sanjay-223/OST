from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    principle = float(request.form['principle'])
    rate = float(request.form['rate'])
    years = int(request.form['years'])

    future_value = round(principle * (1 + (rate / 100)) ** years,2)
    double_time = round(72/rate)
    return render_template('result.html', future_value=future_value,double_time=double_time)

if __name__ == '__main__':
    app.run(debug=True)
