from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def main():
  return render_template('home.html')

@app.route('/about')
def res():
  return render_template('about.html')

@app.route('/data')
def com():
  return render_template('data.html')

@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry, page not found', 404




if __name__ == '__main__':
  app.run()#port=33507)
