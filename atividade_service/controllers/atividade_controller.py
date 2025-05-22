from flask import Blueprint, jsonify
from models import atividade_model
from flask import request
from config import db
from clients.pessoa_service_client import PessoaServiceClient

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
    enuciado = data.get('enuciado')
    respostas = data.get('respostas')

    if not all([id_turma, enuciado, respostas]):
        return jsonify({'erro': 'Dados incompletos'}), 400

    nova_atividade = atividade_model.criar_atividade(
        id_turma, enuciado, respostas)
    return jsonify(nova_atividade), 201


@atividade_bp.route('/<int:id_atividade>/professor/<int:id_professor>', methods=['GET'])
def obter_atividade_para_professor(id_atividade, id_professor):
    try:
        atividade = atividade_model.obter_atividade(id_atividade)
    except atividade_model.AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

    # Verifica se o professor leciona a turma da atividade
    if not PessoaServiceClient.verificar_leciona(id_professor, atividade['id_turma']):
        return jsonify({'erro': 'Professor não leciona a turma da atividade'}), 403
    return jsonify(atividade)
