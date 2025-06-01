from watchdog.observers import Observer 
from ImgHandler import ImgHandler, caminho
import time

print(f"ImgSentinel Iniciado")

count: int = 45
observer = Observer() # objeto para o obsever
handler = ImgHandler() # objeto para o handler

#conecta o observer com o handler e diz qual caminho vai ser vigiado
observer.schedule(handler, caminho, recursive=False) # recursive vai decidir se as subpastas do meu caminho serão monitoradas também, como está em False não será
observer.start()


try: 
    while count: # mantém o código rodando)
        print(count)
        time.sleep(2)
        count -= 1

except KeyboardInterrupt:
    observer.stop()

finally:
    print(f"Encerrando o Observer")
    observer.stop()
    observer.join()
    print(f"ImgSentinel Encerrado")