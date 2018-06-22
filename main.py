# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:41:21 2018

@author: Hao J.
"""
from ProcessData import ProcessData
from task import task_one
# get the data
ps = ProcessData()
data = ps.data_table()
data.to_csv('data_table.csv')

"""
Based on census bureau data, how much has the minority population grown over the last 18 years, 
from 2000 (focus on Asian Americans, Blacks, Hispanics and White) and predict the trend to 2030 for 
age groups (0-18, 19-34, 35-64, 65+) - please create a stacked bar chart per minority population
"""
t1 = task_one(data)
data_pred = t1.task_one_output()

# get the plot stacked chart
# Asian
title = 'Asian alone or in combination with one or more other races'
group, name = 31, 'Asian_stacked_bar_chart.png'
t1.create_stack_bar_chart(data_pred, group, title, name)

# Black
title = 'Black or African American alone or in combination with one or more other races'
group, name = 5, 'Black_stacked_bar_chart.png'
t1.create_stack_bar_chart(data_pred, group, title, name)

# Hispanic
title = 'Hispanic or Latino (of any race)'
group, name = 400, 'Hispanic_stacked_bar_chart.png'
t1.create_stack_bar_chart(data_pred, group, title, name)

# White
title = 'White alone or in combination with one or more other races'
group, name = 3, 'White_stacked_bar_chart.png'
t1.create_stack_bar_chart(data_pred, group, title, name)


"""
Create a heat map of which states will feel the biggest demographic shifts in 
the above minority populations and what is the estimated percentage increase 
in these 3 minority demographics from 2005(probably 2006 or 2007, it depends 
on the data) to 2030 (table is fine to show percentage increase per minority 
population)
"""
# Asian heatmap
data_pred_ = data_pred[data_pred.raceID == 31]
t1.heatmap(data_pred_, 'AsianHeatMap.png', 'Asian HeatMap')
Est_increase_table_asian = t1.get_estimated_percentage_increased(data_pred_)

data_pred_ = data_pred[data_pred.raceID == 31]
data_pred_ = data_pred_[data_pred_ != 'California']
t1.heatmap(data_pred_, 'AsianHeatMap_NoCA.png', 'Asian HeatMap, without California')

# Black
data_pred_ = data_pred[data_pred.raceID == 5]
t1.heatmap(data_pred_, 'BlackHeatMap.png', 'Black Or African American HeatMap')
Est_increase_table_black = t1.get_estimated_percentage_increased(data_pred_)

# Hispanic
data_pred_ = data_pred[data_pred.raceID == 400]
t1.heatmap(data_pred_, 'HispanicHeatMap.png', 'Hispanic HeatMap')
Est_increase_table_hispanic = t1.get_estimated_percentage_increased(data_pred_)

"""
From 2005 to 2030, show a table that depicts the % share of Whites, 
Asian Americans, Blacks, and Hispanics in the US population per year
"""
share_table = t1.get_sharing_percentage_table(data_pred)
