from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    # Get the input data from the form
    input_data = request.form['input']

    # Run your Python code with the input data
    result = run_your_code(input_data)

    # Pass the result to the template
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)