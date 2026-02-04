# Team_TRG_e-commerce
Repositorio destinado a los avances del proyecto. Ciclo-02-2025, Transacciones Comerciales por Medios Electrónicos

---

# PASOS PARA EJECUTAR EL BACKEND DE MANERA LOCAL:

**Necesario tener:**

- Python versión >= 3...
- Pip
- Postman (opcional pero recomendado para evaluar las rutas)
- Workbench

---

## PASO 1:

- Descargar el proyecto:
  - En .rar o zip.
  - O Clonación: `https://github.com/WilliamsRod19/prueba-JWT.git`

---

## PASO 2:

- Posicionarse en el repositorio y crear un entorno virtual:
  1. Abrir terminal y `cd` hasta el repositorio.
  2. Ejecutar el comando: `python -m venv env` (se creará una carpeta env en el mismo nivel de la carpeta backend)
  3. Para activar el entorno virtual el comando es: `env\Scripts\activate` (debemos estar en el mismo nivel de la carpeta env)

---

## PASO 3:

- Ejecutar librerías comandos:
  1. `cd ToDoPruebaJWT`
  2. `pip install -r requirements.txt`

---

## PASO 4:

- Hacer migraciones comandos (estar en el mismo nivel de backend):
  1. `python manage.py migrate`
  2. `python manage.py makemigrations`
  3. `python manage.py migrate`
- Crear un super usuario:
  1. `python manage.py createsuperuser`
  2. Ponerle nombre de usuario, correo y contraseñas genéricos (`admin`, `me@admin.com`, `123`)
  3. Dirá que la contraseña es débil pero dejenlo pasar (Y)

---

## PASO 6:

- Correr el servidor comando (estar en el mismo nivel de backend):
  - `python manage.py runserver 127.0.0.1:8000` (antes es necesario conocer nuestra ip)

## EndPoints Para Realizacion de Pruebas
- POST http://127.0.0.1:8000/api/token/ - Para Obtencion de Token
Body:
{
  "username": "username",
  "password": "password"
}

- GET http://127.0.0.1:8000/api/v1/todos/ - Para Listar los Datos
Header:
Authorization: Bearer [Token]

- POST http://127.0.0.1:8000/api/v1/todos/ Para crear datos 
Body:
{
  "title": "Aprender ingles",
  "description": "Tarea de aprender ingles"
}

Header:
Authorization: Bearer [Token]

- PUT http://127.0.0.1:8000/api/v1/todos/ID/ Para crear datos 
Body:
{
  "title": "Aprender ingles",
  "description": "Tarea de aprender ingles"
}

Header:
Authorization: Bearer [Token]

- DELETE http://127.0.0.1:8000/api/v1/todos/ID/ Para crear datos 