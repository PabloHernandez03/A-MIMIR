import pandas as pd

dataFrame = pd.read_csv('./student_sleep_patterns.csv')
print(dataFrame)

print("Procesamiento")

dataFrame=dataFrame.drop(columns=['Student_ID',
                                    'Gender',
                                    'University_Year',
                                    'Weekday_Sleep_Start',
                                    'Weekend_Sleep_Start',
                                    'Weekday_Sleep_End',
                                    'Weekend_Sleep_End',
                                ])
print(dataFrame)

dataFrame.to_csv('DatasetRegression.csv',index=False)

def sleepQuality(x):
    if x < 5:
        return 'Bajo'
    elif x >=5 and x<7:
        return 'Regular'
    elif x >=7:
        return 'Bueno'

dataFrame['Sleep_Quality'] = dataFrame['Sleep_Quality'].apply(sleepQuality)
dataFrame.to_csv('DatasetClasification.csv',index=False)