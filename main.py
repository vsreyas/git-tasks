import streamlit as st
import pickle
import pandas as pd
import  hickle as hkl
import numpy as np
import requests
def recommend(song):
        song_index = music1[music['track_name'] == song].index[0]
        dis = cps[song_index]
        m_l = sorted(list(enumerate(dis)), reverse=True, key=lambda x: x[1])[2:40]
        rec_ms=[]
        for i in m_l:
            rec_ms.append(music.iloc[i[0]].track_name)
        return rec_ms
def recommend1(genre):
    print(type(genre))
    gen=np.array_str(genre)
    l=len(gen)
    gen1=''
    for i in range(2,l-2):
        gen1+=gen[i]
    print(gen1)
    gen_list=pd.read_csv('genre/'+gen1+'.csv').head(10)
    print(gen_list)
    return gen_list['track_name'],gen_list['artists']
    
    
    
music_list=pickle.load(open('movie12_dict.pkl','rb'))
music_list1=pickle.load(open('movie1_dict.pkl','rb'))
cps=pickle.load(open('cps.pkl','rb'))
music=pd.DataFrame(music_list)
music1=pd.DataFrame(music_list1)
g=pickle.load(open('genree.pkl','rb'))
g1=pd.DataFrame(g)
st.title('MUSIC RECOMMENDATION SYSTEM')
option=st.selectbox(
    "Select the Music",music['track_name'].values)
if st.button('Recommend'):
    rec=recommend(option)
    for i in rec:
     st.write(i)
        
option1=st.selectbox(
    'Select the genre',g1.values)
if st.button('Recommend '):
    rec,rec1=recommend1(option1)
    for i in range(0,10):
        st.write(rec[i]+" ("+rec1[i]+")")