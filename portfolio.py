from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('mountain.html')

@app.route('/<string:page_name>')
def project(page_name):
    return render_template(page_name)

@app.route('/send_contact_details', methods=['POST'])
def send_contact_details():
    if request.method == 'POST':
        data = request.form.to_dict()  # -> this will turn user responses in a dict
        storing_data(data)
        storing_data1(data)
        # Now we can redirect user to new HTML page which will say thanks after submitting details. Using 'redirect'.
        return redirect('/thanks.html')
    else:
        return 'Try again'

def storing_data(data):  # This fun is linked to above fun via line 16.
    with open('database.txt', mode='a') as data_file:
        email_add = data['email']
        txt = data['text']
        msg = data['message']
        file = data_file.write(f'\n {email_add}, {txt}, {msg}')

# Like above fun: we can write this user data in a CSV file, but for that we have to import csv lib and also the fun
# will be little different, than above on.

def storing_data1(data):  # This fun is linked to above fun via line 16.
    with open('database.csv', mode='a', newline='') as csv_file:
        email_add = data['email']
        txt = data['text']
        msg = data['message']
        # Now we will create a variable to write to CSV file.
        writing_to_csv = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # In the above variable 'writing_to_csv' we used '.writer' method from 'csv' lib to write in our 'csv_file'.
        # by gibing it our fie name i.e. 'csv_file', a delimiter as ',' delimiter actually tells csv writer where one
        # column ends. Usually, after the comma. Also set a quote character. Last things will remain same.
        # newline is for to add new line everytime a new user gives us input.
        writing_to_csv.writerow([email_add, txt, msg])
        # In above line we used variable 'writing_to_csv' which has been set as a csv writer, to write a row having
        # 3 columns as "email_add,txt,msg" as list.