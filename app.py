from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_salario_liquido(salario, dependentes):
    inss = salario * 0.08

    if salario > 2500:
        ir = salario * 0.15
    else:
        ir = 0

    valor_dependentes = dependentes * 200

    return salario - inss - ir + valor_dependentes


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/resultado', methods=['POST'])
def resultado():
    try:
        salario = float(request.form['salario'].replace(",", "."))
        dependentes = int(request.form['dependentes'])
        
    except ValueError:
        return f"Erro: Insira valores válidos"
    if salario < 0:
        return f"Erro: o salário não pode ser negativo."
    if dependentes < 0:
        return f"Erro: o número de dependentes não pode ser negativo."
    liquido = calcular_salario_liquido(salario, dependentes)
    return f"Salário líquido: {liquido:.2f}"
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False) 