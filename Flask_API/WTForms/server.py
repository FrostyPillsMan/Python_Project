from flask import Flask, render_template, request
from wtforms import Form, StringField, validators

# create a server instance
app = Flask(__name__)

class UserRegistrationForm(Form):
    uName = StringField("Name", validators=[validators.InputRequired(), validators.Length(min=4,max=150)])
    uEmail = StringField("Email Address", [validators.Length(min=6, max=35)])

# route handler
@app.route("/", methods=['GET', 'POST'])
def index():
    form = UserRegistrationForm(request.form)
    if request.method == "POST":
        print(form.uName.data)
        print(form.uEmail.data)
    return render_template("index.html.j2", form=form)


if __name__ == "__main__":
    app.run(debug=True)

