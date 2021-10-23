from flask import *
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route('/Home')
def home():
    return render_template("Home.html")

@app.route('/Add_Data')
def Add_Data():
    return render_template("Add_Data.html")


@app.route("/save",methods = ["POST","GET"])
def save():
    msg = 'msg'
    
    if request.method == "POST":
        
        try:
            name = request.form["name"]
            Roll_No = request.form["Roll_No"]
            Age = request.form["Age"]
            Mobile_No = request.form["Mobile_No"]
            Email = request.form["Email"]
            with sqlite3.connect("student_detials.db") as connection:
                cursor = connection.cursor()
                cursor.execute("INSERT into Student_Info (name, Roll_No, Age, Mobile_No, Email) values (?,?,?,?,?)",(name, Roll_No, Age, Mobile_No, Email))
                connection.commit()
                msg = "Student detials successfully Added"
        except:
            connection.rollback()
            msg = "We can not add Student detials to the database"            
            
               
        finally:
            return render_template("success_record.html",msg = msg)

@app.route("/student_info")
def student_info():
    connection = sqlite3.connect("student_detials.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("select * from Student_Info")
    rows = cursor.fetchall()
    return render_template("student_info.html",rows = rows)




if __name__ == "__main__":
    app.run(debug=True,port=8000)