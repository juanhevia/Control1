Este código simula la recepción y procesamiento de imágenes satelitales utilizando colas e hilos. 
Las imágenes entran de manera aleatoria y el código simula un tiempo de procesamiento también aleatorio para cada una de ellas, 
por lo que pueden entrar muchas imágenes a la vez o ninguna, y pueden tarder mucho o poco en procesarse.
Trabajará indefinidamente hasta que se pare manualmente (puede hacerse escribiendo stop en el teclado o presionando Enter).
El código utiliza .join() para que todas las imágenes recibidas se procesen; es decir, no se para abruptamente 
si no que dejan de recibirse imágenes y acaba cuando todas las imágenes recibidas son procesdas.
