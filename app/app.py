from flask import Flask, render_template, request, url_for, redirect

app=Flask(__name__) #app es un objeto (una instancia de flask)

@app.before_request
def before_request():
    print("Antes de lapetición")

@app.after_request
def after_request(response):
    print("Después de la petición")
    return response

@app.route('/')     #ruta raíz (pág principal)
def index():
    #return "<h1>Probando</h1>"   #puede retornar texto, etiquetas html
    cursos=['PHP', 'Python', 'JavaScript', 'Java', 'Angular']
    data={
        'titulo':'Index',
        'bienvenida':'¡Hola!',
        'cursos':cursos,    #llama a la lista creada anteriormente
        'numero_cursos':len(cursos)
    }
    return render_template('index.html', data=data) ##como está en la carpeta 'templates', flask lo reconoce autmáticamente

@app.route('/contacto/<nombre>/<int:edad>')     #URL con decorador
def contacto(nombre, edad):
    data={
        'titulo':'Contacto',
        'nombre':nombre,
        'edad':edad
    }
    return render_template('contacto.html', data=data)
    
def query_string():
    print(request)                          #obtiene la petición del usuario
    print(request.args)                     #obtiene los argumentos de la petición
    print(request.args.get('param1'))       #obtiene el argumento del parámetro param1
    print(request.args.get('param2'))
    return "ok"
def pagina_no_encontrada(error):
    #return render_template('404.html'), 404 #es necesario que la función devuelva el código 404 
                                            #porque sino Flask va a devolver otro código de error para el que no tenemos respuesta
    return redirect(url_for('index'))       #ante error, redirige a 'index'(pág principal)
                                            #redirect(a dónde redirige) --> url_for(plantilla que queremos obtener url)
if __name__=='__main__': #el archivo solo se va a ejecutar si se ejecuta directamente, no como un módulo
    app.add_url_rule('/query_string', view_func=query_string)   #enlaza la funcion (2do param) a la URL (1er param)
    app.register_error_handler(404, pagina_no_encontrada)       #1er param el error, 2do param la función que invoca
    app.run(debug=True, port=5000)   #inicia el servidor web 
                                    #el modo de depuración permite que los cambios se vean al actualizar la app, sin detener el servidor




