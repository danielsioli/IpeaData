# IpeaData
Pacote para obter dados do IpeaData

## Install 

```
pip install ipeaData
```

## Use
Importar pacote
```
from ipeaData import ipeadata
```
Obter dados de uma série
```
ipeadata.get_serie('ADMIS')
```
Listar séries disponíveis
```
ipeadata.get_metadados()
```
Obter informações sobre uma série (usar campo SERCODIGO)
```
ipeadata.get_metadados('ADMIS')
```
Listar Temas das séries
```
ipeadata.get_temas()
```
Obter informações sobre um Tema (usar campo TEMCODIGO)
```
ipeadata.get_temas(28) #Agropecuária
```
Listar Páises das séries
```
ipeadata.get_paises()
```
Obter informações sobre um Pais (usar campo PAICODIGO)
```
ipeadata.get_paises('BRA') #Brasil
```
Listar Territórios das séries
```
ipeadata.get_territorios()
```
Obter informações sobre um Território (usar campo TERCODIGO e NIVNOME)
```
ipeadata.get_territorios('1100015','Municípios') #Alta Floresta D'Oeste
```
Listar Fontes das séries
```
ipeadata.get_fontes()
```
## API Ipea Data

http://ipeadata.gov.br/api/
