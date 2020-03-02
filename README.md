Inicializacion:

sudo apt-get update
sudo apt-get install git
sudo apt-get install nano
sudo apt-get install unzip

wget https://bigdata20192.s3.amazonaws.com/uk-housing-prices-paid.zip

unzip wget

git clone https://github.com/cmce2019/proyecto_big_data


Punto 1:

Punto 2:

Punto 3:

Punto 4: 

Punto 5:
"Prueba": head -n 100 price_paid_records.csv | python proyecto_big_data/punto_5/mapper.py | sort | python proyecto_big_data/punto_1/reducer.py 
head -n 100 price_paid_records.csv | python proyecto_big_data/punto_5/mapper.py | sort | python proyecto_big_data/punto_5/reducer.py 

Punto 6:
head -n 100 price_paid_records.csv | python proyecto_big_data/punto_6/mapper.py | sort | python proyecto_big_data/punto_6/reducer.py | sort -V | python proyecto_big_data/punto_6/reducer2.py 

