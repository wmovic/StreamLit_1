import random

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd





# -------------- app config ---------------

st.set_page_config(page_title="Ophthalmic Flashcards", page_icon="🚀",layout="wide")

padding_top = 0
st.markdown(""" <style> .big-font {font-size:40px !important; font-color:Blue;} </style> """, unsafe_allow_html=True)

st.markdown(""" <style> .title-font
{font-size:70px !important;
fomt-weight:700;
text-align: center;
padding-bottom: {0}rem;
padding-top: {padding_top}rem;
font-color:Blue;}
</style> """, unsafe_allow_html=True)

st.markdown(""" <style> .tiny-font
{font-size:5px !important;
</style> """, unsafe_allow_html=True)

# ---------------- functions ----------------

# external css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# callbacks
def callback():
    st.session_state.button_clicked = True
    st.session_state.firstTime = False



def callback2():
    st.session_state.button2_clicked = True




# ---------------- CSS ----------------

##local_css("style.css")
###st.markdown('<style>body{background-color: #81A2B6;}</style>',unsafe_allow_html=True)
###background-color: #81A2B6
# ---------------- SESSION STATE ----------------

if 'firstTime' not in st.session_state:
    st.session_state.firstTime =True

if 'lastChoice' not in st.session_state:
    st.session_state.lastChoice =-1

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

if "button2_clicked" not in st.session_state:
    st.session_state.button2_clicked = False

if "q_no" not in st.session_state:
    st.session_state.q_no = 0

if "q_no_temp" not in st.session_state:
    st.session_state.q_no_temp = 0

# ---------------- Main page ----------------

st.markdown('<p class="title-font">Ophthalmic Flashcards</p>', unsafe_allow_html=True)
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;padding-top: {0}rem;" /> """, unsafe_allow_html=True)
###st.write(":heavy_minus_sign:" * 32)



excel_data_df = pd.read_excel('test2.xlsx', sheet_name='Sheet1',header=None)

# print whole sheet data
#print(excel_data_df[column][row])
####print(excel_data_df[1][1])
####print(excel_data_df[0][1])



df = pd.read_excel("test2.xlsx")


# how many rows were returned?
no=df.shape[0]
holdRandit=no+30


######st.write("Currently we have " + str(no) + " questions in the database")

# ---------------- Questions & answers logic ----------------


##if (st.button("Ask question", on_click=callback, key="Draw") or st.session_state.button_clicked):
st.write(st.session_state.button_clicked)
st.write('ssssssssssssss')
st.write(st.session_state.firstTime)


col1, col2, col3 = st.columns([1,1,4])

with col1:
    st.button('Ask question', on_click=callback)  ##, key="Draw")
    #st.session_state.button_clicked = True
with col2:
    st.button('Show answer', on_click=callback2)  ##, key="Answer")
    #st.session_state.button2_clicked = True
st.write('')
st.write('')
st.write('')






if  (st.session_state.button_clicked) and not st.session_state.firstTime:
    # randomly select question number
    st.session_state.q_no = random.randint(1, no)


    while st.session_state.q_no==st.session_state.lastChoice:
        st.session_state.q_no = random.randint(1, no)
    st.session_state.lastChoice = st.session_state.q_no

    if st.session_state.button2_clicked:
        st.markdown('<p class="big-font">' + excel_data_df[0][st.session_state.q_no_temp] + '</p>', unsafe_allow_html=True)

    else:
        st.markdown('<p class="big-font">' + excel_data_df[0][st.session_state.q_no] + '</p>', unsafe_allow_html=True)
        st.session_state.q_no_temp = st.session_state.q_no


        ##if st.button("Show answer", on_click=callback2, key="Answer"):
    if (st.session_state.button2_clicked):
        st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;padding-top: {0}rem;" /> """, unsafe_allow_html=True)
        st.markdown('<p class="big-font">' + excel_data_df[1][st.session_state.q_no_temp]+ '</p>', unsafe_allow_html=True)
        st.write(st.session_state.button2_clicked)
        st.session_state.button2_clicked = False
