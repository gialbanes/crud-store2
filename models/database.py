from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Classe responsável por criar a entidade "Estudante" com os atributos: id, nome e idade. 
class Produto(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    imagem = db.Column(db.String(50))
    nome = db.Column(db.String(150))
    descricao = db.Column(db.String[500])
    valor = db.Column(db.Float)

    def __init__(self, imagem, nome, descricao, valor):
        self.imagem = imagem
        self.nome = nome
        self.descricao = descricao
        self.valor = valor