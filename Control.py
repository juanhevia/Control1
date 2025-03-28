import threading
import queue
import time
import random

# Cola para almacenar imágenes
image_queue = queue.Queue()
stop_event = threading.Event() # Evento para detener los hilos de forma segura

# Función para simular la recepción de imágenes
def receive_images():
    image_id = 1
    while not stop_event.is_set():
        time.sleep(random.uniform(0.5, 2)) # Simula la llegada impredecible de imágenes
        image_name = f"image_{image_id}.jpg"
        image_queue.put(image_name)
        print(f"Recibida: {image_name}")
        image_id += 1

# Función para simular el procesamiento de imágenes
def process_images():
    while not stop_event.is_set() or not image_queue.empty():
        if not image_queue.empty():
            image_name = image_queue.get()
            print(f"Procesando: {image_name}")
            time.sleep(random.uniform(3, 6)) # Simula el procesamiento complejo de la imagen
            print(f"Finalizado: {image_name}")
            image_queue.task_done()
        else:
            time.sleep(1) # Espera si no hay imágenes en la cola

# Crear y arrancar los hilos de recepción y procesamiento
receiver_thread = threading.Thread(target=receive_images, daemon=True)
processor_thread = threading.Thread(target=process_images, daemon=True)

receiver_thread.start()
processor_thread.start()

#input del usuario o stop para detener el programa
input("Presiona Enter o escribe 'stop' para finalizar...\n")
stop_event.set()  # Indica a los hilos que deben detenerse
receiver_thread.join()
processor_thread.join()
print("Sistema detenido correctamente.")
