# Yolov3 Project
Instituto Tecnologico de Costa Rica.<br/>
I Proyecto de Arquitectura de Computadores, segundo semestre, 2021.<br/>
Samantha Acuña Montero, Katherine Amador González, Raquel Arguedas Sánchez.

## Explicación del algoritmo Yolo3
Para explicar este método de reconocimiento de imágenes, vamos a definir dos conceptos: Deep Learning y CNN, el primero es un tipo de machine learning que entrena a una computadora para que realice tareas avanzadas, comunmente realizadas por seres humanos, como el reconocimiento del habla, la identificación de imágenes o hacer predicciones. El CNN es el diminutivo de redes neuronales convolucionales, estas son un tipo de red neuronal artificial donde las neuronas corresponden a campos receptivos de una manera muy similar a las neuronas en la corteza visual primaria de un cerebro biológico.<br/>
El algoritmo Yolo, procede a dividir la imagen en varias celdas, y calcula la probabilidad de que el objeto buscado se encuentre ahí, si la probabilidad esta debajo de un rango determinado, desecha esa celda.

# Tutorial
1. Clonar este repositorio<br/>
```git clone https://github.com/samantha2302/Yolov3-Project.git```  <br/> <br/> 
2. Dentro de la carpeta clonada, ingresar a la consola y copiar el siguiente comando: <br/>
```pip install -r requirements.txt ``` 
Este proyecto esta entrenado para reconocer carros, hombres y mujeres dentro de una imágen.  <br/> <br/> 
3. Ya con el repositorio clonado, se ingresa al documento de python *ProyectoMulticore*, y se ejecuta. Dentro de la carpeta en **runs\detect** se nos van a generar diferentes carpetas con las imagenes ya procesadas. Además, en consola, se nos van a mostrar la diferencia entre los tiempos, de haber ejecutado el algoritmo con multiprocesamiento y de manera secuencial. <br/> <br/> 
### Prueba de los tiempos
![SSTiempos](https://user-images.githubusercontent.com/91703769/138800932-86b82dbd-ea30-4706-9839-97b6c48613a6.jpg)
### Ejemplo de imagen procesada
![ImagenProcesadaEjemplo](https://user-images.githubusercontent.com/91703769/138800887-5f78a457-f103-4516-a527-40e16e82986a.jpg)
