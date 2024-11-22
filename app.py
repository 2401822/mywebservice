from flask import Flask, Blueprint, request, jsonify, render_template, redirect, url_for, flash

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
@app.route('/activity/config', methods=['GET'])
def activity_config_page():
    """
    Retorna a página de configuração da atividade.
    """
    try:
        #return render_template('activity_config.html')  # Criar este template
        params = {

                "id": 1,
                "nome": "Introducao ao print()",
                "descricao": "Explicar o comando basico print().",
                "modulo_id": 1,
                "tipo_atividade": "quiz",
                "configuracao_json": {
                    "dificuldade": "basico",
                    "tempo_estimado": "15 minutos",
                    "numero_de_perguntas": 10,
                    "tipo_de_resposta": "multipla escolha"
                },
                "criado_em": "2024-11-20 10:00:00",
                "atualizado_em": "2024-11-20 12:00:00"

        }
        return jsonify(params)
    except Exception as e:
        flash(f'Erro ao carregar página de configuração: {str(e)}', 'error')
        return jsonify({"error": str(e)}), 500

@app.route('/activity/config/params', methods=['GET'])
def activity_config_params():
    """
    Retorna os parâmetros configurados no formato JSON.
    """
    try:
        # Exemplo de estrutura de parâmetros configurados
        params = {
              "id": 1,
              "atividade_id": 1,
              "chave_configuracao": "tempo_limite",
              "valor_configuracao": "30 minutos",
              "criado_em": "2024-01-20 10:00:00"
                }

        return jsonify(params)
    except Exception as e:
        flash(f'Erro ao carregar parâmetros: {str(e)}', 'error')
        return jsonify({"error": str(e)}), 500

@app.route('/analytics/list', methods=['GET'])
def analytics_list():
    """
    Retorna a lista de análises cadastradas, incluindo todos os campos disponíveis.
    """
    try:
        # Obtém todas as análises da tabela
        # analises = Analise.query.all()
        analises_list = [
            {
                "id":1,
                "atividade_id": 1,
                "atividade_nome": "Introducao ao print()",
                "utilizador_id": 1,
                "utilizador_nome": "Alexandre Nascimento",
                "dados": {"s1": "value1", "s2": "value2"},
                "criado_em": "2024-11-20 10:12:42"
            }
            #for analise in analises
        ]
        return jsonify(analises_list)
    except Exception as e:
        flash(f'Erro ao carregar dados de análises: {str(e)}', 'error')
        return jsonify({"error": str(e)}), 500


@app.route('/activity/deploy', methods=['GET'])
def activity_deploy():
    """
    Processa o deploy de uma atividade.
    """
    try:
        return jsonify({
            "response": "Nova atividade registada!",
            "redirect_url": f"{request.host_url}activity/6"
        })
    except Exception as e:
        # Em caso de erro, faz rollback da transação e retorna o erro
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    """    
    try:
        # Recebe os dados enviados no POST
        data = request.get_json()
        json_params = data.get("json_params", {})

        # Validação dos campos obrigatórios
        if not json_params.get("nome"):
            return jsonify({"error": "O campo 'nome' é obrigatório."}), 400
        if not json_params.get("modulo_id"):
            return jsonify({"error": "O campo 'modulo_id' é obrigatório."}), 400
        if not json_params.get("tipo_atividade"):
            return jsonify({"error": "O campo 'tipo_atividade' é obrigatório."}), 400

        # Verificar se o módulo existe
        modulo = Modulo.query.get(json_params.get("modulo_id"))
        if not modulo:
            return jsonify({"error": "O módulo especificado não existe."}), 400

        # Criação da nova atividade com os parâmetros recebidos
        nova_atividade = Atividade(
            nome=json_params.get("nome"),
            descricao=json_params.get("descricao", "Descrição padrão para deploy"),
            modulo_id=json_params.get("modulo_id"),
            tipo_atividade=json_params.get("tipo_atividade"),
            configuracao_json=json_params.get("configuracao_json", {})
        )

        # Grava a nova atividade no banco de dados
        db.session.add(nova_atividade)
        db.session.commit()

        # Retorna a URL de redirecionamento para o aluno
        return jsonify({
            "redirect_url": f"{request.host_url}activity/{nova_atividade.id}"
        })
    except Exception as e:
        # Em caso de erro, faz rollback da transação e retorna o erro
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        # Fecha a sessão para liberar recursos
        db.session.close()
"""

@app.route('/analytics/request', methods=['GET'])
def ananlytics_request():
    """
    Retorna os parâmetros configurados no formato JSON.
    """
    try:
        # Exemplo de estrutura de parâmetros configurados
        params = [
  {
    "id": 1,
    "atividade_id": 1,
    "chave_configuracao": "tempo_limite",
    "valor_configuracao": "30 minutos",
    "criado_em": "2024-11-20 10:10:00"
  },
  {
    "id": 2,
    "atividade_id": 1,
    "chave_configuracao": "dificuldade",
    "valor_configuracao": "intermediario",
    "criado_em": "2024-11-20 10:10:00"
  },
  {
    "id": 3,
    "atividade_id": 1,
    "chave_configuracao": "tipo_de_resposta",
    "valor_configuracao": "multipla escolha",
    "criado_em": "2024-11-20 10:10:00"
  }
]


        return jsonify(params)
    except Exception as e:
        flash(f'Erro ao carregar parâmetros: {str(e)}', 'error')
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
