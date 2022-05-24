'''
This library holds the function for acquiring data from the CodeUp DB Server.
'''


import pandas as pd
import os
import env

def get_db_url(db_name):
    url = f'mysql+pymysql://{env.username}:{env.password}@{env.host}/{db_name}'
    return url

def get_telco_data():
    '''
    This acquires all customer data from telco_churn.  If it already exists, the function
    loads the pre-downloaded csv into the notebook; otherwise it downloads it using
    the 'get_db_url' function in env.py that holds login information.
    '''
    
    filename = 'telco_churn_data.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else:
        df = pd.read_sql(
            '''
            SELECT 
                * 
            FROM
                customers
                    JOIN
                contract_types USING(contract_type_id)
                    JOIN
                customer_signups USING(customer_id)
                    JOIN
                internet_service_types USING(internet_service_type_id)
                    JOIN
                payment_types USING(payment_type_id);
            ''',
            get_db_url('telco_churn')
        )

        df.to_csv(filename)

        return df

