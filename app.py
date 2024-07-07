from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Cria a instância da aplicação Flask
app = Flask(__name__)

# # Define o caminho do banco de dados na pasta 'desafio_api'
# base_dir = os.path.abspath(os.path.dirname(__file__))
# db_path = os.path.join(base_dir, 'Desafio API', 'esportes.db')


# Define o caminho do banco de dados na pasta 'desafio_api'
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'esportes.db')

# Configura o banco de dados que vou usar
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

# Exemplo de configuração adicional
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Cria a instância do SQLAlchemy com o Flask
db = SQLAlchemy(app)

# Define o modelo da tabela 'Atividade'
class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    detalhes = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    km = db.Column(db.Float, nullable=False)
    esforço = db.Column(db.String(50), nullable=False)

# Cria todas as tabelas no banco de dados, nesse caso só a tabela 'Atividade'
with app.app_context():
    db.create_all()

# Rota para listar todas as atividades
@app.route('/atividades', methods=['GET'])
def obter_atividades():
    atividades = Atividade.query.all()
    return jsonify([{
        'id': atividade.id,
        'nome': atividade.nome,
        'detalhes': atividade.detalhes,
        'tipo': atividade.tipo,
        'km': atividade.km,
        'esforço': atividade.esforço
    } for atividade in atividades])

# Rota para obter uma atividade por ID
@app.route('/atividades/<int:id>', methods=['GET'])
def obter_atividade(id):
    atividade = Atividade.query.get(id)
    if atividade is None:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    return jsonify({
        'id': atividade.id,
        'nome': atividade.nome,
        'detalhes': atividade.detalhes,
        'tipo': atividade.tipo,
        'km': atividade.km,
        'esforço': atividade.esforço
    })

# Rota para criar uma nova atividade
@app.route('/atividades', methods=['POST'])
def criar_atividade():
    dados = request.get_json()
    nova_atividade = Atividade(
        nome=dados['nome'],
        detalhes=dados['detalhes'],
        tipo=dados['tipo'],
        km=dados['km'],
        esforço=dados['esforço']
    )
    db.session.add(nova_atividade)
    db.session.commit()
    return jsonify({'mensagem': 'Atividade criada com sucesso'}), 201

# Rota para deletar uma atividade
@app.route('/atividades/<int:id>', methods=['DELETE'])
def deletar_atividade(id):
    atividade = Atividade.query.get(id)
    if atividade is None:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    db.session.delete(atividade)
    db.session.commit()
    return jsonify({'mensagem': 'Atividade deletada com sucesso'})

# Inicializa o servidor Flask
if __name__ == '__main__':
    # Imprimir o caminho absoluto do banco de dados
    print(f"Banco de dados localizado em: {db_path}")
    app.run(debug=True)