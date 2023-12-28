import pandas as pd
import numpy as np
def bins(r,f,m):
  #recency_bin=[rfm['Recency'].min()-1, 20,50,150,250,rfm['Recency'].max()]
  recency_bin=[0, 20,50,150,250,np.inf]
  #freq_bin=[rfm['Frequency'].min()-1, 2,3,10,100,rfm['Frequency'].max()]
  freq_bin=[0, 2,3,10,100,np.inf]
  #mon_bin=[rfm['Monetary Value'].min()-3,300,600,2000,5000,rfm['Monetary Value'].max()
  mon_bin=[0,300,600,2000,5000,np.inf]
  r_s=pd.cut(r, bins=recency_bin, labels=range(1,6), include_lowest=True)
  r_s=5-r_s.astype(int) +1
  f_s=pd.cut(f,bins=freq_bin,labels=range(1,6),include_lowest=True).astype(int)
  m_s=pd.cut(m,bins=mon_bin,labels=range(1,6),include_lowest=True).astype(int)
  return r_s,f_s,m_s

if __name__ == "__main__":
    # This block will only run if the script is executed directly, not when imported
    # You can add test or example code here
    print("Hello")
    pass