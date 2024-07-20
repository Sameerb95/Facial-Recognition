import streamlit as st 

st.markdown("""
    <style>
        button {
            
            padding-top: 50px !important;
            padding-bottom: 50px !important;
        }
    </style>
""", unsafe_allow_html=True)

for i in range(25):
    st.write('')

columns = st.columns([2,2,2])

with columns[1]:
    st.image('resources/User2.png')
    st.write("Name:")
    st.write("Purpose ")
    st.write("Contact No: ")
st.write('')

approve = st.button("Approve",use_container_width=True)
reject = st.button("Reject",use_container_width=True)
