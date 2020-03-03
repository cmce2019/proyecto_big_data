# Inicializacion:

ssh -i "clave.pem" hadoop@ec2-184-72-104-249.compute-1.amazonaws.com

sudo yum update

sudo yum install git

sudo yum install nano

sudo yum install unzip

wget https://bigdata20192.s3.amazonaws.com/uk-housing-prices-paid.zip

unzip wget

git clone https://github.com/cmce2019/proyecto_big_data

git config --global user.email "carlosm.cordoba1@correo.usa.edu.co"

git config --global user.name "Carlos Mama Huevo"

# Punto 1:
head -n 800000 price_paid_records.csv | python proyecto_big_data/punto_1/mapper.py | sort | python proyecto_big_data/punto_1/reducer.py 

# hadoop:
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_1/mapper.py,/home/hadoop/proyecto_big_data/punto_1/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input -output /output_1

# Punto 2:
head -n 700 price_paid_records.csv | python proyecto_big_data/punto_2/mapper.py | sort | python proyecto_big_data/punto_2/reducer.py

# hadoop:
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_2/mapper.py,/home/hadoop/proyecto_big_data/punto_2/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input -output /output_2

# Punto 3:
head -n 700 price_paid_records.csv | python proyecto_big_data/punto_3/mapper.py | sort | python proyecto_big_data/punto_3/reducer.py

# hadoop:
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_3/mapper.py,/home/hadoop/proyecto_big_data/punto_3/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input -output /output_3 

# Punto 4: 
Esta en 1995 por cuestión de pruebas
head -n 10000 price_paid_records.csv | python proyecto_big_data/punto_4/mapper.py | sort -V 

# hadoop:
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_4/mapper.py,/home/hadoop/proyecto_big_data/punto_4/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input -output /output_4
# Punto 5:
![#f03c15](https://placehold.it/15/f03c15/000000?text=+)"Prueba":

 head -n 100 price_paid_records.csv | python proyecto_big_data/punto_5/mapper.py | sort | python proyecto_big_data/punto_1/reducer.py 

head -n 100 price_paid_records.csv | python proyecto_big_data/punto_5/mapper.py | sort | python proyecto_big_data/punto_5/reducer.py 

# hadoop:
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_5/mapper.py,/home/hadoop/proyecto_big_data/punto_5/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input -output /output_5
 
# Punto 6:
head -n 100 price_paid_records.csv | python proyecto_big_data/punto_6/mapper.py | sort | python proyecto_big_data/punto_6/reducer.py | sort -V | python proyecto_big_data/punto_6/reducer2.py 

# hadoop:
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_6/mapper.py,/home/hadoop/proyecto_big_data/punto_6/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input -output /output_6
