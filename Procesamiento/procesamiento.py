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

def age(x):
    if x >=18 and x<=19:
        return '18-19'
    elif x >=20 and x<=21:
        return '20-21'
    elif x >=22 and x<=23:
        return '22-23'
    elif x >=24 and x<=25:
        return '24-25'

def sleepQuality(x):
    if x < 5:
        return 'Bajo'
    elif x >=5 and x<7:
        return 'Regular'
    elif x >=7:
        return 'Bueno'

def studyHours(x):
    if x >=0 and x<=4:
        return '[0-4]'
    elif x >4 and x<=8:
        return '(4-8]'
    elif x >8:
        return '(8-inf)'

def sleepDuration(x):
    if x >=0 and x<=3:
        return '[0-3]'
    elif x >3 and x<=6:
        return '(3-6]'
    elif x >6:
        return '(6-inf)'

def screenTime(x):
    if x >=0 and x<=2:
        return '[0-2]'
    elif x >2 :
        return '(2-inf)'
    
def intake(x):
    if x >=0 and x<=2.5:
        return '[0-2.5]'
    elif x >2.5 :
        return '(2.5-inf)'

def phisicalActivity(x):
    if x >=0 and x<=30:
        return '[0-30]'
    elif x >30 and x<=60:
        return '(30-60]'
    elif x >60 and x<=90:
        return '(60-90]'
    elif x >90:
        return '(90-inf)'  
dataFrame['Age'] = dataFrame['Age'].apply(age)
dataFrame['Sleep_Quality'] = dataFrame['Sleep_Quality'].apply(sleepQuality)
dataFrame['Study_Hours']=dataFrame['Study_Hours'].apply(studyHours)
dataFrame['Sleep_Duration'] = dataFrame['Sleep_Duration'].apply(sleepDuration)
dataFrame['Screen_Time'] = dataFrame['Screen_Time'].apply(screenTime)
dataFrame['Caffeine_Intake'] = dataFrame['Caffeine_Intake'].apply(intake)
dataFrame['Physical_Activity'] = dataFrame['Physical_Activity'].apply(phisicalActivity)

dataFrame.to_csv('DatasetAssociation.csv',index=False)