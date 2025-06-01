from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from typing import List

caminho: str = r"C:\Users\Gustavo H. Valadares\Downloads"  
destino: str = r"C:\Users\Gustavo H. Valadares\Pictures" 
extensoes_img: List[str] = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}
 
observer = Observer() # objeto para o obsever
handler = FileSystemEventHandler() # objeto para o handler

observer.schedule(handler, caminho, recursive=False) # recursive vai decidir se as subpastas do meu caminha serão monitoradas também, como está em False não será


