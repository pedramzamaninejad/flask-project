from flask import Flask, template_rendered, request, jsonify
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/pzama/Desktop/flask-starter/flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False

db.init_app(app)

migrate = Migrate(app, db)
migrate.init_app(app, db)


@app.route("/", methods=['POST', 'GET'])
def home():
    new_fname = request.form['first_name']
    new_lname = request.form['last_name']
    new_email = request.form['email']
    new_phone = request.form['phone']
    new_slug = new_fname + new_lname

    new_user = User(first_name=new_fname, last_name=new_lname, email=new_email, phone=new_phone, \
                    slug=new_slug)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'msg': 'created succesfully'})

app.app_context().push()

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)