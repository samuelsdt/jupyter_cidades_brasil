# Mapa do Brasil por Cidades no Jupyter
Mapa coroplético com as cidades brasileiras para visualização no Jupyter Notebook usando ipyleaflet.

## Instalação 

pip install git+git://github.com/samuelsdt/jupyter_cidades_brasil

## Uso 

from brlcities import brlmap, linear

mapa = brlmap(data, pattern="cod", title="", colormap = linear.YlOrBr_04, legendPosition = "bottomright", style={'fillOpacity': 1, 'dashArray': '5, 5'})

### Parâmetros:  

-> data = dicionario de dados usado para o carregamento de dados, sendo a chave o identificador do munícipio e o respectivo valor para plotagem. O identificador de munícipio pode ser:  
- Código IBGE do munícipio;  
- Nome do munícipio e UF;

-> pattern = modo como está descrito a identificação do município na chave, por exemplo se na chave está como nome + "/" + UF o pattern é igual a "nome/uf", se está como UF + "-" + nome, o pattern é "uf-nome", caso use o código IBGE o pattern é apenas "cod" (default = "cod")

-> title = título do mapa (default = "") 

-> colormap = mapa de cores para a plotagem do mapa (default = linear.YlOrBr_04)

-> legendPosition = posição da legenda (default = "bottomright")

-> style = estilo da linha de divisa dos munícipios (default = {'fillOpacity': 1, 'dashArray': '5, 5'})
