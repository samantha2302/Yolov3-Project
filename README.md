# Yolov3 Project
Instituto Tecnológico de Costa Rica.<br/>
I Proyecto de Arquitectura de Computadores, segundo semestre, 2021.<br/>
Samantha Acuña Montero, Katherine Amador González, Raquel Arguedas Sánchez.

## Explicación del algoritmo Yolo3 
Para explicar este método de reconocimiento de imágenes, vamos a definir dos conceptos: Deep Learning y CNN, el primero es un tipo de machine learning que entrena a una computadora para que realice tareas avanzadas, comunmente realizadas por seres humanos, como el reconocimiento del habla, la identificación de imágenes o hacer predicciones. El CNN es el diminutivo de redes neuronales convolucionales, estas son un tipo de red neuronal artificial donde las neuronas corresponden a campos receptivos de una manera muy similar a las neuronas en la corteza visual primaria de un cerebro biológico.<br/>
El algoritmo Yolo, procede a dividir la imagen en varias celdas, y calcula la probabilidad de que el objeto buscado se encuentre ahí, si la probabilidad esta debajo de un rango determinado, desecha esa celda.

# Tutorial
1. Clonar este repositorio<br/>
```git clone https://github.com/samantha2302/Yolov3-Project.git```  <br/> <br/> 
2. Dentro de la carpeta clonada, ingresar a la consola y copiar el siguiente comando: <br/>
```pip install -r requirements.txt ``` <br/>
Este proyecto esta entrenado para reconocer carros, hombres y mujeres dentro de una imágen.  <br/> <br/> 
3. Ya con el repositorio clonado, se ingresa al documento de python *ProyectoMulticore*, y se ejecuta.<br/>
  -Se implementó multiprocesamiento en dos funciones:
  ```def multiprocessingVideoImages():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for video in videosPorDetectar:
            executor.submit(videoProcessor, video)
    print(f'Duración de la framentacion de los videos, en segundos, con multiprocesamiento: {time.perf_counter() - start}')
   ```
<br/>En esta función, se realiza un llamado a la función ```videoProcessor(videoName)```  que es la encargada de fragmentar en imágenes los videos encontrados en la carpeta *dataVideo*, como argumento se le dan los nombres de archivos de video guardados en una lista, y posteriormente los guarda en la carpeta *data*, y gracias al multiprocesamiento los tiempos en que se realiza son sumamente cortos. En la siguiente imagen se puede apreciar:
![SSTiemposFragmentandoVideos](https://user-images.githubusercontent.com/91703769/139379259-a7ffee6f-87cf-4fb7-b2ad-4c87465c46e1.jpg)

<br/> La segunda implementación de multiprocesamiento que se da en el código es para detectar los objetos en las imágenes, mediante el algoritmo de YOLO. En una lista ya se encuentran guardadas los nombres de las imágenes, para enviarlos como parámetros a la funcion que las procesa. Para mostrar la diferencia entre los tiempos al realizarlo de manera secuencial y con multiprocesamiento solo se ultilizaron 5 fotografías, ya que la función que lo realiza de manera lineal si toma un lapso de tiempo considerable. 
 ```def multiprocessing():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for imagen in imagenesPorDetectar:
            executor.submit(detector, imagen)
    print(f'Duración con multiprocesamiento de la detección de objetos, en segundos: {time.perf_counter() - start}')
   ```
![SSTiemposYOLO](https://user-images.githubusercontent.com/91703769/139379971-4e7dc414-94fd-4c93-8f79-3c9c4505c789.jpg)
    Para facilitar el uso de este código, se comentó la función que procesa las imágenes linealmente.

<br/>Dentro de la carpeta en **runs\detect** se nos van a generar diferentes carpetas con las imagenes ya procesadas.


### Ejemplo de una imagen procesada
![ImagenProcesadaEjemplo](https://user-images.githubusercontent.com/91703769/138800887-5f78a457-f103-4516-a527-40e16e82986a.jpg)<br/> <br/> 

Podemos observar que al haber implementado el multiprocesamiento, los tiempos de ejecución para la obtención de objetos dentro de imágenes se reducen considerablemente. 
