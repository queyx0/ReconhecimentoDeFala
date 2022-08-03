import speech_recognition as sr

rec = sr.Recognizer()
print(sr.Microphone().list_microphone_names()) 
# --> VER LISTA DE MICROFONES NO COMPUTADOR E COLOCAR A POSIÇÃO NA LSITA DO ESCOLHIDO NO () DE sr.Microphone

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)