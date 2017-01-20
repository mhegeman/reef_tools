
# coding: utf-8

# In[ ]:

#import bokeh modules for interactive plotting
import numpy as np
import pandas as pd

from bokeh.charts import Bar, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import HoverTool, BoxZoomTool, PanTool, SaveTool
from bokeh.palettes import Spectral11

#to show charts inline
#from bokeh.io import push_notebook, show, output_notebook
#output_notebook()


# In[ ]:

#data
def reefBoatCount():
    sourceData = pd.read_csv("C:/Users/maalbino/Documents/project_dev/reef_tools/ReefsAerialSurvey_boatcount.csv")
    sourceData['Date'] = pd.to_datetime(sourceData['Date'], format='%m/%d/%Y')
    sourceData.rename(columns={'Number of Boats':'NumberOfBoats','Reef ':'Reef', 'Boat Type':'BoatType'},inplace=True)
    return sourceData
#get source data
#read data to dataframe    
boatCount = reefBoatCount()
boatCount['Year'] = boatCount.Date.map(lambda x: x.year)
source=ColumnDataSource(boatCount)

#create a palette with a number of colors equal to the number of reef locations
numbars = len(boatCount.groupby('Reef',as_index=False).sum().Reef)
mypalette = Spectral11[0:numbars]



# In[ ]:

#organize data by reef
byReef = boatCount.groupby(['Reef'],as_index=False).sum()
#set up chart tools
hover = HoverTool()
hover.tooltips = [("Boats", "@height")]
myTools = [BoxZoomTool(), PanTool(), SaveTool(), hover]

#Create bar chart by reef
chartByReef = Bar(byReef, values='NumberOfBoats', label='Reef', title='Total Number of Boats Observed by Reef',
      color='#66c2a5', tools=myTools, legend=False, plot_width=400, plot_height=400)
#show(chartByReef)


# In[ ]:

#organize data by Year
byYear = boatCount.groupby('Year', as_index=False).sum()
byYear.sort_values('Year', inplace=True)

#set up chart tools
hover = HoverTool()
hover.tooltips = [("Year","@x"),
                 ("Boats", "@top"),]
myTools = [BoxZoomTool(), PanTool(), SaveTool(), hover]

#create bar chart by year
chartByYear = figure(background_fill_color='white', plot_width=400, plot_height=400,
                         title='Total Number of Boats Observed by Year (1995-2015)',tools=myTools)
chartByYear.vbar(x=byYear['Year'], bottom=0, top=byYear['NumberOfBoats'], width=0.5, color='#66c2a5')
chartByYear.xaxis.axis_label = "Year"
chartByYear.yaxis.axis_label = "Boat Counts"


# In[ ]:

#from bokeh.layouts import row
#show(row(chartByYear, chartByReef))


# In[ ]:

#create tabbed report
from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.plotting import figure

output_file("C:/Users/maalbino/Documents/project_dev/reef_tools/report_test1.html")

tab1 = Panel(child=chartByYear, title="Years")
tab2 = Panel(child=chartByReef, title="Reef")

tabs = Tabs(tabs=[tab1, tab2])
show(tabs)


# In[ ]:




# In[ ]:



