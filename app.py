from flask import Flask

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
        
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
