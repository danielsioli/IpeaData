# IpeaData
Pacote para obter dados do IpeaData baseado em https://github.com/ipea/pyIpeaData.
Não consegui contato com o autor original, então criei esse projeto separado.

## Install 

```
pip install ipeaData
```

## Use
Importar pacote
```
import pyIpeaData as ipea
```
Obter dados de uma série
```
ipea.get_serie('ADMIS')
```
Listar séries disponíveis
```
ipea.get_metadados()
```
Obter informações sobre uma série (usar campo SERCODIGO)
```
ipea.get_metadados('ADMIS')
```
Listar Temas das séries
```
ipea.get_temas()
```
Obter informações sobre um Tema (usar campo TEMCODIGO)
```
ipea.get_temas(28) #Agropecuária
```
Listar Páises das séries
```
ipea.get_paises()
```
Obter informações sobre um Pais (usar campo PAICODIGO)
```
ipea.get_paises('BRA') #Brasil
```
Listar Territórios das séries
```
ipea.get_territorios()
```
Obter informações sobre um Território (usar campo TERCODIGO e NIVNOME)
```
ipea.get_territorios('1100015','Municípios') #Alta Floresta D'Oeste
```
Listar Fontes das séries
```
ipea.get_fontes()
```
## API Ipea Data

http://ipeadata.gov.br/api/
