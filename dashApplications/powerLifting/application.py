
# The following application when zipped with the requirements.txt file can be uploaded directly to elastic beanstalk on AWS and will generate a basic x,y scatterplot colored by gender.
# To get this working on local host will require some changes to the code below. 
# I may add in the alternate code in comments later for those interested in running this locally.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from random import randint

app = dash.Dash(__name__)
application = app.server


url = 'http://www.openpowerlifting.org/static/data/openpowerlifting.csv?' + str(randint(0, 1000))

def readData(dataurl):
    return pd.read_csv(dataurl).sample(n=10000)

df = readData(url)

markdown_text = '''
### OpenPowerLifting - Basic ScatterPlot

The above chart simply takes a random sample of 1000 from the openpowerlifting data set and 
plots the weight (x-axis) of the athletes vs the age (x-axis) of the athletes.

Data available at: http://www.openpowerlifting.org/static/data/openpowerlifting.csv

'''

#Reloading the data everytime has the downside of causing larger loading on server.

def serve_layout():
    url = 'http://www.openpowerlifting.org/static/data/openpowerlifting.csv?' + str(randint(0, 1000))
    df = readData(url)
    return html.Div([ dcc.Graph(id='life-exp-vs-gdp',figure={ 'data': [go.Scatter(x=df[df['Sex'] == i]['Age'],y=df[df['Sex'] == i]['BodyweightKg'],mode='markers',opacity=0.7,marker={'size': 15,'line': {'width': 0.5, 'color': 'white'}},name=i) for i in df.Sex.unique()],'layout': go.Layout(xaxis={'title': 'Age'},yaxis={'title': 'Body Weight (Kg)'},margin={'l': 40, 'b': 40, 't': 10, 'r': 10},legend={'x': 0, 'y': 1},hovermode='closest')}),dcc.Markdown(children=markdown_text)])

app.layout = serve_layout

if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
