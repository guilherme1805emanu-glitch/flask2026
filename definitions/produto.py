from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from connection import db

class ProductForm(FlaskForm):
    name = StringField('Nome do Produto', validators=[
        DataRequired(message="O nome do produto é obrigatório"),
        Length(min=2, max=100, message="O nome do produto deve ter entre 2 e 100 caracteres")
    ])
    price = StringField('Preço', validators=[
        DataRequired(message="O preço é obrigatório")
    ])
    description = StringField('Descrição', validators=[
        Length(max=500, message="A descrição não pode exceder 500 caracteres")
    ])

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=True)

    