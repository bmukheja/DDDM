import pandas as pd
import numpy as np
from sklearn import preprocessing


def input_output(selected_countries,selected_categories,weights):
	dataframes=[]
	i=0
	weight_vector=[]
	for category in selected_categories:
		url=category+'.csv'
		dataframe=pd.read_csv(url)
		ncols=len(dataframe.columns)
		for j in range(0,ncols-1):
			weight_vector.append(weights[i])
		dataframes.append(dataframe)
		i+=1
	truth_table=dataframes[0]
	for dataframe in dataframes[1:]:
		truth_table=truth_table.merge(dataframe,on='Country',how='outer')
	truth_table=truth_table.loc[truth_table['Country'].isin(selected_countries)]	
	truth_table = truth_table.replace(np.NaN, 0)
	truth_table_temp=truth_table
	del truth_table_temp['Country']
	min_max_scaler = preprocessing.MinMaxScaler()
	np_scaled = min_max_scaler.fit_transform(truth_table)
	data = pd.DataFrame(np_scaled)
	scores=[]
	for i in range(0,len(data.index)):
		score_vector=np.array(list(data.iloc[i]))*np.array(weight_vector)
		scores.append(sum(score_vector))
	data['scores'] = scores
	data=data.sort(['scores'],ascending=0)
	print(data)

list1=['af','ba','cy']
list2=['economy','society','geography','demographics','infrastructure']
list3=[1,2,3,4,5]

input_output(list1,list2,list3)
