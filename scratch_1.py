import pandas as pd


df_survey = pd.read_csv('/Users/kitaeklee/PycharmProjects/coursera_vis/Topic_Survey_Assignment.csv')


df_survey = df_survey.sort_values(by=['Very interested'],
                                  ascending=False)
df_survey = df_survey.reset_index()
i=0
for i in df_survey.index:
    df_survey.loc[i, 'Very interested'] = round((df_survey.loc[i, 'Very interested']/2233), 2)
    df_survey.loc[i, 'Somewhat interested'] = round((df_survey.loc[i, 'Somewhat interested'] / 2233), 2)
    df_survey.loc[i, 'Not interested'] = round((df_survey.loc[i, 'Not interested'] / 2233), 2)
    i+=1
    if i==6:
        break

print(df_survey.loc[:, ['Very interested','Somewhat interested', 'Not interested']])