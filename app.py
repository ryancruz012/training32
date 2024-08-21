from flask import Flask, render_template, request

# Create an instance of the Flask class for the web application
app = Flask(__name__)

# Define the main route for the application, which handles both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize a variable to store the processed age value, default is None
    result_age = None
    
    if request.method == 'POST':
        try:
            # Retrieve the age input from the form and convert it to an integer
            age = int(request.form['age'])
            # Calculation: According to the formula (Man's Age / 2) + 7
            result_age = age / 2 + 7
        except ValueError:
            # If the input is not a valid integer, set result_age to None
            result_age = None
            
    # Render the index.html template and pass the processed age to it
    return render_template("index.html", age=result_age)

# Run the Flask application in debug mode when the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
