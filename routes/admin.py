from flask import Blueprint, render_template
from definitions.produto import ProductForm,Product
from connection import db


adminRoutes = Blueprint('admin', __name__)

@adminRoutes.route('/produtos', methods=["GET", "POST"])
def produtos():
    form = ProductForm()
    message = ''
    if form.validate_on_submit():
        new_product = Product(
            nome=form.nome.data,
            descricao=form.descricao.data,
            preco=form.preco.data,
            quantidade=form.quantidade.data
        )
        db.session.add(new_product)
        db.session.commit()
        message = 'Produto adicionado com sucesso!'
    products = Product.query.all()
    return render_template('admin/produtos.html', form=form, products=products, message=message)
