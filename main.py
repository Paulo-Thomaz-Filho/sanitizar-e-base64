# Inports
from pathlib import Path
from PIL import Image
import base64
import json

# Paths
pathRoot   = Path(__file__).resolve().parent
pathInput  = pathRoot / 'input'
pathOutput = pathRoot / 'output'
pathDb     = pathRoot / 'db.json'

# Garante a existencia das pastas
pathInput.mkdir(exist_ok=True)
pathOutput.mkdir(exist_ok=True)

# Garante que o arquivo db.json exista e carrega os dados
if not pathDb.exists() or pathDb.stat().st_size == 0:
    with open(pathDb, mode = 'w', encoding = 'utf-8') as JSON:
        json.dump([], JSON)

# Carregar O Banco de Dados
with open(pathDb, mode = 'r', encoding = 'utf-8') as JSON:
    DB = json.load(JSON)

# ====== Defs ======

# Logica principal
def ProcessarImagens(ConverterPara64):
    # Pegar todas os arquivos do tipo .png
    Imagens = list(pathInput.glob('*.png'))
    if not Imagens:
        return 'Nenhuma imagem PNG encontrada'

    # Sanetiza a imagem
    for Imagem in Imagens:
        url = Sanitizar(Imagem)
        if url is None:
            continue

        # Converter imagem
        img64 = None
        if ConverterPara64 == True:
            img64 = ConveterB64(url)
        
        # Salvar imagem
        SalvarNoDb(url, img64)

# Limpa os metadados
def Sanitizar(url):
    # Verifica se o png é realmente um png
    with open(url, mode = 'rb') as arquivo:
        header = arquivo.read(8)
    if header != b'\x89PNG\r\n\x1a\n':
        print(f'Arquivo invalido | Este arquivo não era um png - indentificador({header})')
        return None

    # Limpa os metadados
    ImagemPil = Image.open(url)
    ImagemPil.info.clear()

    # Salvar na pasta de Output
    PathSave = pathOutput / url.name
    ImagemPil.save(PathSave) 
    return PathSave
    
# Converte para base 64
def ConveterB64(url):
    with open(url, mode = 'rb') as Arquivo:
        Dados = Arquivo.read()
        Img64 = base64.b64encode(Dados).decode('utf-8')
    
    return Img64

# Salva os dados das imagens no banco de dados
def SalvarNoDb(url, img64):
    
    DadosJson = {
        'nome'   : url.name,
        'url'    : str(url),
        'base64' : img64,
    }

    DB.append(DadosJson)
    with open(pathDb, mode = 'w', encoding = 'utf-8') as Arquivo:
        json.dump(DB, Arquivo, indent=4, ensure_ascii=False)
    return 'Sucesso ao salvar a imagem'

ProcessarImagens(True)