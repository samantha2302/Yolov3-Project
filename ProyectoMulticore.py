import cv2
import math
import os
from os import mkdir
import time
import concurrent.futures

#funcion que pasa las imagenes por el detector de yolo
def detector(path):
    os.system("py detect.py --weights best.pt --img 640 --conf 0.25 --source data/" + path) 


#lista que guarda los nombres de las imagenes guardadas en la carpeta data
imagenesPorDetectar = os.listdir("data")



def sinMultiprossesing():
    start = time.perf_counter()
    for imagen in imagenesPorDetectar:
        detector(imagen)
    print(f'Duración sin multiprocesamiento: {time.perf_counter() - start}')

def multiprocessing():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for imagen in imagenesPorDetectar:
            executor.submit(detector, imagen)
    print(f'Duración con multiprocesamiento: {time.perf_counter() - start}')




if __name__ == '__main__':
    sinMultiprossesing()
    multiprocessing()


    
