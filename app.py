from flask import Flask, render_template, redirect
from readfile import ReadFile
from writefile import WriteFile
from write_program import WriteProgram
import datetime
from flask import request
import os

PEOPLE_FOLDER = os.path.join('static', 'logo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
logo = os.path.join(app.config['UPLOAD_FOLDER'], 'csa_logo.png')

dloads_dir = 'participants_lists'
dloads = os.listdir(dloads_dir)
dloads_src = ['/participants_lists/{}'.format(i) for i in dloads]

# filename = "task.txt"
filename2 = "programs.txt"
is_authenticated = "No"


@app.route('/', methods=['GET'])
def index():
    tasks = ReadFile()
    file_contents = tasks.read_file(filename2)

    x = datetime.datetime.now()
    day = x.strftime("%d")
    month = x.strftime("%m")
    year = x.strftime("%Y")
    date_today = f"{year}-{month}-{day}"

    return render_template('index.html', logo=logo, contents=file_contents, form_type="participants",
                           date_today=date_today)


@app.route('/programs', methods=['GET'])
def programs():
    return render_template('index.html', logo=logo, form_type="key")


@app.route('/add', methods=['GET'])
def add():
    if is_authenticated == "Yes":
        tasks = ReadFile()
        file_contents = tasks.read_file(filename2)
        return render_template('index.html', logo=logo, contents=file_contents, form_type="programs", dloads=dloads,
                               dloads_src=dloads_src)
    else:
        return redirect("/")


@app.route('/submit', methods=['POST'])
def submit():
    program = request.form['program']

    filename = "participants_lists/" + program + ".txt"
    print(program)

    save = WriteFile()
    save.write_file(filename)

    return redirect('/')


@app.route('/add_program', methods=['POST'])
def submit_program():
    save = WriteProgram()
    save.write_program(filename2)

    return redirect('/add')


@app.route('/submit_key', methods=['POST'])
def submit_key():
    tm = datetime.datetime.now()
    time_stamp = tm.strftime("%d/%m/%Y %H:%M")
    our_safoa = f"CSA {time_stamp} programs"
    your_safoa = request.form['your_safoa']

    if your_safoa == our_safoa:
        global is_authenticated
        is_authenticated = "Yes"
        return redirect('/add')
    else:
        return render_template('index.html', logo=logo, message=" - - - - - - - - Wrong Key!", form_type="key")


if __name__ == "__main__":
    app.run(debug=True)