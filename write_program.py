from flask import request

class WriteProgram:

    def __init__(self):
        self.a = "Hi"

    def write_program(self, filename):

        program = request.form['program']
        date = request.form['date']

        with open(filename, 'a') as f:
            f.write(str(date + " _ "  + program + "\n"))