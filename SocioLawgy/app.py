from flask import Flask, render_template, request, redirect, url_for
from config import DevelopmentConfig
from backend.models import db, Lawyer, Client, Case
from backend.resources import api
import requests

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api.init_app(app)
db.init_app(app)
app.app_context().push()

with app.app_context():
    db.create_all()

    if Lawyer.query.filter_by(name='default').count() == 0:
        default_lawyer = Lawyer(name='default', email='default', password='default', speciality='default', experience=0, personal_website='default', verified=True)

        db.session.add(default_lawyer)
        db.session.commit()

@app.get('/')
def home():
    return render_template('login.html')

@app.route('/signupLawyer', methods=['GET', 'POST'])
def signupLawyer():
    if request.method == 'GET':
        return render_template('signupLawyer.html')
    else:
        name = request.form['name']
        speciality = request.form['speciality']
        experience = request.form['experience']
        personal_website = request.form['personal_website']
        email = request.form['email']
        password = request.form['password']
        lawyer = Lawyer(name=name, email=email, password=password, speciality=speciality, experience=experience, personal_website=personal_website, verified=False)
        db.session.add(lawyer)
        db.session.commit()
        return redirect(url_for('loginLawyer'))

@app.route('/signupClient', methods=['GET', 'POST'])
def signupClient():
    if request.method == 'GET':
        return render_template('signupClient.html')
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        client = Client(name=name, email=email, password=password)
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('loginClient'))


@app.route('/loginLawyer', methods=['GET', 'POST'])
def loginLawyer():
    if request.method == 'GET':
        return render_template('login_lawyer.html')
    else:
        lawyer = Lawyer.query.filter_by(email=request.form['email'], password=request.form['password']).first()
        if lawyer is None:
            return render_template('login_lawyer.html')
        else:
            return redirect('/lawyer_dashboard/{}'.format(lawyer.id))

@app.route('/loginClient', methods=['GET', 'POST'])
def loginClient():
    if request.method == 'GET':
        return render_template('login_client.html')
    else:
        client = Client.query.filter_by(email=request.form['email'], password=request.form['password']).first()
        if client is None:
            print('Here\n' * 20)
            return render_template('login_client.html')
        else:
            print('Here\n' * 20)
            return redirect('/client_dashboard/{}'.format(client.id))

@app.get('/client_dashboard/<int:id>')   
def clientDashboard(id):
    client = Client.query.filter_by(id=id).first()
    lawyers = Lawyer.query.all()
    print(client)
    return render_template('client_dashboard.html', client=client, lawyers=lawyers)

@app.get('/lawyer_dashboard/<int:id>')   
def lawyerDashboard(id):
    lawyer = Lawyer.query.filter_by(id=id).first()
    clients =  Client.query.all()
    return render_template('lawyer_dashboard.html', lawyer=lawyer, clients=clients)

@app.get('/registerCase/<int:id>')
def register_case(id):
    client = Client.query.filter_by(id=id).first()
    return render_template('caseDetails.html', client=client)

@app.post('/registerCase/<int:id>')
def add_case(id):
    name = request.form['name']
    case_type = request.form['case_type']
    description = request.form['case_description']
    summary = request.form['case_summary']
    client_id = id
    lawyer_id = 1
    case = Case(name=name, case_type=case_type, description=description, summary=summary, client_id=client_id, lawyer_id=lawyer_id)
    db.session.add(case)
    db.session.commit()
    return redirect(f'/client_dashboard/{id}')

@app.get('/help')
def help():
    return render_template('caseType.html')

if __name__ == "__main__":
    app.run(debug=True)