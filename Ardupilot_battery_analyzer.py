import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def bat(*file_locatoin):
    for current_file in file_locatoin:
        db = pd.read_csv(current_file, low_memory=False)
        plt.style.use(['dark_background'])

        element = 'BAT'

        bool_is_element = db['FMT']==element
        new_db_by_element = db[bool_is_element]

        old_column_name1 = new_db_by_element.columns[1]
        old_column_name4 = new_db_by_element.columns[4]
        new_column_name1 = 'Time'
        new_column_name4 = 'Volt'

        new_db_by_element.rename(columns={old_column_name1:new_column_name1,old_column_name4:new_column_name4}, inplace=True)
        filterd_db = new_db_by_element.filter(items=['Time','Volt'])
        filterd_db['Time'] = pd.to_datetime(filterd_db['Time'])
        filterd_db['Volt'] = filterd_db['Volt'].astype(float)

        time_db = filterd_db['Time']
        volt_db = filterd_db['Volt']
        plt.plot(time_db, volt_db)
    plt.show()

new_list = [r'C:\Users\Or\VSC\test\output.csv', r'C:\Users\Or\VSC\test\output1.csv']
bat(r'C:\Users\Or\VSC\test\output1.csv',r'C:\Users\Or\VSC\test\output.csv')