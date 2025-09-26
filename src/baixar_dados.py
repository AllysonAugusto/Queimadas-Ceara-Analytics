import pandas as pd
import requests
import zipfile
import os

  #Baixar dados
def baixar_dados_ce(ano, pasta_raiz="dados_ceara"):
  url = f"https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/anual/EstadosBr_sat_ref/CE/focos_br_ce_ref_{ano}.zip"
  print(f"Baixando dados do ano {ano}...")

  try:
    resposta = requests.get(url, stream=True)
    resposta.raise_for_status()
  except requests.RequestException as e:
    print(f"Erro ao baixar dados do ano {ano}: {e}")
    return None

#Salvar zip

  try:
    os.makedirs(pasta_raiz, exist_ok = True)
    zip_path = os.path.join(pasta_raiz, f"focos_br_ce_ref_{ano}.zip")
    with open(zip_path, "wb") as f:
      for chunk in resposta.iter_content(chunk_size=8192):
        f.write(chunk)

    print(f"Dados do ano {ano} baixados.")
  except OSError as e:
    print(f"Erro ao salvar o arquivo zip: {e}")
    return None
    
#Extrair todos os arquivos do zip
  try:
    with zipfile.ZipFile(zip_path, "r") as z:
      z.extractall(pasta_raiz)
      print(f"Todos os arquivos extraidos em: {pasta_raiz}")
  except zipfile.BadZipFile as e:
    print("Erro: Zip corrompido")
    return None
  except Exception as e:
    print(f"Erro ao extrair ZIP:{e}")
    return None
  
  return pasta_raiz



pasta = baixar_dados_ce(2023)
if pasta:
  print("Download e extracao concluidos com sucesso")
