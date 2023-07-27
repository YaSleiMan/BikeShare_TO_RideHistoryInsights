from flask import Flask, request, render_template
from Selenium_GetData import selenium_getdata
from Present_Data import present_data
from Cost_Savings_Calculator import cost_savings_calculator
import shutil

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    # Get the input data from the form
    username = request.form['username']
    password = request.form['password']
    startDate = request.form['startDate']
    endDate = request.form['endDate']

    # Run your Python code with the input data
    # selenium_getdata(username, password, startDate, endDate)
    # present_data()
    costs = cost_savings_calculator()

    # Copy all files from the source directory to the destination directory
    shutil.rmtree('static')
    shutil.copytree('Outputs', 'static')

    # Outputs
    result_text = "By using Toronto Bike Share you've saved at least "+str(costs[0])+"$"+"\nYou were charged " + str(costs[1]) + "$ for ebike rides"

    result_image1 = "Outputs/RidesDurationsHist.png"
    result_image2 = "Outputs/RidesPerMonthHist.png"
    result_image3 = "Outputs/TimeOfDayHist.png"

    html_choice = request.form['html_choice']
    # Read the selected HTML template
    with open(f'static/{html_choice}', 'r') as html_file:
        result_html = html_file.read()

    # Pass the results to the template
    return render_template('result.html', result_text=result_text, result_image1=result_image1, result_image2=result_image2, result_image3=result_image3, result_html=result_html)

if __name__ == '__main__':
    app.run(debug=True)