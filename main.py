import pandas as pd
import numpy as np

exam_data = {'name': ['Ritvik', 'Paarthu', 'Jayanth', 'Sai Krishna', 'Taneesh', 'Devi Sri Prasad', 'Charan Kumar Reddy', 'Chiitesh', 'Ekanath', 'Chaitanya'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify' : ['yes', 'yes', 'yes', 'yes', 'yes','yes', 'yes', 'yes','yes','yes' ]}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print("Summary of the Basic information about this dataFrame and its data: ")
print(df.info())