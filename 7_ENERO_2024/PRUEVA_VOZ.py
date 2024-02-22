# Untitled - By: Alex Soto - mié. feb. 7 2024

import time
from Maix import GPIO, I2S
from fpioa_manager import fm

# Configuración del usuario
sample_rate = 16000
record_time = 4  #s

# Registro de pines GPIO e I2S
fm.register(20, fm.fpioa.I2S0_IN_D0, force=True)
fm.register(18, fm.fpioa.I2S0_SCLK, force=True)
fm.register(19, fm.fpioa.I2S0_WS, force=True)

# Configuración del objeto I2S para la recepción de audio
rx = I2S(I2S.DEVICE_0)
rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode=I2S.STANDARD_MODE)
rx.set_sample_rate(sample_rate)

print(rx)

from speech_recognizer import isolated_word

# Crear objeto isolated_word para el usuario A
sr_a = isolated_word(dmac=2, i2s=I2S.DEVICE_0, size=10, shift=0) # maix bit set shift=1
print(sr_a.size()) # longitud de la palabra sr
print(sr_a.dtw(sr.get(0)))
print("Estoy leyendo la palabra para el usuario A")

# Umbral para el usuario A
sr_a.set_threshold(0, 0, 10000)

# Grabar y obtener & establecer para el usuario A
while True:
    time.sleep_ms(100)
    print("Estado del que habla ",sr_a.state())
    #print("")
    if sr_a.Done == sr_a.record(0):
        data_a = sr_a.get(0)
        print("Dato de la grabacion:",data_a)
        print("Tipo del dato: ", type(data_a))
        print("Longitu del dato de grabacion:",len(data_a))
        break
    if sr_a.Speak == sr_a.state():
        print("Valor del estado comparando con el hablante",sr_a.Speak)
        print('Usuario A hablando')

# Reconocimiento para el usuario A
print('Recognizer para el usuario A')
while True:
    time.sleep_ms(200)
    if sr_a.Done == sr_a.recognize():
        res_a = sr_a.result()
        print("Longitud resultado:",len(res_a))
        print("Tipo de tupla:",type(res_a))
        print("Usuario A detectado")
        print(res_a)
        if res_a == data_a:
            print("Bienvenido, Usuario A")
        else:
            print("USUARIO INCORRECTO")
        print("")
