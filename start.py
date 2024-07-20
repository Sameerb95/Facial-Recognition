import streamlit as st 


# st.set_page_config(initial_sidebar_state="collapsed",layout = "wide")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)



# Custom CSS to styles
st.markdown("""
    <style>
        button {
            
            padding-top: 50px !important;
            padding-bottom: 50px !important;
        }
    </style>
""", unsafe_allow_html=True)

# create two columns to structure the app
columns = st.columns([1,1,1])

with columns[1]:
    triggered = st.button(
        r"$\textsf{\Large Push}$",
        type="primary",
        use_container_width=True
    )

if triggered:
    st.switch_page("pages/1_face_detection.py")