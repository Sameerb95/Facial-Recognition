import streamlit as st


st.title("Visitor's Form")
st.subheader("Enter details below")

#CREATING OUR FORM FIELDS
with st.form("form1", clear_on_submit=True):
    fname = st.text_input("Enter First name")
    lname = st.text_input("Enter Last name")
    contact_no =  st.text_input("Enter your Contact number")
    Purpose  =  st.text_area("State your Purpose for Visit")
    submit = st.form_submit_button("Submit Form")


if submit:
    st.session_state['Form'] = {
            'fname' : fname,
            'lname' : lname,
            'contact' : contact_no,
            'Purpose' : Purpose,

    }
    st.switch_page("pages/2_caretaker_page.py")