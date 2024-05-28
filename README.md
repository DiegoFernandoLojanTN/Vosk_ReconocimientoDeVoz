# Vosk_ReconocimientoDeVoz
Este proyecto se realizó como una prueba para evaluar el funcionamiento del modelo VOSK en el reconocimiento de voz. El modelo VOSK es una poderosa herramienta de código abierto que permite la transcripción de audio a texto en tiempo real. 

[![VOSK](https://i.postimg.cc/NMYXL0rX/imagen-2024-05-28-172456500.png)](https://postimg.cc/McPHFq5Z)

## Grupo GEO.VOICE-TECH

Este proyecto está a cargo del grupo GEO.VOICE-TECH, que se enfoca en desarrollar aplicaciones y sistemas donde el reconocimiento de voz es fundamental para la toma de notas por parte de personas que no pueden escribir durante el trabajo de campo. 

[![GEO](https://i.postimg.cc/MZ3cJ5tV/imagen-2024-05-28-172726543.png)](https://postimg.cc/9zTXGG6Q)

## Instalación

Para ejecutar este código y probar el reconocimiento de voz con VOSK, sigue estos pasos:

1. **Clonar el repositorio**
    ```powershell
    git clone https://github.com/DiegoFernandoLojanTN/Vosk_ReconocimientoDeVoz.git
    ```
    ```powershell
    cd Vosk_ReconocimientoDeVoz
     ```
2. **Crear un entorno virtual**
    ```powershell
    python -m venv venv
    ```
    ```powershell
    source venv/bin/activate # En Windows usa venv\Scripts\activate
    ```

3. **Instalar las dependencias**
    ```powershell
    pip install -r requirements.txt
    ```

4. **Preparar el modelo VOSK**
- Crea en la raíz del proyecto una carpeta llamada `ASSETS/Vosk`.
- Descarga el modelo de VOSK desde [este enlace](https://alphacephei.com/vosk/models) y extrae los archivos dentro de la carpeta `ASSETS/Vosk`.

## Código

El proyecto consta de dos archivos principales:

- **vosk_recog.py**: Este script configura el modelo de reconocimiento de voz y procesa el audio de entrada, transcribiéndolo a texto.
- **app.py**: Este script es el punto de entrada del proyecto. Inicia el reconocimiento de voz y muestra las transcripciones en tiempo real.


5. **Proyectos Relacionados**

Además de este proyecto, estamos desarrollando una interfaz web que puede ser encontrada en el siguiente repositorio:
- [VoskGeoVoiceTech](https://github.com/jahirxtrap/VoskGeoVoiceTech.git)

También estamos trabajando en una aplicación para Android que utiliza una versión más ligera del modelo VOSK, diseñada específicamente para dispositivos móviles:
- [GeoMinerTranscripts](https://github.com/jahirxtrap/GeoMinerTranscripts)

