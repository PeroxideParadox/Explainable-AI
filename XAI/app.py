from flask import Flask
from view import view

app= Flask(__name__)
app.register_blueprint(view,url_prefix='/view')

if __name__=='__main__':
    app.run(debug=True)