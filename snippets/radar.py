##################################################
# radar.py uses the plotly library
# The concept developed here plots values from an
# analytical observation vs the mean and mean +/-
# 3 standard deviations (upper and lower control
# limits for a single observation across many values.
# The intended use is in the comparison of analytical
# samples in comparison to historical data to ensure
# sample matches expected behaviour. The data should
# be normalised to the ucl and lcl values and scaled
# so the ucl and lcl values are 20 and 10 respectively.
# This means if a sample is 'good' or 'comparable, the 
# radar profile will take a circular shape. While a sample
# with results which are atypical will result in a 
# skewed/distorted shape. However, while I describe
# a specific application, the concept can be deployed in
# a variety of situations.
#
# MIT License
# Please attribute: kevinbolger
##################################################

import plotly.graph_objs as go
from plotly.offline import plot

# Defining a function which templates my radar charts for me.
def myRadar(r, theta, name, fill = 'toself', color = 'blue', subplot = 'polar', dash = 'solid'):
    fig = go.Scatterpolar(
        r = r,
        theta = theta,
        fill = fill,
        name = name,
        line =  dict(
            shape = 'spline',
            smoothing = 1.3,
            color = color,
            dash = dash 
        ),
        subplot = subplot
    )
    return fig

values = [10.1, 14, 17, 16, 19.9, 14, 10.1]
ucl = [20, 20, 20, 20, 20, 20, 20]
lcl = [10, 10, 10, 10, 10, 10, 10]
mean = [15, 15, 15, 15, 15, 15, 15]
params = ['x1','x2','x3', 'x4', 'x5', 'x6','x7']


data = [
    myRadar(values,params,'values','toself','blue', 'polar', 'solid'),
    myRadar(values,params,'log_values','toself','blue', 'polar2', 'solid'),
    myRadar(ucl,params,'ucl','none','red','polar', 'dash'),
    myRadar(lcl,params,'lcl','none','red', 'polar', 'dash'),
    myRadar(mean,params,'mean','none','green', 'polar', 'dash'),
    myRadar(ucl,params,'log_ucl','none','red', 'polar2', 'dash'),
    myRadar(lcl,params,'log_lcl','none','red', 'polar2', 'dash'),
    myRadar(mean,params,'log_mean','none','green', 'polar2', 'dash')
]

layout = {
  "autosize": True, 
  "polar": {
    "radialaxis": {
      "autorange": True, 
      "range": [0,25], 
      "type": "linear"
    },
  'domain': {
    'x': [0, .42],
    'y': [0, 1]},
  }, 
  "polar2": {
    "radialaxis": {
      "autorange": True,
      "type": "log"
  },
  'domain': {
    'x': [0.58, 1],
    'y': [0, 1]},
  }
}

plot(go.Figure(data=data,layout = layout))
