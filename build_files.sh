# build_files.sh
pip install -r requirements.txt


# Kompilacja plików źródłowych
python setup.py build

# Wykonaj migracje bazy danych
python manage.py migrate

# Zebranie statycznych plików
python manage.py collectstatic --noinput

# Uruchomienie testów jednostkowych
python manage.py test
