from trail import bins
x_new=[[20],[300],[4000]]
y=[]
y[0:2]=bins(x_new[0],x_new[1],x_new[2])
# Flatten the nested list
y2= [val for sublist in y for val in sublist]
print(y2)