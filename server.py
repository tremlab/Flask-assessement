from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


positions = ["Software Engineer",
            "QA Engineer",
            "Product Manager",
            "Monkey Trainer"
            ]

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def welcome_applicants():
    """Homepage - welcome users to Ubermelon application.
    """
    return render_template("index.html", positions=positions)


@app.route("/application-form")
def receive_application():
    """display application form and receive applicants input.
    """

    return render_template("application-form.html", positions=positions)


@app.route("/application-success", methods=["POST"])
def confirm_application():
    """confirm application receipt to the applicant.
    """

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    position = request.form.get("positionapp")
    salary = float(request.form.get("salaryreq"))
    salary = "${:,.2f}".format(salary)

    return render_template("application-response.html",
                            firstname=firstname,
                            lastname=lastname,
                            position=position,
                            salary=salary,
                            )


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
