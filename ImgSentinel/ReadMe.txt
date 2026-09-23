Image Sentinel
==============

Projeto de automação em Python para organizar arquivos de imagem automaticamente.

Resumo
-------
Image Sentinel monitora a pasta de Downloads e identifica arquivos de imagem quando eles são baixados. Assim que o arquivo termina de ser transferido e seu tamanho deixa de mudar, o script move o arquivo para a pasta de Pictures.

Este projeto foi desenvolvido como estudo prático sobre automação de tarefas no sistema operacional, monitoração de arquivos e organização de arquivos em fluxo de trabalho do dia a dia.

O que ele faz
-------------
- observa uma pasta específica em tempo real
- detecta criação de arquivos
- filtra extensões de imagem (.jpg, .jpeg, .png, .gif, .bmp, .tiff)
- aguarda o download terminar antes de mover o arquivo
- move o arquivo para uma pasta de destino definida

Tecnologias
-----------
- Python
- watchdog (monitoramento de eventos do sistema de arquivos)
- shutil (movimentação de arquivos)
- os (operações do sistema operacional)
- time (espera e sincronização)

Arquivos do projeto
-------------------
- ImgSentinel.py: inicia o monitoramento e mantém o observador ativo
- ImgHandler.py: contém a lógica de detecção e movimentação dos arquivos
- ImgSentinel.bat: arquivo batch para execução rápida no Windows
- ReadMe.txt: documentação do projeto

Como executar
-------------
1. Instale a dependência:
   pip install watchdog

2. Ajuste os caminhos no arquivo ImgHandler.py:
   - caminho = pasta monitorada (ex.: Downloads)
   - destino = pasta de destino (ex.: Pictures)

3. Execute o script:
   python ImgSentinel.py

4. Ou execute o arquivo .bat no Windows:
   ImgSentinel.bat

Estrutura do fluxo
------------------
1. O script inicia um observer para monitorar a pasta informada.
2. Quando um arquivo é criado, o handler recebe o evento.
3. O código espera alguns segundos para garantir que o download tenha sido concluído.
4. Verifica se a extensão do arquivo está na lista de imagens.
5. Caso esteja, move o arquivo para a pasta de destino.

Aplicação prática
------------------
Este projeto é um exemplo simples de automação orientada a produtividade. Ele ajuda a manter o ambiente de trabalho organizado sem exigir ação manual do usuário.

O mesmo conceito pode ser expandido para:
- mover arquivos por tipo (PDF, ZIP, documentos)
- separar arquivos por extensões
- organizar downloads por data ou categoria
- criar pastas automáticas com base em regras definidas

Portfolio / descrição profissional
----------------------------------
Image Sentinel é um projeto de automação em Python voltado para organização de arquivos no sistema operacional. O sistema monitora a pasta de Downloads e move automaticamente imagens para a pasta de Pictures assim que o arquivo é concluído. A solução foi construída com Python usando a biblioteca watchdog para observar alterações em tempo real, além de manipulação de arquivos com shutil e os. O projeto demonstra domínio de automação de processos, monitoramento de eventos do sistema e criação de ferramentas práticas para melhorar produtividade.


------------------------
English version
------------------------

Image Sentinel is a Python automation project designed to organize image files automatically.

Overview
--------
The system watches the Downloads folder and detects newly created image files. Once the file is fully downloaded and its size stops changing, the script moves it to the Pictures folder.

This project was created as a practical study of file-system automation, monitoring, and productivity-oriented scripting.

What it does
------------
- watches a target folder in real time
- detects created files
- filters image extensions (.jpg, .jpeg, .png, .gif, .bmp, .tiff)
- waits for the download to finish before moving the file
- moves the file to a configured destination folder

Tech stack
----------
- Python
- watchdog
- shutil
- os
- time

How to run
----------
1. Install dependency:
   pip install watchdog

2. Update the paths in ImgHandler.py:
   - caminho = monitored folder
   - destino = destination folder

3. Run:
   python ImgSentinel.py

4. On Windows, you can also use:
   ImgSentinel.bat

Portfolio-ready description
---------------------------
Image Sentinel is a Python automation project that monitors a download directory and automatically moves image files to the Pictures folder. Built using the watchdog library and standard Python file-management modules, the project demonstrates practical automation for organizing files and reducing manual work. It highlights skills in system monitoring, event-driven programming, and task automation for everyday productivity scenarios.
