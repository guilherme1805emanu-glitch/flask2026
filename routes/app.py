from flask import Flask,render_template
from flask_wtf import FlaskForm
from routes.auth import authRoutes,RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'qualquer coisa'

app.register_blueprint(authRoutes)

@app.route('/', methods=['GET', 'POST'])
def render_index():
    form = RegisterForm()
    messagem = ''
    if form.validate_on_submit():
        print('Nome:', form.name.data)
        print('Email:', form.email.data)
        print('Assunto:', form.subject.data)
        print('Mensagem:', form.message.data)
        messagem = "Formulário Enviado com sucesso!"
    return render_template('index.html', form=form , messagem = messagem)

# servicos= [
#     {
#         "name": "manutenção",
#         "price": 5000
#     },
#         {
#         "name": "limpeza",
#         "price": 3000
#     },
#     {
#         "name": "lentes",
#         "price": 10000
#     },
# ]

# @app.route('/servicos')
# def render_servicos():
#     return render_template('servicos.html', servicos=servicos)

# app.run(debug=True) 