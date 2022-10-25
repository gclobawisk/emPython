#import playsound
import winsound

#playsound(r'C:\Users\Gabriel\PycharmProjects\pythonProject\0000912.wav')

contador = 1
while True:
    if contador == 1:
        winsound.PlaySound(r'C:\Users\Gabriel\PycharmProjects\pythonProject\0000912.wav', winsound.SND_FILENAME)
    contador +=1