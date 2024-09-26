### Integrate HTML With Flask
### HTTP verb GET And POST

##Jinja2 templates engine
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    print(f"Score received: {score}, Type: {type(score)}")  # Debug
    res = "PASS" if score >= 50 else "FAIL"
    exp = {'score': score, 'res': res}
    return render_template('result.html', result=exp)
    # return render_template('result.html', result=score)

# @app.route('/fail/<int:score>')
# def fail(score):
#     return "The Person has failed and the marks is " + str(score)


@app.route('/results/<int:marks>')
def results(marks):
    print(f"Marks received: {marks}, Type: {type(marks)}")  # Debug
    result = 'fail' if marks < 50 else 'success'
    return redirect(url_for(result, score=marks))

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        try:
            science = float(request.form['science'])
            maths = float(request.form['maths'])
            c = float(request.form['c'])
            data_science = float(request.form['datascience'])
            total_score = (science + maths + c + data_science) / 4
        except ValueError:
            return "Invalid input. Please enter numeric values."
    print(f"Total Score: {total_score}, Type: {type(total_score)}")  # Debug
    return redirect(url_for('success', score=total_score))

if __name__ == '__main__':
    app.run(debug=True)