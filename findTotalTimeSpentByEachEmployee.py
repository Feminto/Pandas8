# Method 1
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    emp_dict ={}
    for i in range(len(employees)):
        eid = employees['emp_id'][i]
        day = employees['event_day'][i]
        it = employees['in_time'][i]
        ot = employees['out_time'][i]
        
        if (day,eid) in emp_dict:
            emp_dict[day,eid] += ot-it
        else:
            emp_dict[day,eid] = ot-it
    
    # print(emp_dict)

    result = []
    for (k,v) in emp_dict.items():
        k1 = k[0]
        k2 = k[1]

        result.append([k1,k2,v])

    return pd.DataFrame(result, columns = ['day','emp_id','total_time'])

# Method 2

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    df = employees.groupby(['event_day','emp_id'])['total_time'].sum().reset_index()
    print(df)
    df.rename(columns = {'event_day':'day'}, inplace = True)
    return df