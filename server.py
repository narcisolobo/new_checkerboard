from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
  params = {
    'color0': 'red',
    'color1': 'black',
    'rows': 8,
    'columns': 8
  }
  return render_template('index.html', params = params)

@app.route('/<x>')
def rows(x):
  params = {
    'color0': 'red',
    'color1': 'black',
    'rows': int(x),
    'columns': 8
  }
  return render_template('index.html', params = params)

@app.route('/<x>/<y>')
def rows_and_columns(x, y):
  params = {
    'color0': 'red',
    'color1': 'black',
    'rows': int(x),
    'columns': int(y)
  }
  return render_template('index.html', params = params)

@app.route('/<x>/<y>/<color0>/<color1>')
def colors(x, y, color0, color1):
  params = {
    'color0': color0,
    'color1': color1,
    'rows': int(x),
    'columns': int(y)
  }
  return render_template('index.html', params = params)

if __name__ == '__main__':
  app.run(debug=True)