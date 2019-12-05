'''
Created on 3 de dez de 2019
@author: Samuel
'''
import ipyleaflet 
import json 
import re
from ipywidgets import Layout, Box, HTML, widgets
from branca.colormap import linear
from ipyleaflet import WidgetControl

__data = None

def brlmap(data, pattern="cod", title="", colormap = linear.YlOrBr_04, legendPosition = "bottomright", style={'fillOpacity': 1, 'dashArray': '5, 5'}):
    geo_json_data = __finddictcities(data.keys(), pattern)
    key_max = max(data.keys(), key=(lambda k: data[k]))
    key_min = min(data.keys(), key=(lambda k: data[k]))
    centerX = (geo_json_data["bounds"][0]+geo_json_data["bounds"][2])/2
    centerY = (geo_json_data["bounds"][1]+geo_json_data["bounds"][3])/2
    escala = {1 : 360,2 : 180,3 : 90,4 : 45,5 : 22.5,6 : 11.25,7 : 5.625,8 : 2.8125,9 : 1.40625,10 : 0.703125,11 : 0.3515625,12 : 0.17578125,13 : 0.087890625,14 : 0.0439453125,15 : 0.02197265625,16 : 0.010986328125,17 : 0.0054931640625}
    difX = abs(geo_json_data["bounds"][2]-geo_json_data["bounds"][0])
    difY = abs(geo_json_data["bounds"][3]-geo_json_data["bounds"][1])
    if(difY>difX):
        maiordif = difY*1.5
    else:
        maiordif = difX
    ind=17
    while (escala[ind]<maiordif):
        ind-=1
    m = ipyleaflet.Map(center = (centerY,centerX), zoom = ind)
    
    global __data
    __data = data
    layer = ipyleaflet.Choropleth(
        geo_data=geo_json_data,
        choro_data=data,
        colormap=colormap, 
        border_color='black',  
        style=style
    )
    legend=colormap.scale(data[key_min],data[key_max])
    out = widgets.Output()
    with out:
        display(legend)
      
    m.add_layer(layer)
    stylesheets = HTML('''
        <style>
        .rigthlgd svg{
            float: right;
        }
        
        .rigthlgd{
            float: right;
            text-align: right;
        }
        .hiddenTitle
        {
           display: none;
        }
        </style>
    ''')
    elemTitle = HTML('''
        <h3 style="text-align: center;">''' + 
          title 
        + '''</h3>
    ''')
    if(title==""):
        elemTitle.add_class("hiddenTitle")
        
    global labelDados
    labelDados = HTML('<h4><h4>')

    labelDados.layout.padding = '2px';
    labelDados.layout.width = '47%';
    
    box_legenda = Layout(display='flex',
                    flex_flow='row',
                    align_items='stretch',
                    width='100%')

        
    if(legendPosition.find("right")>=0):
        out.add_class("rigthlgd")
        boxLgnd = Box(children=[labelDados, out,stylesheets], layout=box_legenda)
    else:
        labelDados.add_class("rigthlgd")
        boxLgnd = Box(children=[out, labelDados,stylesheets], layout=box_legenda)
    
    box_layout = Layout(display='flex',
                    flex_flow='column',
                    align_items='stretch',
                    width='100%')
    
    
    layer.on_hover(__update_html)
    
    
    if(legendPosition.find("bottom")>=0):
        box = Box(children=[elemTitle, m, boxLgnd], layout=box_layout)
    else:
        box = Box(children=[elemTitle, boxLgnd,m], layout=box_layout)
    return box

def __update_html( **kwargs):
        labelDados.value = kwargs["properties"]["nome"] + "/" + kwargs["properties"]["uf"] + ": " +  str(__data[kwargs["id"]])
    
def __finddictcities(ks, pattern):
    ret = {}
    ret["type"] = "FeatureCollection"
    ret["features"] = []
    patterns= [r'[^a-zA-Z0-9 ]+']
    for p in patterns:
        match= re.findall(p, pattern)
    spl = "".join(match)
    seg=[]
    if(spl==""):
        seg.append(pattern.lower())
    else:
        seg = pattern.lower().split(spl)
    json_data = json.load(open('data.geo.json')) 
    bds = [181,181,-181,-181]
    for k in ks:
        t=[]
        if(spl==""):
            t.append(k)
        else:
            t = k.split(spl)
        if(len(t)==len(seg)):
            for dic in json_data["features"]:
                enc = True
                i=0
                while ((i<len(seg)) & (enc)):
                    if(dic["properties"][seg[i]].lower() != t[i].lower()):
                        enc = False
                    i+=1
                if(enc):
                    tmp = {}
                    tmp["type"] = "Feature"
                    tmp["id"] = k
                    tmp["properties"] = dic["properties"]
                    tmp["geometry"] = dic["geometry"]
                    ret["features"] .append(tmp)
                    if(float(dic["properties"]["bounds"][0])<bds[0]):
                        bds[0] = float(dic["properties"]["bounds"][0])
                    if(float(dic["properties"]["bounds"][1])<bds[1]):
                        bds[1] = float(dic["properties"]["bounds"][1])
                    if(float(dic["properties"]["bounds"][2])>bds[2]):
                        bds[2] = float(dic["properties"]["bounds"][2])   
                    if(float(dic["properties"]["bounds"][3])>bds[3]):
                        bds[3] = float(dic["properties"]["bounds"][3])
                    break;
    ret["bounds"] = bds
    return ret
