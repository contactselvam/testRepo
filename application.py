from flask import Flask

# Create Flask application instance
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, World!</h1><p>Welcome to my Flask application!</p>'

@app.route('/about')
def about():
    return '<h1>About Page</h1><p>This is a simple Flask application.</p>'

# For AWS Elastic Beanstalk, use 'application' instead of 'app'
application = app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
