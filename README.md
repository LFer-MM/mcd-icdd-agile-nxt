# mcd-icdd-agile-nxt
Repositorio dedicado al ejercicio de Metodologias Agiles de la materia de Introduccion a la Ciencia de Datos.

Se hizo bosquejo de una Web GUI que se pretende sirva como control remoto, que enviara comandos desde el backend (Python usando funciones de NXT-Python) via Bluetooth (en esta version solo se dejo USB, las pruebas con Bluetooth se haran mas adelante ya que la instalacion debe ser via GitHub, no via Pip) hacia el Brick del Robot.

Se intento dejar todo en un acomodo basico para no complicar mucho.

El enlace o framework que nos permitira trabajar el frontend, la Web GUI (HTML/CSS/Js), y el backend, Python (para usar NXT-Python) es Flask.

Propuesta unicamente. No significa que se descarten para siempre las VMs de Windows, esto es solo una alternativa.

---------------------------------------------------------------------------------------------------------------------------------------

Se añadieron funciones de JavaScript para que las llamadas a los endpoints de la API de Flask no requieran refresh de la pagina de la interfaz.

Ya solo resta cargar la logica de NXT-Python a los endpoints de Flask en el app.py y si a alguien le da por pimpear los HTML/CSS.

NOTA: Para que el programa con NXT-Python funcione por bluetooth, hay que instalar (con pip) en su ambiente de Python el paquete de PyBluez desde github, no desde PyPi (el de PyPi esta desactualizado). Eso no viene en el requirements porque por default los baja de PyPi al correr "pip install requirements.txt".

Hasta aqui mi reporte, Joaquin.

<img width="1429" alt="Screenshot 2024-09-29 at 12 22 10 p m" src="https://github.com/user-attachments/assets/5b437e23-8814-4e4a-b803-746bb50de016">
