from watchdog.events import FileSystemEventHandler
import time
import shutil
import os
from typing import Set

caminho: str = r"C:\Users\Gustavo H. Valadares\Downloads"  
destino: str = r"C:\Users\Gustavo H. Valadares\Pictures" 
extensoes_img: Set[str] = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}

# necessário criar um subclasse de FileSystemEventHandler para sobreescrever métodos vazios dela 
class ImgHandler(FileSystemEventHandler): # assim se cria uma subclasse de FileSystemEventHandler

    def on_created(self, event): 
        arquivo = event.src_path
        # print(arquivo)

        time.sleep(5)
        for ext in extensoes_img:
            print(f"Extensão: {ext}")
            if arquivo.endswith(ext):
                
                while True: # é necessário esperar que o arquivo esteja baixado, esse looping garante isso 
                    try: 
                        tamanho1 = os.path.getsize(arquivo)
                        time.sleep(1)
                        tamanho2 = os.path.getsize(arquivo)

                        if tamanho1 == tamanho2: #se os dois tamanhos são iguais, antes de depois de um segundo, significa que o arquivo terminou de baixar
                            shutil.move(arquivo, destino) # move arquivo para o destino
                            print(f"Imagem movida para {destino}")
                            break

                    except FileNotFoundError:
                        print(f"Não foi possível encontrar {arquivo}")
                        break

                    except Exception as e:
                        print(f"Erro inesperado {e}")
                        break

                break