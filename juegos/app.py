from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Necesario para usar sesiones

# Configuración inicial
ELEMENTOS = ["limón", "pera", "manzana"]

def inicializar_juego():
    if 'inventario' not in session:
        session['inventario'] = [random.choice(ELEMENTOS) for _ in range(10)]
    if 'historial' not in session:
        session['historial'] = []

def contar_grupos():
    conteo = {
        "limón": session['inventario'].count("limón"),
        "pera": session['inventario'].count("pera"),
        "manzana": session['inventario'].count("manzana")
    }
    return min(conteo.values())

@app.route('/', methods=['GET', 'POST'])
def index():
    inicializar_juego()
    
    if request.method == 'POST':
        accion = request.form.get('accion')
        
        if accion == 'canjear_grupos':
            if contar_grupos() >= 2:
                # Crear copia modificable del inventario
                inventario = session['inventario'].copy()
                
                # Eliminar 2 grupos (2 de cada elemento)
                try:
                    for _ in range(2):
                        for elemento in ELEMENTOS:
                            inventario.remove(elemento)
                    
                    # Añadir regalo
                    inventario.append("regalo")
                    session['historial'].append("Canjeaste 2 grupos por 1 regalo")
                    
                    # Añadir elementos extras
                    extra1 = request.form.get('extra1')
                    extra2 = request.form.get('extra2')
                    
                    if extra1 in ELEMENTOS:
                        inventario.append(extra1)
                    if extra2 in ELEMENTOS:
                        inventario.append(extra2)
                    
                    session['historial'].append(f"Añadiste {extra1} y {extra2}")
                    
                    # Actualizar inventario en la sesión
                    session['inventario'] = inventario
                except ValueError as e:
                    session['historial'].append("Error al canjear: " + str(e))
            
        elif accion == 'canjear_regalo':
            if "regalo" in session['inventario']:
                inventario = session['inventario'].copy()
                inventario.remove("regalo")
                nuevos = []
                
                for i in range(6):
                    nuevo = request.form.get(f'nuevo_{i}')
                    if nuevo in ELEMENTOS:
                        inventario.append(nuevo)
                        nuevos.append(nuevo)
                
                session['historial'].append(f"Canjeaste 1 regalo por: {', '.join(nuevos)}")
                session['inventario'] = inventario
        
        elif accion == 'reiniciar':
            session['inventario'] = [random.choice(ELEMENTOS) for _ in range(10)]
            session['historial'] = ["Juego reiniciado"]
        
        return redirect(url_for('index'))
    
    return render_template('index.html', 
                         elementos=ELEMENTOS,
                         inventario=session['inventario'],
                         grupos_posibles=contar_grupos(),
                         historial=session['historial'])

if __name__ == '__main__':
    app.run(debug=True)