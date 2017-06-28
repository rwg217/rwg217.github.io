name1 = 'Richard'
name2 = 'Jessica'
  
# Get the directory name for data files
import os.path
directory = os.path.dirname(os.path.abspath(__file__)) 
   
#initialize the aggregators
years1=[]
number_of_people1=[]
years2=[]
number_of_people2=[]
  
# Scan one year's file at a time

# Open the file
filename = os.path.join(directory, 'CA'+ '.TXT')
datafile = open(filename, 'r')
# Go through all the names that year
for line in datafile:
    state, gender, year, name, number = line.split(',')
    # Aggregate based on name1
    if name == name1 and gender == 'M':
      years1.append(year)
      number_of_people1.append(number) 
    #Aggregate based on name2
    if name == name2 and gender == 'F':
        years2.append(year)
        number_of_people2.append(number) 
    # Close that year's file
datafile.close()
  
# Plot on one set of axes.
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax.plot(years1, number_of_people1, '#0000FF')
ax.plot(years2, number_of_people2, '#FF00FF')
  
ax.set_title('U.S. Babies Named Richard(blue) or Jessica(pink)')
fig.show()