from flask import Flask

app = Flask(__name__)


# Rota dos Alunos da Impacta
@app.route("/alunos")
def alunos():
    return { "alunos":
                    [
                        "Guilherme", 
                        "Lucas",
                        "Matheus", 
                        "Carolina", 
                        "Clara", 
                        "Marcela", 
                        "Daniela"
                    ]
    }

if __name__ == "__main__":
    app.run(debug=True)