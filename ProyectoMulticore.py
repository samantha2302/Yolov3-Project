import cv2
import math
import os
from os import mkdir
import time
import concurrent.futures




#genera una lista con los videos por fragmentar en imagenes
videosPorDetectar = os.listdir("dataVideo")


#fragmenta un video en imagenes
def videoProcessor(videoName):
    capture = cv2.VideoCapture("C:\\Users\\raque\\OneDrive - Estudiantes ITCR\\Raquel\\TEC\\II Semestre 2021\\Arquitectura de computadores\\Semana 14\\Yolov3-Project\\dataVideo\\" + videoName)
    cont = 0
    path = "C:\\Users\\raque\\OneDrive - Estudiantes ITCR\\Raquel\\TEC\\II Semestre 2021\\Arquitectura de computadores\\Semana 14\\Yolov3-Project\\data\\"

    while (capture.isOpened()):
        ret, frame = capture.read()
        if (ret == True):
            cv2.imwrite(path + "videoExtract_%04d.jpg" % cont, frame)    
            cont += 1
            if (cv2.waitKey(1) == ord('s')):
                break
        else:
            break

    capture.release()
    cv2.destroyAllWindows()



#utiliza multiprocesamiento para fragmentar los videos
def multiprocessingVideoImages():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for video in videosPorDetectar:
            executor.submit(videoProcessor, video)
    print(f'Duración de la framentacion de los videos, en segundos, con multiprocesamiento: {time.perf_counter() - start}')



#funcion que pasa las imagenes por el detector de yolo
def detector(path):
    os.system("py detect.py --weights best.pt --img 640 --conf 0.25 --source data/" + path) 


#lista que guarda los nombres de las imagenes guardadas en la carpeta data
imagenesPorDetectar = os.listdir("data")



def sinMultiprossesing():
    start = time.perf_counter()
    for imagen in imagenesPorDetectar:
        detector(imagen)
    print(f'Duración sin multiprocesamiento de la detección de objetos, en segundos: {time.perf_counter() - start}')

def multiprocessing():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for imagen in imagenesPorDetectar:
            executor.submit(detector, imagen)
    print(f'Duración con multiprocesamiento de la detección de objetos, en segundos: {time.perf_counter() - start}')




if __name__ == '__main__':
    multiprocessingVideoImages()
    #sinMultiprossesing()
    multiprocessing()


    
