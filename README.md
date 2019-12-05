# Mapa do Brasil por Cidades para Jupyter Notebook
Mapa coroplético com as cidades brasileiras para visualização no Jupyter Notebook usando ipyleaflet.

## Instalação 

pip install git+git://github.com/samuelsdt/jupyter_cidades_brasil

## Uso 

from brlcities import brlmap, linear

mapa = brlmap(data, pattern="cod", title="", colormap = linear.YlOrBr_04, legendPosition = "bottomright", style={'fillOpacity': 1, 'dashArray': '5, 5'})

### Parâmetros:  

- **data** = dicionario de dados usado para o carregamento dos dados no mapa, sendo a chave o identificador do munícipio e o respectivo valor para plotagem. O identificador de munícipio pode ser: Código IBGE do munícipio; Nome do munícipio e UF;

- **pattern** = modo como está descrito a identificação do município na chave, o nome do múnicipio é identificado pela string "nome" e a UF é identificada pela string "uf", por exemplo, se na chave está "<nome do município>/<UF>" o pattern é igual a "nome/uf", se está como "<uf>-<nome>", o pattern é "uf-nome", a posição do nome e da UF são intercambiáveis, pode ser utilizado qualquer caractere não alfanumérico como separador, porém é necessário especificá-lo no pattern. Caso use o código IBGE o pattern é apenas "cod" (parâmetro opcional, default = "cod")

- **title** = título do mapa (parâmetro opcional, default = "") 

- **colormap** = mapa de cores para a plotagem do mapa (parâmetro opcional, default = linear.YlOrBr_04)

- **legendPosition** = posição da legenda (parâmetro opcional, default = "bottomright")

- **style** = estilo da linha de divisa dos munícipios (parâmetro opcional, default = {'fillOpacity': 1, 'dashArray': '5, 5'})
