from app import app
from flask import render_template

'''
Page rendering
'''

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/sign-up', methods=['GET'])
def signUp():
  return render_template('index.html')

@app.route('/calendar', methods=['GET'])
def calendar():
  return render_template('index.html')

@app.route('/reviews', methods=['GET'])
def reviews():
  return render_template('index.html')

'''
Landing page
'''



'''
Sign up page
'''



'''
Recommendation page
'''



'''
Testing endpoint
'''

@app.route('/test', methods=['GET'])
def test():
  return 'it works!'

'''
Page Not Found
'''

# @app.errorhandler(404)
# def pageNotFound(e):
#   return render_template('index.html')