import speech_recognition as sr
from maix_asr import MaixAsr

# Inicializar el reconocimiento de voz con maix_asr
maix_asr = MaixAsr()

# Cargar el modelo acústico (por ejemplo, maix_asr_2900k_0x50000)
#maix_asr.load_acoustic_model("maix_asr_2900k_0x50000")

# Definir la vocabularia de pinyin
vocabulary = ["abc", "def", "ghi", "jkl", "mno", "pqr", "rst", "tuv", "wxyz"]
maix_asr.set_vocabulary(vocabulary)

# Reconocer la voz del usuario
while True:
    audio = maix_asr.record_voice()
    if audio is not None:
        result = maix_asr.recognize_voice(audio)
        print(f"Resultado: {result}")

# Utilizar la biblioteca isolated_word de speech_recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

try:
    while True:
        audio = microphone.listen()
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
except sr.UnknownValueError:
    print("Sorry, I couldn't understand that.")
except sr.RequestError:
    print("Sorry, there was an error processing your request.")

if __name__ == "__main__":
    maix_asr.run()