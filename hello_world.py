from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return render_template('hello.html')
    

# @app.route("/jedi/<first_name>/<last_name>")
# def hello_jedi(first_name,last_name):
#     fullName = first_name + " " + last_name
#     jediName = ""
#     jediName = last_name[0:3] + first_name[0:2]
#     html = """
#         <h1>
#             Hello {}!
#         </h1>
#         <p>
#             Your jedi name is {}.
#         </p>
#    """
#     return html.format(fullName,jediName)
@app.route("/hello/<name>")
def hello_person(name):
    return render_template('hello_name.html',name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)