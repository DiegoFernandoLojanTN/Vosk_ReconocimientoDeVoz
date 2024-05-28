from typing import Generator
import pyaudio
from vosk import Model, KaldiRecognizer
import json

class VoiceRecognizer:
    def __init__(self, model_path: str = "ASSETS/Vosk/vosk-model-es-0.42", device_index: int = 2):
        """
        Inicializa el reconocedor de voz con el modelo especificado.
        
        Args:
        model_path (str): Ruta al modelo de VOSK.
        device_index (int): Índice del dispositivo de entrada de audio.
        """
        self.model_path = model_path
        self.device_index = device_index
        self.model = Model(self.model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
        print("Inicialización del modelo de reconocimiento de voz completada.")

    def stream_audio(self, prints: bool = True) -> Generator[str, None, None]:
        """
        Comienza a transcribir audio en tiempo real.

        Args:
        prints (bool): Si True, imprime la transcripción en consola.

        Yields:
        str: Transcripciones del audio.
        """
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192, input_device_index=self.device_index)
        stream.start_stream()
        print("Transmisión de audio iniciada.")

        try:
            while True:
                data = stream.read(8192, exception_on_overflow=False)
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    if 'text' in result:
                        transcript = result['text'].lower()
                        if prints:
                            print(f"\rTranscripción: {transcript}")
                        yield transcript
                else:
                    partial_result = json.loads(self.recognizer.PartialResult())
                    if prints and "partial" in partial_result:
                        print(f"\rHablando: {partial_result['partial']}", end='', flush=True)
        finally:
            stream.stop_stream()
            stream.close()
            audio.terminate()
            print("Transmisión de audio finalizada correctamente.")

if __name__ == "__main__":
    recognizer = VoiceRecognizer()
    stop_words = ["stop", "parar"]  # Lista de palabras clave para detener
    for speech in recognizer.stream_audio():
        if any(word in speech for word in stop_words):
            print(f"Detección de palabra clave '{speech}'. Terminando sesión...")
            break
