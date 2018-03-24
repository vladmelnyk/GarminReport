import pandas as pd
import statsmodels.api as sm
from fitparse import FitFile
from numpy import nan



def get_data_df(fitfile):
    df = pd.DataFrame(columns=('cadence', 'heart_rate', 'speed'))

    for record in fitfile.get_messages('record'):

        record = record.get_values()
        df = df.append(pd.DataFrame([[record.get('cadence'), record.get('heart_rate'), record.get('speed')]],
                           columns=('cadence', 'heart_rate', 'speed')))

    return df


if __name__ == '__main__':
    df = get_data_df(FitFile('2576417416.fit'))
    # drop 0 values and duplicates
    df = df.drop_duplicates()
    df = df.replace(0, nan)
    df = df.dropna(how='any', axis=0)
    df = df.replace(nan, 0)
    # convert rpm to spm
    df['cadence'] = df['cadence'] * 2
    # convert m/sec to min/km
    df['speed'] = 1 /(df['speed'] /(100/6))

    X = df[['cadence', 'speed']]
    y = df['heart_rate']
    model = sm.OLS(y, X).fit()
    predictions = model.predict(X)
    print(model.summary())
