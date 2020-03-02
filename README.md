Inicializacion:

sudo apt-get update
sudo apt-get install git
sudo apt-get install nano
sudo apt-get install unzip

wget https://bigdata20192.s3.amazonaws.com/uk-housing-prices-paid.zip

unzip wget

git clone https://github.com/cmce2019/proyecto_big_data
git config --global user.email "carlosm.cordoba1@correo.usa.edu.co"

Punto 1:
head -n 800000 price_paid_records.csv | python proyecto_big_data/punto_1/mapper.py | sort | python proyecto_big_data/punto_1/reducer.py 

Punto 2:
head -n 700 price_paid_records.csv | python proyecto_big_data/punto_2/mapper.py | sort | python proyecto_big_data/punto_2/reducer.py
Punto 3:
head -n 700 price_paid_records.csv | python proyecto_big_data/punto_3/mapper.py | sort | python proyecto_big_data/punto_3/reducer.py 
Punto 4: 
Esta en 1995 por cuestión de pruebas
head -n 10000 price_paid_records.csv | python proyecto_big_data/punto_4/mapper.py | sort -V 
Punto 5:
"Prueba": head -n 100 price_paid_records.csv | python proyecto_big_data/punto_5/mapper.py | sort | python proyecto_big_data/punto_1/reducer.py 
head -n 100 price_paid_records.csv | python proyecto_big_data/punto_5/mapper.py | sort | python proyecto_big_data/punto_5/reducer.py 

Punto 6:
head -n 100 price_paid_records.csv | python proyecto_big_data/punto_6/mapper.py | sort | python proyecto_big_data/punto_6/reducer.py | sort -V | python proyecto_big_data/punto_6/reducer2.py 

