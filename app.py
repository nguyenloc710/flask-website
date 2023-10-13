from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Bengalure, India',
    'salary': 'Rs. 1,00,000'
  },
  {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Bengalure, India',
    'salary': 'Rs. 11,00,000'
  },
  {
    'id': 3,
    'title': 'FontEnd',
    'location': 'Bengalure, India',
    'salary': 'Rs. 12,00,000'
  }
]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='BEST')

@app.route("/api/jobs")
def  list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)