from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/db_sqlalchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Example(db.Model):
	__tablename__ = 'tb_example'
	id = db.Column('id', db.Integer, primary_key=True)
	data = db.Column('data', db.Unicode)

	def __init__(self, id, data):
		self.id = id
		self.data = data
# if __name__ == '__main__':
# 	app.run(debug=True, port=8080)