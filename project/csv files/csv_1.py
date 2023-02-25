import numpy as np

# Create 50 rows and 4 columns of data
new_data = np.random.random((50, 4))
np.savetxt("main.csv", new_data, fmt="%.2f", delimiter=",", header="H1,H2,H3,H4")

#read csv file

reading_csv= np.loadtxt("main.csv", delimiter=",")
reading_csv[:4, :] #print first 4 rows
