import json 
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

filename = "data/readable_all_month.json"
with open(filename) as f:
	data = json.load(f)

earthquake_list = data['features']

magnitudes = [eq['properties']['mag'] for eq in earthquake_list]
longitude = [eq['geometry']["coordinates"][0] for eq in earthquake_list]
latitude = [eq['geometry']["coordinates"][1] for eq in earthquake_list]
hover_text = [f"Magnitude= {eq['properties']['mag']} Location= {eq['properties']['place']}" for eq in earthquake_list] 

my_layout = Layout({'title':data['metadata']["title"]})

data = [{
	'type':'scattergeo',
	'lat':latitude,
	'lon':longitude,
	'text':hover_text,
	'marker':
	{
	'size': [abs(2*mag) for mag in magnitudes],
	'color':magnitudes,
	'colorscale':'Rainbow',
	'reversescale':True,
	'colorbar':{'title':'Magnitudes'}
	}	

}]
fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename = "All_Month_Earthquakes.html")