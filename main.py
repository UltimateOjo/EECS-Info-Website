from flask import Flask, render_template,request
from twilio.rest import Client

account_sid = 'INSERT YOUR ACCOUNT SID'
auth_token = 'INSERT YOUR AUTHTOKEN'
client = Client(account_sid, auth_token)
app = Flask(__name__)

def masstext(m_message):

    with open("contact.txt", "r") as contactfile:

        for line in contactfile:

            message = client.messages.create(
                messaging_service_sid='CREATE YOUR OWN SERVICE AND INSERT YOUR SERVICE ID',
                body=m_message,
                to=line
            )

            print(message.sid)

    contactfile.close()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result",methods = ['POST','GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]
    return render_template("index2.html", name = name)

@app.route("/quiz",methods = ['POST','GET'])
def quiz():
    return render_template("quiz.html")

@app.route("/softquestion",methods = ['POST','GET'])
def softquestion():
    return render_template("softquestion1.html")
@app.route("/hardquestion1",methods = ['POST','GET'])
def hardquestion1():
    return render_template("hardquestion1.html")

@app.route("/hardquestion2",methods = ['POST','GET'])
def hardquestion2():
    return render_template("hardquestion2.html")

@app.route("/ee",methods = ['POST','GET'])
def ee():
    return render_template("ee.html")

@app.route("/cs",methods = ['POST','GET'])
def cs():
    return render_template("cs.html")

@app.route("/ce",methods = ['POST','GET'])
def ce():
    return render_template("ce.html")

@app.route("/ic",methods = ['POST','GET'])
def ic():
    return render_template("ic.html")

@app.route("/thanks",methods = ['POST','GET'])
def numbers():
    output = request.form.to_dict()
    number = output["number"]
    if len(number) == 10:

        number = '+1' + number

        with open("contact.txt", "a+") as contactfile:
            contactfile.seek(0)

            data = contactfile.read(100)

            if len(data) > 0:

                contactfile.write("\n")


            contactfile.write(number)

        contactfile.close()

        message = client.messages.create(
            messaging_service_sid='CREATE YOUR OWN SERVICE AND INSERT YOUR SERVICE ID',
            body='Click The Following Links For More Information on Majors:\nElectrical Engineering: https://eecs.ku.edu/prospective-students/undergraduate/degree-requirements#electrical_engineering \nComputer Science: https://eecs.ku.edu/prospective-students/undergraduate/degree-requirements#computer_science \nComputer Engineering: https://eecs.ku.edu/prospective-students/undergraduate/degree-requirements#computer_engineering \nInterdisciplinary Computing: https://eecs.drupal.ku.edu/prospective-students/undergraduate/degree-requirements#interdisciplinary_computing',
            to= number
        )

        print(message.sid)
    return render_template("thanks.html")

if __name__ == "__main__":
    app.run(debug= True,host="127.0.0.1", port=8080)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
