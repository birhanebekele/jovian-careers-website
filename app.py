from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'data analist',
  'location': 'Addis Ababa',
  'salary': 'br. 120,000'
}, {
  'id': 2,
  'title': 'front end development',
  'location': 'Hawassa',
  'salary': 'br. 130,000'
}, {
  'id': 3,
  'title': 'Database designer',
  'location': 'Addis Ababa',
  'salary': 'br. 100,000'
}, {
  'id': 4,
  'title': 'Network designner',
  'location': 'Arbaminch',
  'salary': 'br. 150,000'
}]


@app.route("/")
def Hello():
  return render_template('home.html', jobs=JOBS, campanyname='BBK')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
