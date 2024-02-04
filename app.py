from flask import Flask, request, jsonify
from flask_migrate import Migrate

from config import Config
from Users.models import db, User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)
migrate.init_app(app, db)


@app.route("/", methods=['POST', 'GET'])
def home():
    print(app.config['SECRET_KEY'])
    new_fname = request.form['first_name']
    new_lname = request.form['last_name']
    new_email = request.form['email']
    new_phone = request.form['phone']
    new_slug = new_fname + '-' + new_lname
    new_user_type = request.form.get('user_type', None)
    new_affiliated_by = request.form.get('affiliated_by', None)
    new_location = request.form.get('location', None)
    new_address = request.form.get('address', None)
    new_weight = request.form.get('weight', None)
    new_password = request.form['password'] + app.config['SECRET_KEY']

    # try:
    new_user = User(first_name=new_fname, last_name=new_lname, email=new_email, phone=new_phone, \
                    slug=new_slug, affiliated_by=new_affiliated_by, location=new_location, address=new_address,
                    password=new_password, user_type=new_user_type, weight=new_weight)

    db.session.add(new_user)
    db.session.commit()
    # except:
    #     return jsonify({'msg': 'Your form has a problem'}), 400
    return jsonify({'msg': 'created succesfully'}), 201


app.app_context().push()

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
