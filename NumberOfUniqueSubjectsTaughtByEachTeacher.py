# Method 1
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    tdict = {}
    for i in range(len(teacher)):
        t = teacher['teacher_id'][i]
        s = teacher['subject_id'][i]

        if t not in tdict:
            tdict[t] = set()
        tdict[t].add(s)
    
    result = []
    for k,v in tdict.items():
        result.append([k,len(v)])
    print(result)

    return pd.DataFrame(result, columns = ['teacher_id','cnt'])

# Method 2
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()

    return df.rename(columns = {'subject_id':'cnt'})