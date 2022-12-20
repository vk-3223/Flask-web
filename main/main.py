from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from backend import Database 
from mail import send_email
from sqlalchemy.sql import func
app = Flask(__name__)

db = Database("info.db")

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/success.html',methods=['POST'])
def success():
    count = 0
    sum_ = 0
    if request.method=="POST":
        email = request.form["email_name"]
        height = request.form["height_name"]
        
        db.insert(email=email,height=height)
        avrage_height = (db.search(email,height))
        for i in avrage_height:
            avr = (i[2])
            count = count+1
            sum_= sum_+avr
            avrage_sum = sum_/count
        print(avrage_sum)
        send_email(email,height,avrage_sum)


        return render_template('success.html')
if __name__==("__main__"):
    app.run(debug=1)    
    