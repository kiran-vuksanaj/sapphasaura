# i miss my girlfrienddd


from flask import Flask, render_template
app = Flask(__name__) # constructor of the flask app

@app.route("/") #route for the function directly below, this is the root route
def home():
    return render_template("base.html")


if __name__ == "__main__": 
    app.debug = True 
    app.run() 
