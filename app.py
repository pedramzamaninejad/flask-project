from flask import Flask, request, jsonify, template_rendered
from flask_migrate import Migrate

from config import Config
from Users.models import db, User, Laboratory, LabBranch, UserAddress

app = Flask(__name__)
app.config.from_object(Config)

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
    new_user_type = request.form.get('user_type', None)
    new_affiliated_by = request.form.get('affiliated_by', None)
    new_weight = request.form.get('weight', None)
    new_password = request.form['password'] + app.config['SECRET_KEY']

    # try:
    new_user = User(first_name=new_fname, last_name=new_lname, email=new_email, phone=new_phone, \
                    slug=new_slug, affiliated_by=new_affiliated_by, password=new_password, user_type=new_user_type, \
                    weight=new_weight)

    db.session.add(new_user)
    user = User.query.first()
    db.session.commit()
    # except:
    #     return jsonify({'msg': 'Your form has a problem'}), 400
    return jsonify({'msg': 'created succesfully', "id": f"{user.id}"}), 201


@app.route('/create', methods=['POST', 'GET'])
def create_lab():
    if request.method == 'POST':
        from datetime import date
        new_name = request.form['name']
        new_employee = request.form.get('employee', None)
        new_year = request.form['year_founded']
        year, month, day = map(int, new_year.split('-'))
        date_obj = date(year, month, day)

        try:
            new_lab = Laboratory(name=new_name, employee=new_employee, year_founded=date_obj)
            db.session.add(new_lab)
            db.session.commit()
        except:
            return jsonify({'msg': 'form has a problem'}), 400
        return jsonify({'msg': 'created succesfully'}), 201
    elif request.method == 'GET':
        labs = Laboratory.query.get('9161545b-bc93-4e08-b86f-96422b559213')
        branch_list = [(branch.id, branch.branch_name) for branch in labs.branches]
        print(branch_list)

        return jsonify({"msg": "check console"})


@app.route('/create/<string:lab_id>', methods=['POST'])
def create_branch(lab_id):
    new_branch_name = request.form['branch_name']

    try:
        new_branch = LabBranch(branch_name=new_branch_name, laboratory_id=lab_id)
        db.session.add(new_branch)
        db.session.commit()
    except:
        return jsonify({'msg': 'It didnt worked'}), 400
    return jsonify({'msg': 'it worked'}), 201


@app.route('/user/address/<string:id>', methods=['POST', 'GET'])
def addres(id):
    if request.method == 'POST':
        new_user_id = id
        new_address = request.form.get('address', None)

        new_user_address = UserAddress(user_id=new_user_id, address=new_address)
        db.session.add(new_user_address)
        db.session.commit()
        return jsonify({'msg': 'It worked'})
    elif request.method == 'GET':
        return jsonify({'msg': 'not developed yet'})


app.app_context().push()

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
