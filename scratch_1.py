import pandas as pd

# Read file
df_survey = pd.read_csv('/Users/kitaeklee/PycharmProjects/coursera_vis/Topic_Survey_Assignment.csv')

# Sort the values in descending orders and rest the index
df_survey = df_survey.sort_values(by=['Very interested'],
                                  ascending=False)
df_survey = df_survey.reset_index()
df_survey1 = df_survey.loc[:, ['Very interested', 'Somewhat interested', 'Not interested']]

# Convert the numbers into percentages of the total number of respondents and
# round the results to 2 decimal places
i=0
for i in df_survey1.index:
    df_survey1.loc[i, 'Very interested'] = round((df_survey.loc[i, 'Very interested']/2233), 2)
    df_survey1.loc[i, 'Somewhat interested'] = round((df_survey.loc[i, 'Somewhat interested'] / 2233), 2)
    df_survey1.loc[i, 'Not interested'] = round((df_survey.loc[i, 'Not interested'] / 2233), 2)
    i+=1
    if i==6:
        break


# Import the Artist Layer, numpy
import matplotlib.pyplot as plt
import numpy as np

xlabels = ['Data Analysis / Statistics', 'Machine Learning',
         'Data Visualization', 'Big Data(Spark / Hadoop)',
         'Deep Learning', 'Data Journalism']

fig, ax = plt.subplots()        # create subplots

# Create the bar chart
ax = df_survey1.plot(kind='bar', figsize=(20,8), width=0.8,
                     color=('#5cb85c', '#5bc0de', '#d9534f'), fontsize=14)
ax.legend(fontsize=14)
ax.set_title('Percentage of Respondents\' Interest in Data Science Areas', fontsize=16)
ax.set_xticklabels(xlabels)
ax.set_yticklabels([])      # remove labels on y-axis
ax.set_yticks([])       # remove y-ticks

# Removing the top, right and left borders from the chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# To adjust the labels of x-axis when it gets cut off
plt.tight_layout()

# Adding % at the top of each bars
for bar in ax.patches:
    ax.annotate('{:.2%}'.format(bar.get_height()),
                xy=(bar.get_x(), bar.get_height()), fontsize=14)

plt.show()


