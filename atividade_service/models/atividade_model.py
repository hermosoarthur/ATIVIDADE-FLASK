from config import db
from clients.pessoa_service_client import PessoaServiceClient


class AtividadeNotFound(Exception):
    pass


class ProfessorNaoLecionaTurma(Exception):
    pass


class Atividade(db.Model):
    __tablename__ = 'atividade'
    id = db.Column(db.Integer, primary_key=True)
    id_turma = db.Column(db.Integer, nullable=False)
    id_professor = db.Column(db.Integer, nullable=False)
    enuciado = db.Column(db.String(255), nullable=False)
    respostas = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'id_turma': self.id_turma,
            'id_professor': self.id_professor,
            'enuciado': self.enuciado,
            'respostas': self.respostas
        }


def listar_atividades():
    atividades = Atividade.query.all()
    return [atividade.to_dict() for atividade in atividades]


def obter_atividade(id_atividade):
    atividade = Atividade.query.get(id_atividade)
    if not atividade:
        raise AtividadeNotFound(
            f"Atividade com id {id_atividade} não encontrada.")
    return atividade.to_dict()


def criar_atividade(id_turma, id_professor, enuciado, respostas):

    nova_atividade = Atividade(
        id_turma=id_turma,
        id_professor=id_professor,
        enuciado=enuciado,
        respostas=respostas
    )
    db.session.add(nova_atividade)
    db.session.commit()
    return nova_atividade.to_dict()
