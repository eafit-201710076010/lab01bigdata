# lab01bigdata

## Laura Sánchez Córdoba

# Bitácora

### Gestión de Datos:

**Datasets en DCA**

**![](http://imgfz.com/i/qp5ir0M.png)**
Instalación del AWS CLI

**![](http://imgfz.com/i/GSUc94b.png)**

**Datasets en AWS S3**

 **![](http://imgfz.com/i/djt4Dkf.png)**
 
**Datasets en AWS por medio del CLI**
 
 **![](http://imgfz.com/i/mIqaMhB.png)**
 
 **![](http://imgfz.com/i/fdC5sKJ.png)**
 
**Datasets desde el shell en 192.168.10.116 a AWS S3**
 
  **![](http://imgfz.com/i/wamyovF.png)**
  
  **![](http://imgfz.com/i/kzFxbaj.png)**
  
 **Datasets en HUE**
  
  **![](http://imgfz.com/i/6nsYyXF.png)**
  
  **Datasets en cluster EMR** 
  
  **![](http://imgfz.com/i/fnEilRB.png)**
  
 ### Ejecución del Wordcount local y MRjob
  
 **Local DCA**
 ```
 $ cd 02-mapreduce
 
 $ python wordcount-local.py /datasets/gutenberg-small/*.txt > salida-serial.txt 
 
 $ more salida-serial.txt
  ```
  **![](http://imgfz.com/i/U9mAvGt.png)**
  
 **MRJob**
 ```
 $ cd 02-mapreduce
 
 $ python wordcount-mr.py ../datasets/gutenberg-small/*.txt
 ``` 
 **![](http://imgfz.com/i/GL12x8i.png)**
  
 ### Ejercicio 1 de MapReduce/MRJob
  
  **Enunciado**
  
1. Se tiene un conjunto de datos, que representan el salario anual de los empleados formales en Colombia por sector económico, según la DIAN.

La estructura del archivo es: (sececon: sector económico) (archivo: dataempleados.csv)

idemp,sececon,salary,year

3233,1234,35000,1960

3233,5434,36000,1961

1115,3432,34000,1980

3233,1234,40000,1965

1115,1212,77000,1980

1115,1412,76000,1981

1116,1412,76000,1982

Realizar un programa en Map/Reduce, con hadoop en Python o Java, que permita calcular:

- El salario promedio por Sector Económico (SE)
- El salario promedio por Empleado
- Número de SE por Empleado que ha tenido a lo largo de la estadística
  
  1. 
  **![](http://imgfz.com/i/XsNGOtJ.png)**
  
  ```python employees1.py dataempleados.csv```
  
  2.
  **![](http://imgfz.com/i/rN5m7MD.png)**
  
 ```python employees2.py dataempleados.csv```
  
  3.
  **![](http://imgfz.com/i/Jz9kAI3.png)**
  
 ```python employees3.py dataempleados.csv```
 
 ### Creación de Clúster por CLI 
  
  **![](http://imgfz.com/i/au9j0PC.png)**
  
  **Script de creación y terminación de clusters**
  
  **![](http://imgfz.com/i/GwFpRJY.png)**
  
  **Conexión al Clúster desde SSH** 
  
  **![](http://imgfz.com/i/MV3UnI5.png)**
  
  **Acceso al Hue desde el Clúster**
  
  **![](http://imgfz.com/i/DKkPh2t.png)**
  
  **Acceso a Zeppelin y creación de un Notebook** 
  
  **![](http://imgfz.com/i/rHj582P.png)**

### Wordcount con datos en hdfs
```
python wordcount-mr.py hdfs:///user/lsanchezc/datasets/gutenberg-small/*.txt -r hadoop
```

**Correr Wordcount-mr.py con hdfs en EMR** 

**![](http://imgfz.com/i/tSR4BW3.png)**
  
**Correr Wordcount-mr.py con hdfs en el  DCA** 

**![](http://imgfz.com/i/YthCGFo.png)**
