# # O flask vai ser usado pra criar a apliação web
# from flask import Flask, request, jsonify
# # Com essa biblioteca eu posso gerenciar o banco de dados SQLite
# from flask_sqlalchemy import SQLAlchemy


from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# cria instancia da appliacação web
app = Flask(__name__)
# Configuramos o banco de dados que sera usado
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///esportes.db'
# Desativamos o rastreamento de modificações do SQLAlchemy para economizar recursos.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Criamos uma instância do SQLAlchemy com o Flask.
db = SQLAlchemy(app)

class Atividade(db.Model):
   # cria coluna ID, como chave primaria e auto imcrementa
    id = db.Column(db.Integer, primary_key=True)
    # coluna nome, nao pode ser nula
    nome = db.Column(db.String(100), nullable=False)
    # coluna detalhe, nao pode ser nula
    detalhes = db.Column(db.String(200), nullable=False)
    # coluna tipo, nao pode ser nula
    tipo = db.Column(db.String(50), nullable=False)
    # coluna km, nao pode ser nula
    km = db.Column(db.Float, nullable=False)
    # coluna esforço, nao pode ser nula
    esforço = db.Column(db.String(50), nullable=False)
    

# isso cria todas as tabelas no banco de dados, nesse caso só a tabela atividades    
with app.app_context():
    db.create_all()



# Criando os endpoints

# rota para todas as atividades
@app.route('/atividades/<int:id>', methods =['GET'])
def obter_atividades():
    # consulta todas atividades na tabela
    atividades = Atividade.query.all()
    # retorna a lista de atividades no formato json
    return jsonify([{
        'id': atividade.id,
        'nome': atividade.nome,
        'detalhe': atividade.detalhe,
        'tipo': atividade.tipo,
        'km': atividade.km,
        'esforço': atividade.esforço
    } for atividade in atividades])


#rota para atividade por ID

@app.route('/atividades/<int:id>', methods = ['GET'])
def obter_atividade(id):
    #consulta tividade por id
    atividade  = Atividade.query.get(id)
     # Se a atividade não for encontrada, retornamos um erro 404.
    if atividade is None:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    

    # Atualizamos os campos da atividade com os novos dados fornecidos.
    atividade.nome = dados['nome']
    atividade.detalhe = dados['detalhe']
    atividade.tipo = dados['tipo']
    atividade.quilometragem = dados['quilometragem']
    atividade.esforço = dados['esforço']
    # Cometemos a transação para salvar as mudanças no banco de dados.
    db.session.commit()
    # Retornamos uma mensagem de sucesso no formato JSON.
    return jsonify({'mensagem': 'Atividade atualizada com sucesso'})


# Definimos a rota para deletar uma atividade pelo seu ID.
@app.route('/atividades/<int:id>', methods=['DELETE'])
def deletar_atividade(id):
    # Consultamos a atividade pelo ID.
    atividade = Atividade.query.get(id)
    # Se a atividade não for encontrada, retornamos um erro 404.
    if atividade is None:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

    # Removemos a atividade da sessão do banco de dados.
    db.session.delete(atividade)
    # Cometemos a transação para deletar a atividade do banco de dados.
    db.session.commit()
    # Retornamos uma mensagem de sucesso no formato JSON.
    return jsonify({'mensagem': 'Atividade deletada com sucesso'})

# Inicializamos o servidor Flask para rodar a aplicação.
if __name__ == '__main__':
# Colocamos o servidor em modo debug para facilitar o desenvolvimento.
  app.run(debug=True)




