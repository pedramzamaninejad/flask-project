from flask import Flask, request, jsonify
from flask_migrate import Migrate

from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = '363c98df0c8a633364e269e1a91f64307bad1cada77e72624c648bc80be4946f'
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
    new_slug = new_fname + '-' + new_lname
    new_type = request.form['type']
    new_affiliated_by = ''
    new_location = None
    new_address = ''
    new_password = request.form['password'] + app.config['SECRET_KEY']

    try:
        new_user = User(first_name=new_fname, last_name=new_lname, email=new_email, phone=new_phone, \
                        slug=new_slug, affiliated_by=new_affiliated_by, location=new_location, address=new_address,
                        password=new_password, type=new_type)

        db.session.add(new_user)
        db.session.commit()
    except:
        return jsonify({'msg': 'Your form has a problem'}), 400
    return jsonify({'msg': 'created succesfully'}), 201


app.app_context().push()

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
