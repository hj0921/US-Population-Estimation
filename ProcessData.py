# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:26:50 2018

@author: Hao J.
"""

import pandas as pd
import numpy as np
    
class  ProcessData:   
    
    def __init__(self):
        self.label = ['Total population', 'Under 18 years','18 to 34 years','35 to 64 years','age 65 above']
#    label = ['Total population', 'Under 18 years','18 to 34 years','35 to 64 years','age 65 above']
    
        self.name = []
        self.name.append(['Estimate; TOTAL NUMBER OF RACES REPORTED - Total population', 
                     'Estimate; Total population'])
        self.name.append(['Estimate; Total population - SEX AND AGE - Under 18 years',
                     'Estimate; SEX AND AGE - Under 18 years',
                     'Estimate; SEX AND AGE - Total population - Under 18 years'])
        self.name.append(['Estimate; Total population - SEX AND AGE - 18 to 34 years',
                     'Estimate; SEX AND AGE - 18 to 34 years',
                     'Estimate; SEX AND AGE - Total population - 18 to 34 years'])
        self.name.append(['Estimate; Total population - SEX AND AGE - 35 to 64 years',
                     'Estimate; SEX AND AGE - 35 to 64 years',
                     'Estimate; SEX AND AGE - Total population - 35 to 64 years'])
        self.name.append(['Estimate; Total population - SEX AND AGE - 65 years and over',
                     'Estimate; SEX AND AGE - 65 years and over',
                     'Estimate; SEX AND AGE - Total population - 65 years and over'])
    
    def get_data_total_population(self):
        # 1 - all population
        data_total = {}
        data_useful_total = {}
        group = 1
        for i in range(5,17):
            year = str(i)
            if i < 10:
                year = '0'+ year
            if i <= 6:
                p_file = 'data/AllPopulation/all together/ACS_' + year + '_EST_S0201_with_ann.csv'
                label_file = 'data/AllPopulation/all together/ACS_' + year + '_EST_S0201_metadata.csv'
            else:
                p_file = 'data/AllPopulation/all together/ACS_' + year + '_1YR_S0201_with_ann.csv'
                label_file = 'data/AllPopulation/all together/ACS_' + year + '_1YR_S0201_metadata.csv'
            
            year = '20' + year
            inputdata= pd.read_csv(p_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
            read_index = [j+1 for j, ele in enumerate(inputdata[1:]['POPGROUP.id']) if int(ele) == group]
            data_total[year] = inputdata.iloc[read_index]
            
            inputlabel = pd.read_csv(label_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
            looking_table = {}
            for i in range(len(self.label)):
                lab = self.label[i]
                nam = self.name[i]
                tmp = inputlabel.loc[inputlabel.Id.isin(nam)]
                if (len(tmp)==1):
                    var = tmp.iloc[0, 0]
                    looking_table[lab] = var
                elif (len(tmp)==2):
                    var = tmp.iloc[0, 0]
                    looking_table[lab] = var
                else:
                    looking_table[lab] = 'Not Found'
                    print(str(len(tmp)) +' not found on year '+year+', in data_total dataset')
                    print(nam)
            
            data_useful_total[year] = data_total[year][['GEO.display-label','POPGROUP.id']]
            for key in self.label:
                data_useful_total[year][key] =data_total[year][looking_table[key]]
            data_useful_total[year]['age 65 above'] = pd.to_numeric(data_useful_total[year]['age 65 above']) * pd.to_numeric(data_useful_total[year]['Total population']) // 100
        return data_useful_total
    
    def get_data_asian_population(self):
        # 31 - Asian alone or in combination with one or more other races 
        data_asian = {}
        data_useful_asian = {}
        group = 31
        for i in range(5,17):
            index = str(i)
            if i < 10:
                index = '0'+ index
            year = '20' + index
            if i <= 6:
                p_file = 'data/asian/' + year + '/ACS_' + index + '_EST_S0201_with_ann.csv'
                label_file = 'data/asian/' + year + '/ACS_' + index + '_EST_S0201_metadata.csv'
            else:
                p_file = 'data/asian/' + year + '/ACS_' + index + '_1YR_S0201_with_ann.csv'
                label_file = 'data/asian/' + year + '/ACS_' + index + '_1YR_S0201_metadata.csv'
            
            inputdata= pd.read_csv(p_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
            read_index = [j+1 for j, ele in enumerate(inputdata[1:]['POPGROUP.id']) if int(ele) == group]
            data_asian[year] = inputdata.iloc[read_index]
            
            inputlabel = pd.read_csv(label_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
            looking_table = {}
            for i in range(len(self.label)):
                lab = self.label[i]
                nam = self.name[i]
                tmp = inputlabel.loc[inputlabel.Id.isin(nam)]
                if (len(tmp)==1):
                    var = tmp.iloc[0, 0]
                    looking_table[lab] = var
                elif (len(tmp)==2):
                    var = tmp.iloc[0, 0]
                    looking_table[lab] = var
                else:
                    looking_table[lab] = 'Not Found'
                    print(str(len(tmp)) +' not found on year '+year+', in data_asian dataset')
                    print(nam)
            
            data_useful_asian[year] = data_asian[year][['GEO.display-label','POPGROUP.id']]
            for key in self.label:
                data_useful_asian[year][key] =data_asian[year][looking_table[key]]
            data_useful_asian[year]['age 65 above'] = pd.to_numeric(data_useful_asian[year]['age 65 above']) * pd.to_numeric(data_useful_asian[year]['Total population']) // 100
        return data_useful_asian
    
    def get_data_black_population(self):
        # 5 - Black or African American alone or in combination with one or more other races
        group = 5
        data_black ={}
        data_useful_black = {}
        for i in range(5,17):
            index = str(i)
            if i < 10:
                index = '0'+ index
            year = '20' + index
            if i <= 6:
                p_file = 'data/black/' + year + '/ACS_' + index + '_EST_S0201_with_ann.csv'
                label_file = 'data/black/' + year + '/ACS_' + index + '_EST_S0201_metadata.csv'
            else:
                p_file = 'data/black/' + year + '/ACS_' + index + '_1YR_S0201_with_ann.csv'
                label_file = 'data/black/' + year + '/ACS_' + index + '_1YR_S0201_metadata.csv'
            
            inputdata= pd.read_csv(p_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
            read_index = [j+1 for j, ele in enumerate(inputdata[1:]['POPGROUP.id']) if int(ele) == group]
            data_black[year] = inputdata.iloc[read_index]
            
            inputlabel = pd.read_csv(label_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
            looking_table = {}
            for i in range(len(self.label)):
                lab = self.label[i]
                nam = self.name[i]
                tmp = inputlabel.loc[inputlabel.Id.isin(nam)]
                if (len(tmp)==1):
                    var = tmp.iloc[0, 0]
                    looking_table[lab] = var
                elif (len(tmp)==2):
                    var = tmp.iloc[0, 0]
                    looking_table[lab] = var
                else:
                    looking_table[lab] = 'Not Found'
                    print(str(len(tmp)) +' not found on year '+year+', in data_black dataset')
                    print(nam)
            
            data_useful_black[year] = data_black[year][['GEO.display-label','POPGROUP.id']]
            for key in self.label:
                data_useful_black[year][key] =data_black[year][looking_table[key]]
            data_useful_black[year]['age 65 above'] = pd.to_numeric(data_useful_black[year]['age 65 above']) * pd.to_numeric(data_useful_black[year]['Total population']) // 100
        return data_useful_black
    
    def get_data_hispanic_population(self):
        # 400 - Hispanic or Latino (of any race)
        group = 400
        data_hispanic = {}
        data_useful_hispanic = {}
        
        for i in range(5,17):
            index = str(i)
            if i < 10:
                index = '0'+ index
            year = '20' + index
            if i <= 6:
                p_file = 'data/hispanic/' + year + '/ACS_' + index + '_EST_S0201_with_ann.csv'
                label_file = 'data/hispanic/' + year + '/ACS_' + index + '_EST_S0201_metadata.csv'
            else:
                p_file = 'data/hispanic/' + year + '/ACS_' + index + '_1YR_S0201_with_ann.csv'
                label_file = 'data/hispanic/' + year + '/ACS_' + index + '_1YR_S0201_metadata.csv'
            
            inputdata= pd.read_csv(p_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
            read_index = [j+1 for j, ele in enumerate(inputdata[1:]['POPGROUP.id']) if int(ele) == group]
            data_hispanic[year] = inputdata.iloc[read_index]
            
            inputlabel = pd.read_csv(label_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
            looking_table = {}
            for i in range(len(self.label)):
                lab = self.label[i]
                nam = self.name[i]
                tmp = inputlabel.loc[inputlabel.Id.isin(nam)]
                if (len(tmp)==1):
                    var = tmp.iloc[0, 0]
                    looking_table[lab] = var
                elif (len(tmp)==2):
                    var = tmp.iloc[0, 0]
                    looking_table[lab] = var
                else:
                    looking_table[lab] = 'Not Found'
                    print(str(len(tmp)) +' not found on year '+year+', in data_hispanic dataset')
                    print(nam)
            
            data_useful_hispanic[year] = data_hispanic[year][['GEO.display-label','POPGROUP.id']]
            for key in self.label:
                data_useful_hispanic[year][key] =data_hispanic[year][looking_table[key]]
            data_useful_hispanic[year]['age 65 above'] = pd.to_numeric(data_useful_hispanic[year]['age 65 above']) * pd.to_numeric(data_useful_hispanic[year]['Total population']) // 100
        return data_useful_hispanic
    
        
    def get_data_white_population(self):
        # 3 - White alone or in combination with one or more other races
        group = 3
        data_white = {}
        data_useful_white = {}
        
        for i in range(5,17):
            index = str(i)
            if i < 10:
                index = '0'+ index
            year = '20' + index
            if i <= 6:
                p_file = 'data/white/' + year + '/ACS_' + index + '_EST_S0201_with_ann.csv'
                label_file = 'data/white/' + year + '/ACS_' + index + '_EST_S0201_metadata.csv'
            else:
                p_file = 'data/white/' + year + '/ACS_' + index + '_1YR_S0201_with_ann.csv'
                label_file = 'data/white/' + year + '/ACS_' + index + '_1YR_S0201_metadata.csv'
            
            inputdata= pd.read_csv(p_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
            read_index = [j+1 for j, ele in enumerate(inputdata[1:]['POPGROUP.id']) if int(ele) == group]
            data_white[year] = inputdata.iloc[read_index]
            
            inputlabel = pd.read_csv(label_file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
            looking_table = {}
            for i in range(len(self.label)):
                lab = self.label[i]
                nam = self.name[i]
                tmp = inputlabel.loc[inputlabel.Id.isin(nam)]
                if (len(tmp)==1):
                    var = tmp.iloc[0, 0]
                    looking_table[lab] = var
                elif (len(tmp)==2):
                    var = tmp.iloc[0, 0]
                    looking_table[lab] = var
                else:
                    looking_table[lab] = 'Not Found'
                    print(str(len(tmp)) +' not found on year '+year+', in data_white dataset')
                    print(nam)
            
            data_useful_white[year] = data_white[year][['GEO.display-label','POPGROUP.id']]
            for key in self.label:
                data_useful_white[year][key] =data_white[year][looking_table[key]]
            data_useful_white[year]['age 65 above'] = pd.to_numeric(data_useful_white[year]['age 65 above']) * pd.to_numeric(data_useful_white[year]['Total population']) // 100
        return data_useful_white
    
    def combine_two_data(self, table, data):
        # data is a dictionary, which keys are years
        for year in range(2005,2017):
            year = str(year)
            data_year = data[year]
            data_year['year'] = year
#            data_year.rename(index=str, columns={'POPGROUP.id':'raceID', 'GEO.display-label':'state','Under 18 years':'under18','18 to 34 years':'18to34', 
#                                                 '35 to 64 years':'35to64','age 65 above':'65plus', 'Total population':'totalPopulation'})
            table = table.append(data_year, ignore_index=True)
        
            
#            for i in range(1, len(data_year)+1):
#                try:
#                    tmp = data_year.loc[i,['POPGROUP.id', 'GEO.display-label', 'Under 18 years', '18 to 34 years','35 to 64 years','age 65 above', 'Total population']].tolist()
#                except:
#                    print('Error! The corresponding year and index is: ', year,i)
#                tmp.append(year)
#                d = pd.DataFrame(data = [tmp], columns = ['raceID', 'state', 'under18', '18to34', '35to64', '65plus', 'totalPopulation', 'year'])
#                table = table.append(d, ignore_index=True)
        return table
                
                
                
#                state = data_year.iloc[i, 0] #'GEO.display-label' located at (i,0)
#                # 1:7 is the race id, total population, 0-17, 18-34, 35-64, 65+
#                tmp = pd.DataFrame(data_year.iloc[i,1:7]).transpose() 
#                tmp['year'] = year
#                if state not in self.data:
#                    self.data[state] = tmp
#                else:
#                    self.data[state] = self.data[state].append(tmp)
#        return self.data
    
    def data_table(self):
        # get data
        data_asian = self.get_data_asian_population()
        data_black = self.get_data_black_population()
        data_hispanic = self.get_data_hispanic_population()
        data_white = self.get_data_white_population()
        data_total = self.get_data_total_population()
        # combine all data together
        table = pd.DataFrame(columns = ['POPGROUP.id', 'GEO.display-label','Under 18 years','18 to 34 years', 
                                        '35 to 64 years','age 65 above', 'Total population'])
#        ['raceID', 'state', 'under18', '18to34', '35to64', '65plus', 'totalPopulation', 'year']
        table = self.combine_two_data(table, data_asian)
        print('Asian data is combined successfully!')
        table = self.combine_two_data(table, data_black)
        print('Black data is combined successfully!')
        table = self.combine_two_data(table, data_hispanic)
        print('Hispanic data is combined successfully!')
        table = self.combine_two_data(table, data_white)
        print('White data is combined successfully!')
        table = self.combine_two_data(table, data_total)
        print('Total data is combined successfully!')
        table.columns = ['age18to34','age35to64','state','raceID','totalPopulation','under18','age65plus','year']
        table.age18to34 = pd.to_numeric(table.age18to34)
        table.age35to64 = pd.to_numeric(table.age35to64)
        table.raceID = pd.to_numeric(table.raceID)
        table.totalPopulation = pd.to_numeric(table.totalPopulation)
        table.under18 = pd.to_numeric(table.under18)
        table.age65plus = pd.to_numeric(table.age65plus)
        table.year = pd.to_numeric(table.year)
        
        
        
        print('---------------------------------------------------------')
        print('Please Note:')
        print('# 1 - all population ')
        print('# 31 - Asian alone or in combination with one or more other races' )
        print('# 5 - Black or African American alone or in combination with one or more other races')
        print('# 400 - Hispanic or Latino (of any race)')
        print('# 3 - White alone or in combination with one or more other races')
        return table
    
    
    
    
    
    
