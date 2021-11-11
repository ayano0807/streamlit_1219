# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 17:12:38 2021

@author: ayano
"""

import streamlit as st

st.title('初めてのstreamlit')
st.write('私の名前は綾乃です')
import streamlit as st
text=st.text_input('あなたの名前を教えて下さい')
'あなたの名前は、',text,'です'

condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション:',condition

option=st.selectbox('好きな数字を教えて下さい',list(['1番','2番','3番','4番']))
'あなたが選択したのは,',option,'です'

left_column, right_column=st.columnｓ(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
    
from PIL import Image
img=Image.open('C:/Users/ayano/Desktop/python/IMG_0988.JPG')
st.image(img,caption='陸上部',use_column_width=True)