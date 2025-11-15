from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    errores = []

    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            for n in (nota1, nota2, nota3):
                if n < 10 or n > 70:
                    errores.append("Cada nota debe estar entre 10 y 70.")
            if asistencia < 0 or asistencia > 100:
                errores.append("La asistencia debe estar entre 0 y 100.")

            if not errores:
                promedio = (nota1 + nota2 + nota3) / 3
                estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"
                resultado = {
                    "promedio": f"{promedio:.2f}",
                    "estado": estado,
                    "asistencia": f"{asistencia:.0f}%"
                }
        except ValueError:
            errores.append("Debes ingresar números válidos en las notas y la asistencia.")

    return render_template('ejercicio1.html', resultado=resultado, errores=errores)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    errores = []

    if request.method == 'POST':
        nombre1 = request.form.get('nombre1', '').strip()
        nombre2 = request.form.get('nombre2', '').strip()
        nombre3 = request.form.get('nombre3', '').strip()

        nombres = [nombre1, nombre2, nombre3]

        if any(n == '' for n in nombres):
            errores.append("Todos los nombres son obligatorios.")
        if len({n.lower() for n in nombres}) < 3:
            errores.append("Los tres nombres deben ser diferentes.")

        if not errores:
            mayor = max(nombres, key=len)
            resultado = {
                "nombre": mayor,
                "cantidad": len(mayor)
            }

    return render_template('ejercicio2.html', resultado=resultado, errores=errores)

@app.route('/home')
def home_redirect():
    return redirect(url_for('index'))

@app.route('/forbidden')
def forbidden():
    abort(403)

if __name__ == '__main__':
    app.run(debug=True)
