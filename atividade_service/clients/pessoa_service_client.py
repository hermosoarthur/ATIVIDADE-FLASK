import requests

PESSOA_SERVICE_URL = "http://localhost:5000/projeto-api-flask/"


class PessoaServiceClient:

    @staticmethod
    def verificar_leciona(id_professor, id_turma):
        try:
            response = requests.get(
                f"{PESSOA_SERVICE_URL}professores/{id_professor}/turma/{id_turma}")
            response.raise_for_status()
            json_data = response.json()
            if isinstance(json_data, dict):
                return json_data.get('leciona', False)
            elif isinstance(json_data, bool):
                return json_data
            else:
                return False
        except requests.RequestException as e:
            print(f"Erro ao verificar leciona: {e}")
            return False
