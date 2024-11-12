from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")


@app.post("/portfolio.html")
def portfolio():
        #Get form data
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        fav_language = request.form.get("fav_language")

        return render_template("portfolio.html" , fname=fname , lname=lname , fav_language=fav_language)




if __name__ == "__main__":
    app.run(port=8080 , debug =True)