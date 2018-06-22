# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 22:41:22 2018

@author: jackj
"""
import numpy as np
import pandas as pd
import math
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
"""
Based on census bureau data, how much has the minority population grown over the last 18 years, 
from 2000 (focus on Asian Americans, Blacks, Hispanics and White) and predict the trend to 2040 for 
age groups (0-18, 19-34, 35-64, 65+) - please create a stacked bar chart per minority population
"""
class task_one:
    
    # data should be the one for each race group
    def __init__(self, data):
        self.input_data = data
        self.y0 = 1
    
    def logistic_regression(self, t, r, xm):
        output = xm / (1 +(xm/self.y0-1) * math.e**(-1*r*t))
        return output    
        
    def apply_logis(self, group, data_pred):
        group = int(group)
        sub_data = self.input_data[self.input_data.raceID == group]
        locations = pd.unique(sub_data.state)
        for location in locations:
            small_data = sub_data[sub_data.state == location]
            small_data = small_data.sort_values(by=['year'])
            if not small_data.empty:
                tmp = pd.DataFrame(columns = ['age18to34','age35to64','state','raceID','totalPopulation','under18','age65plus','year'])
                t = small_data.year - small_data.year.iloc[0]
                t_ = np.arange(0, 2031 - small_data.year.iloc[0])
                tmp.year = t_ + small_data.year.iloc[0]
                tmp.state = location
                tmp.raceID = group
                # under 18
                y = small_data.under18 // 1000
                self.y0 = y.iloc[0]
                init_vals = [0.2, 100]
                best_val, covar = curve_fit(self.logistic_regression, t, y, p0 = init_vals)
                y_ = self.logistic_regression(t_, best_val[0], best_val[1])
                tmp.under18 = y_
                
                # age 18 to 34
                y = small_data.age18to34 // 1000
                self.y0 = y.iloc[0]
                init_vals = [0.2, 100]
                best_val, covar = curve_fit(self.logistic_regression, t, y, p0 = init_vals)
                y_ = self.logistic_regression(t_, best_val[0], best_val[1])
                tmp.age18to34 = y_
                
                # age 35 to 64
                y = small_data.age35to64 // 1000
                self.y0 = y.iloc[0]
                init_vals = [0.2, 100]
                best_val, covar = curve_fit(self.logistic_regression, t, y, p0 = init_vals)
                y_ = self.logistic_regression(t_, best_val[0], best_val[1])
                tmp.age35to64 = y_
                
                # age 65+
                y = small_data.age65plus // 1000
                self.y0 = y.iloc[0]
                init_vals = [0.2, 100]
                best_val, covar = curve_fit(self.logistic_regression, t, y, p0 = init_vals)
                y_ = self.logistic_regression(t_, best_val[0], best_val[1])
                tmp.age65plus = y_
                
                # total population
                y = small_data.totalPopulation // 1000
                self.y0 = y.iloc[0]
                init_vals = [0.2, 100]
                best_val, covar = curve_fit(self.logistic_regression, t, y, p0 = init_vals)
                y_ = self.logistic_regression(t_, best_val[0], best_val[1])
                tmp.totalPopulation = y_
                
                #append tmp with predict table
                data_pred = data_pred.append(tmp, ignore_index=True)
            else:
                print('Empty dataframe met   ', location)
        
        return data_pred
    
    def task_one_output(self):
        data_pred = pd.DataFrame(columns = ['age18to34','age35to64','state','raceID','totalPopulation','under18','age65plus','year'])
        data_pred = self.apply_logis(1, data_pred)
        data_pred = self.apply_logis(3, data_pred)
        data_pred = self.apply_logis(5, data_pred)
        data_pred = self.apply_logis(31, data_pred)
        data_pred = self.apply_logis(400, data_pred)
        
        return data_pred
    
    
    def create_stack_bar_chart(self, data_group, group, title, name):
        task_1 = pd.DataFrame(columns = ['age18to34','age35to64','under18','age65plus'])
        
        data_ = data_group[data_group.raceID == group]
        data_ = data_[['under18', 'age18to34', 'age35to64', 'age65plus', 'year']]
        grouped = data_.groupby('year')
        task_1['under18'] = grouped['under18'].agg(np.sum)
        task_1['age18to34'] = grouped['age18to34'].agg(np.sum)
        task_1['age35to64'] = grouped['age35to64'].agg(np.sum)
        task_1['age65plus'] = grouped['age65plus'].agg(np.sum)
        
        ax = task_1[['under18','age18to34','age35to64','age65plus']].plot(kind='bar', stacked = True, title =title, figsize=(15, 10), legend=True, fontsize=12)
        ax.set_xlabel("Year", fontsize=12)
        ax.set_ylabel("Population (Unit in K)", fontsize=12)
#        plt.show()
        ax.figure.savefig(name)
        
    def heatmap(self, data_pred_, name, title):
        import seaborn as sns
        
        # heatmap
        data_pred_ = data_pred_[['year', 'state', 'totalPopulation']]
        # create pivot table
        piv = pd.pivot_table(data_pred_, values='totalPopulation',index=['state'], columns=['year'], fill_value=0)
        piv[piv<0] = 0
        #plot pivot table as heatmap using seaborn
        plt.figure(figsize = (16,10))
        ax = sns.heatmap(piv, cmap="YlGnBu")
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
        ax.set_title(title)
        plt.savefig(name)
        
    def get_estimated_percentage_increased(self, data_):
        states = pd.unique(data_.state)
        table = pd.DataFrame(columns = ['percentage'], index = states)
        for state in states:
            
            a = data_[data_.state == state]
#            a = a[a.year == 2005]['totalPopulation']
            a = a[a.year == a.sort_values(by=['year']).year.iloc[0]]['totalPopulation']
            b = data_[data_.state == state]
            b = b[b.year == 2030]['totalPopulation']
            table.loc[state, 'percentage'] = (b.iloc[0] - a.iloc[0]) / a.iloc[0]
        return table
            
         
    def get_sharing_percentage_table(self, data_pred):
        asian = data_pred[data_pred.raceID == 31]
        black = data_pred[data_pred.raceID == 5]
        hispanic = data_pred[data_pred.raceID == 400]
        white = data_pred[data_pred.raceID == 3]
        total = data_pred[data_pred.raceID == 1]
                
        years = pd.unique(data_pred.year)
        share_table = pd.DataFrame(columns = ['asian','black','hispanic','white'], index = years)

        grouped = asian.groupby('year')
        share_table['asian'] = grouped['totalPopulation'].agg(np.sum)
        
        grouped = black.groupby('year')
        share_table['black'] = grouped['totalPopulation'].agg(np.sum)
        
        grouped = hispanic.groupby('year')
        share_table['hispanic'] = grouped['totalPopulation'].agg(np.sum)
        
        grouped = white.groupby('year')
        share_table['white'] = grouped['totalPopulation'].agg(np.sum)
        
        grouped = total.groupby('year')
        total_population = grouped['totalPopulation'].agg(np.sum)
                  
        share_table['asian'] = share_table['asian'] / total_population
        share_table['black'] = share_table['black'] / total_population
        share_table['hispanic'] = share_table['hispanic'] / total_population
        share_table['white'] = share_table['white'] / total_population
        
        return share_table
            
             
