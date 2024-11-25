from flask import Flask, render_template, request

app = Flask(__name__)

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Página del Ejercicio 1: Calcular Descuento
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    error = None
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            edad = int(request.form['edad'])
            cantidad = int(request.form['cantidad'])
            precio_por_tarro = 9000

            if edad < 0 or cantidad < 0:
                error = " edad y la cantidad no pueden ser negativos."
            else:
                # Calcular el total sin descuento
                total_sin_descuento = cantidad * precio_por_tarro

                # Calcular descuento
                if edad >= 18 and edad <= 30:
                    descuento = 0.15  # 15%
                elif edad > 30:
                    descuento = 0.25  # 25%
                else:
                    descuento = 0.0  # Sin descuento para menores de 18

                total_con_descuento = total_sin_descuento * (1 - descuento)
                resultado = {
                    "nombre": nombre,
                    "total_sin_descuento": total_sin_descuento,
                    "total_con_descuento": total_con_descuento
                }
        except ValueError:
            error = " ingrese valores numéricos válidos."
    return render_template('ejercicio1.html',
                           resultado=resultado,
                           error=error,
                           nombre=resultado['nombre'] if resultado else None,
                           total_sin_descuento=resultado['total_sin_descuento'] if resultado else None,
                           total_con_descuento=resultado['total_con_descuento'] if resultado else None)

# Página del Ejercicio 2: Inicio de Sesión
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        usuarios = {
            'juan': 'admin',
            'pepe': 'user'
        }

        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == 'juan':
                mensaje = f"Bienvenido administrador {usuario}"
            else:
                mensaje = f"Bienvenido  {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)