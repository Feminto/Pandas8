# Method 1
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    cdict = {}
    for i in range(len(courses)):
        c = courses['class'][i]
        s = courses['student'][i]

        if c not in cdict:
            cdict[c] = set()
        cdict[c].add(s)
    
    result = []
    for k,v in cdict.items():
        if len(v) >= 5:
            result.append(k)
    # print(result)

    return pd.DataFrame(result, columns = ['class'])


# Method 2
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].nunique().reset_index()

    return df[df['student'] >= 5][['class']]