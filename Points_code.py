import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


Points_filepath = '...' #Insert Filepath of points data
points_data = pd.read_csv(Points_filepath, index_col = 'Weeks', parse_dates = True) #Using pandas to read the csv file

#print(points_data.head()) #This is done to print the first five rows of the data

plt.figure(figsize = (16,10)) #Plotting the points of each team with their corresponding team kit colors
sns.lineplot(data=points_data['Man City'],color='#6AC6EF', label = 'Man City')
sns.lineplot(data=points_data['Liverpool'],color='#7C101F', label = 'Liverpool')
sns.lineplot(data=points_data['Chelsea'],color='#00158C', label = 'Chelsea')
sns.lineplot(data=points_data['Spurs'],color='#132257', label = 'Spurs')
sns.lineplot(data=points_data['Arsenal'],color='#EF1C26', label = 'Arsenal')
sns.lineplot(data=points_data['Man Utd'],color='#C70101', label = 'Man Utd')

sns.set_style = 'darkgrid' #Seaborn formatting
plt.title('Premier League "Big 6" 18/19 points')
plt.xlim(1,38)
plt.ylim(0,100)
plt.xlabel('Weeks')
plt.ylabel('Points')
plt.show()
