from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

if __name__ =='_main_':
    app.run(debug=True)
    