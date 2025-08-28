# Yolov3 Project
Instituto Tecnológico de Costa Rica.<br/>
I Proyecto de Arquitectura de Computadores, segundo semestre, 2021.<br/>
- Samantha Acuña Montero.
- Katherine Amador González.
- Raquel Arguedas Sánchez.

## Explanation of the Yolo3 Algorithm

To explain this image recognition method, we need to define two concepts: Deep Learning and CNN. The first one is a type of machine learning that trains a computer to perform advanced tasks commonly done by humans, such as speech recognition, image identification, or making predictions. CNN stands for Convolutional Neural Networks, which are a type of artificial neural network where the neurons correspond to receptive fields in a way very similar to the neurons in the primary visual cortex of a biological brain.<br/>
The YOLO algorithm divides the image into several cells and calculates the probability that the desired object is found there. If the probability is below a certain threshold, the cell is discarded.<br/> <br/> This project is trained to recognize:

* Cars
* Men
* Women<br/>

## Tutorial

1. Clone this repository<br/>

```git
git clone https://github.com/samantha2302/Yolov3-Project.git
```

2. Inside the cloned folder, open the command line and run the following command: <br/>

```cd
pip install -r requirements.txt 
```

3. Once the repository is cloned, open `ProyectoMulticore.py` and execute it.<br/>

* Multiprocessing was implemented in two functions:

```py
multiprocessingVideoImages():
```

This function calls

```py
videoProcessor(videoName):
```

which is responsible for splitting videos (found in the **dataVideo** folder) into images. The video file names are passed as arguments in a list, and the resulting images are then saved in the **data** folder. Thanks to multiprocessing, this process takes a very short amount of time. The following image illustrates this:<br>

<br>![SSTiemposFragmentandoVideos](https://user-images.githubusercontent.com/91703769/139379259-a7ffee6f-87cf-4fb7-b2ad-4c87465c46e1.jpg)

<br/> The second use of multiprocessing in the code is for detecting objects in the images using the YOLO algorithm. The image names are already stored in a list, which are then passed as parameters to the processing function. To show the difference between sequential execution and multiprocessing, only 5 images were used, since linear processing takes a considerable amount of time.

```py
multiprocessing():
```

<br>Here we can see the importance of multiprocessing, as the execution time for object detection in images is significantly reduced.<br> <br>![SSTiemposYOLO](https://user-images.githubusercontent.com/91703769/139379971-4e7dc414-94fd-4c93-8f79-3c9c4505c789.jpg) <br>To simplify usage, the function that processes images sequentially has been commented out.

Finally, inside the ***runs\detect*** folder, different subfolders will be generated with the processed images.

### Example of a processed image

In the following image, we can see the different classes that are detected: <br> <br>![ImagenProcesadaEjemplo](https://user-images.githubusercontent.com/91703769/138800887-5f78a457-f103-4516-a527-40e16e82986a.jpg)<br/> <br/>

---

¿Quieres que lo deje en un inglés técnico formal (como documentación científica), o prefieres un tono un poco más sencillo y explicativo (para que cualquiera pueda seguirlo en GitHub)?


