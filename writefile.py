from flask import request
import datetime

class WriteFile:

    def __init__(self):
        self.a = "Hi"

    def write_file(self, filename):

        institution = request.form['institution']
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        
        tm = datetime.datetime.now()
        time_stamp = tm.strftime("%d/%m/%Y %H:%M:%S")

        with open(filename, 'a') as f:
            f.write(str(institution + " | " + name + " | " + phone  + " | " + email  + " | " + time_stamp + "\n"))