# Set up:
```diff
-AWS access:

ssh -i "clave.pem" host

-Instance set up:

sudo yum update

sudo yum install git

sudo yum install nano

sudo yum install unzip

-data-set download and input set up:

wget https://bigdata20192.s3.amazonaws.com/uk-housing-prices-paid.zip

unzip uk-housing-prices-paid.zip

hdfs dfs -mkdir /input

hdfs dfs -put price_paid_records.csv /input

-git set up:

git clone https://github.com/cmce2019/proyecto_big_data

git config --global user.email "carlosm.cordoba1@correo.usa.edu.co"

git config --global user.name "cmce2019"
```
# 1:
```diff
-test: 

head -n 800000 price_paid_records.csv | python proyecto_big_data/punto_1/mapper.py | sort | python proyecto_big_data/punto_1/reducer.py 
```

```diff
-Hadoop test: 

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_1/mapper.py,/home/hadoop/proyecto_big_data/punto_1/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input -output /output_1
```
# 2:
```diff
-test: 

head -n 700 price_paid_records.csv | python proyecto_big_data/punto_2/mapper.py | sort | python proyecto_big_data/punto_2/reducer.py
```
```diff
-Hadoop test: 

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_2/mapper.py,/home/hadoop/proyecto_big_data/punto_2/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input -output /output_2
```
# 3:
```diff
-test: 

head -n 700 price_paid_records.csv | python proyecto_big_data/punto_3/mapper.py | sort | python proyecto_big_data/punto_3/reducer.py
```
```diff
-Hadoop test: 

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_3/mapper.py,/home/hadoop/proyecto_big_data/punto_3/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input -output /output_3 
```
# 4:
```diff
-test: 
 
+Esta en 1995 por cuestión de pruebas
head -n 10000 price_paid_records.csv | python proyecto_big_data/punto_4/mapper.py | sort -V 
```
```diff
-Hadoop test: 

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_4/mapper.py,/home/hadoop/proyecto_big_data/punto_4/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input -output /output_4
```
# 5:
```diff
-test sum: 

 head -n 100 price_paid_records.csv | python proyecto_big_data/punto_5/mapper.py | sort | python proyecto_big_data/punto_1/reducer.py
``` 
```diff
-test 1: 

head -n 100 price_paid_records.csv | python proyecto_big_data/punto_5/mapper.py | sort | python proyecto_big_data/punto_5/reducer.py
``` 
```diff
-Hadoop test: 

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_5/mapper.py,/home/hadoop/proyecto_big_data/punto_5/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input -output /output_5


```
# 6:
```diff
-test: 

head -n 100 price_paid_records.csv | python proyecto_big_data/punto_6/mapper.py | sort | python proyecto_big_data/punto_6/reducer.py | sort -V | python proyecto_big_data/punto_6/reducer2.py 

```
```diff
-Hadoop test: 
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_6/mapper.py,/home/hadoop/proyecto_big_data/punto_6/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input -output /input_p2

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files /home/hadoop/proyecto_big_data/punto_6/mapper.py,/home/hadoop/proyecto_big_data/punto_6/reducer.py -mapper "python mapper.py" -reducer "python reducer.py" -input /input_p2/part* -output /input_6

```
