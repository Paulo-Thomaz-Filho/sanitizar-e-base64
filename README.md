# 🖼️ Sanitizador e Conversor de Imagens PNG

> Ferramenta em Python para limpeza de metadados, validação de segurança de arquivos PNG e conversão automatizada para Base64.

[![Python Version](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pillow](https://img.shields.io/badge/Pillow-Image_Processing-11557c?logo=python&logoColor=white)](https://python-pillow.org/)
[![JSON](https://img.shields.io/badge/JSON-Data-000000?logo=json&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Sobre o Projeto e Funcionalidades

O Sanitizador e Conversor de Imagens é um script de automação focado na higienização e preparação de arquivos de imagem do tipo PNG. Desenvolvido em Python, o sistema inicia seu ciclo de vida garantindo a integridade do ambiente, criando as pastas necessárias e inicializando o arquivo `db.json` caso não existam. O motor principal da aplicação busca todos os arquivos `.png` depositados na pasta de entrada e os submete a uma rigorosa verificação de segurança.

Para garantir que arquivos maliciosos não se passem por imagens, o sistema não confia apenas na extensão do arquivo. Ele abre cada imagem em modo binário e realiza uma validação do "Magic Number", lendo os 8 primeiros bytes para assegurar que a assinatura hexadecimal corresponde exatamente ao cabeçalho padrão de um arquivo PNG autêntico (`b'\x89PNG\r\n\x1a\n'`). Arquivos forjados são imediatamente rejeitados e notificados no console.

Uma vez validada, a imagem passa pelo processo de sanitização através da biblioteca **Pillow (PIL)**, que limpa todos os metadados ocultos do arquivo (como informações de geolocalização ou dados do dispositivo). A imagem limpa é então salva em um diretório de saída seguro. Opcionalmente, o sistema encodifica a imagem higienizada para uma string no formato **Base64**. Por fim, um registro contendo o nome do arquivo, seu novo caminho de diretório e sua respectiva string codificada é catalogado e estruturado no banco de dados local `db.json`.

## 📁 Estrutura do Repositório

A arquitetura do projeto foi desenhada para ser minimalista e separar claramente o processamento, as fontes e os artefatos gerados.

Na raiz do diretório, encontra-se o motor da aplicação, o arquivo `main.py`. Ao lado dele, o arquivo `db.json` atua como um catálogo persistente de todas as imagens que foram processadas com sucesso. O fluxo de dados ocorre entre dois diretórios principais: a pasta `input/`, que atua como a área de recebimento das imagens originais e sujas, e a pasta `output/`, que atua como o cofre final contendo apenas as imagens higienizadas e seguras.

## 🛠️ Instalação e Configuração

Para executar este sanitizador, o ambiente requer o interpretador Python instalado. Como o projeto lida com manipulação avançada de imagens, é necessário instalar a biblioteca externa responsável por esse processamento.

Primeiro, clone o repositório ou faça o download dos arquivos para sua máquina local. No terminal, navegue até a raiz do projeto e instale a dependência de processamento de imagens Pillow:

```bash
pip install Pillow
