from flask import Blueprint, jsonify
from models import atividade_model
from flask import request
from config import db
from clients.pessoa_service_client import PessoaServiceClient
from models.atividade_model import ProfessorNaoLecionaTurma

atividade_bp = Blueprint('atividade_bp', __name__)


@atividade_bp.route('/', methods=['GET'])
def listar_atividades():
    atividades = atividade_model.listar_atividades()
    return jsonify(atividades)


@atividade_bp.route('/<int:id_atividade>', methods=['GET'])
def obter_atividade(id_atividade):
    try:
        atividade = atividade_model.obter_atividade(id_atividade)
        return jsonify(atividade)
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404


@atividade_bp.route('/', methods=['POST'])
def criar_atividade():
    data = request.get_json()
    id_turma = data.get('id_turma')
    id_professor = data.get('id_professor')
    enuciado = data.get('enuciado')
    respostas = data.get('respostas')

    if not PessoaServiceClient.verificar_leciona(id_professor, id_turma):
        return jsonify({'erro': 'Professor não leciona a turma'}), 403

    if not all([id_turma, enuciado, respostas]):
        return jsonify({'erro': 'Dados incompletos'}), 400

    try:
        nova_atividade = atividade_model.criar_atividade(
            id_turma, id_professor, enuciado, respostas)
        return jsonify(nova_atividade), 201
    except ProfessorNaoLecionaTurma as e:
        return jsonify({'erro': str(e)}), 403


@atividade_bp.route('/<int:id_atividade>/professor/<int:id_professor>', methods=['GET'])
def obter_atividade_para_professor(id_atividade, id_professor):
    try:
        atividade = atividade_model.obter_atividade(id_atividade)
        if atividade['id_professor'] != id_professor:
            return jsonify({'erro': 'Atividade não pertence ao professor'}), 403
        return jsonify(atividade)
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
