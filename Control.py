import queue
import threading
import time
import random

# Cola para almacenar las imágenes recibidas
image_queue = queue.Queue()

# Función para simular la recepción de imágenes

def receive_images():
    image_id = 1
    while True:
        time.sleep(random.uniform(0.5, 2))  # Simula la llegada impredecible de imágenes
        image_name = f"image_{image_id}.jpg"
        image_queue.put(image_name)
        print(f"Recibida: {image_name}")
        image_id += 1

# Función para simular el procesamiento de imágenes

def process_images():
    while True:
        if not image_queue.empty():
            image_name = image_queue.get()
            print(f"Procesando: {image_name}")
            time.sleep(random.uniform(3, 6))  # Simula el procesamiento complejo de la imagen
            print(f"Finalizado: {image_name}")
            image_queue.task_done()
        else:
            time.sleep(1)  # Espera si no hay imágenes en la cola

# Crear y arrancar los hilos de recepción y procesamiento
receiver_thread = threading.Thread(target=receive_images, daemon=True)
processor_thread = threading.Thread(target=process_images, daemon=True)

receiver_thread.start()
processor_thread.start()

# Mantener el programa en ejecución
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Finalizando sistema...")
