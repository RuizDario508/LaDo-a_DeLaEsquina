@echo off
echo === Creando entorno virtual ===
python -m venv venv
call venv\Scripts\activate

echo === Instalando dependencias ===
pip install -r backend\requirements.txt

echo === Migrando base de datos ===
cd backend
python manage.py migrate

echo === Creando superusuario ===
python manage.py createsuperuser

echo === Listo! Ejecuta con: python manage.py runserver ===
