from flask import Flask , render_template
from flask import Flask

app=Flask(__name__)
@app.route("/")
def Homepage():
    return render_template("homepage.html",title="Home Page")

if __name__=="__main__":
    app.run(debug=True)