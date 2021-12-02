import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def bat(*file_locatoin):
    for current_file in file_locatoin:
        db = pd.read_csv(current_file, low_memory=False)
        plt.style.use(['dark_background'])
        
        element = 'BAT' # 'BAT' Element to search in the FMT coulum

        bool_is_element = db['FMT']==element 
        new_db_by_element = db[bool_is_element] #new DB with the desirable element

        old_column1_name = new_db_by_element.columns[1]
        old_column4_name = new_db_by_element.columns[4]
        new_column1_name = 'Time'
        new_column4_name = 'Volt'
        
        # Rename columns and fitler by
        new_db_by_element.rename(columns={old_column1_name:new_column1_name,old_column4_name:new_column4_name}, inplace=True)
        filterd_db = new_db_by_element.filter(items=['Time','Volt'])
        filterd_db['Time'] = pd.to_datetime(filterd_db['Time']) #STR to datetime variable 
        filterd_db['Volt'] = filterd_db['Volt'].astype(float) #STR to float variable 

        plt.plot(filterd_db['Time'], filterd_db['Volt'])
    plt.show()

#Change files direction to the correct CSV file
file_direction1 = (r'C:\Users\output.csv')
file_direction2 = (r'C:\Users\output.csv')

bat(file_direction1,file_direction2)