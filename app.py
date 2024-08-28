from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'data analyst',
        'location':'Bengaluru, India',
        'salary':'Rs. 10,00,000'
    },
    {
        'id':2,
        'title':'data scientist',
        'location':'san fransisco, USA',
        'salary':'$120,000'
    },
    {
        'id':3,
        'title':'backend engineer',
        'location':'remote',
        'salary':'Rs. 10,00,000'
    },
    {
        'id':4,
        'title':'frontend engineer',
        'location':'Pune, India',
        'salary':'Rs. 10,00,000'
    },    

]

@app.route('/')
def hello():
    return render_template('home.html', jobs=JOBS)

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)