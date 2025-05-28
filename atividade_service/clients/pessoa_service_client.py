import requests

PESSOA_SERVICE_URL = "http://api-flask:5000/projeto-api-flask/"


class PessoaServiceClient:

    @staticmethod
    def verificar_leciona(id_professor, id_turma):
        url = f"{PESSOA_SERVICE_URL}professores/{id_professor}/turma/{id_turma}"
        try:
            response = requests.get(url, timeout=5)
            print(f"[PessoaServiceClient] Request URL: {url}")
            print(f"[PessoaServiceClient] Status Code: {response.status_code}")
            print(f"[PessoaServiceClient] Response Text: {response.text}")

            response.raise_for_status()

            try:
                json_data = response.json()
                print(f"[PessoaServiceClient] JSON: {json_data}")
                return bool(json_data)
            except ValueError:
                print("[PessoaServiceClient] Erro ao decodificar JSON da resposta.")
                return False
        except requests.RequestException as e:
            print(f"[PessoaServiceClient] Erro na requisição: {e}")
            return False
