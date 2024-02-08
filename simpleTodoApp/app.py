from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = ["Study Flask", "Drink Tea", "Play Something"] #stores our tasks


@app.route('/')
def index():
	return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def create():
	task = request.form['task']
	tasks.append(task)
	return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
	if id >= 0 and id < len(tasks):
		del tasks[id]
	return redirect(url_for('index'))

if __name__=='__main__':
	app.run(debug=True)

