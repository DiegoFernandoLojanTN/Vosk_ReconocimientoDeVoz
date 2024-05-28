from ENGINE.STT.vosk_recog import VoiceRecognizer

try:
    recognizer = VoiceRecognizer()
    print("Iniciando el reconocimiento de voz. Presione Ctrl+C para detener.")
    for speech in recognizer.stream_audio():
        if speech.strip():  # Ignora los resultados vacíos
            print("Humano >>", speech)
except KeyboardInterrupt:
    print("\nReconocimiento de voz detenido por el usuario.")
except Exception as e:
    print("\nError durante el reconocimiento de voz:", e)
finally:
    print("Proceso de reconocimiento de voz finalizado.")
