import pickle
y2= [5,4,4]
#print(y2)
pick_cust_seg=pickle.load(open('cust_seg.pkl','rb'))
m=pick_cust_seg.predict([y2])
print(m)