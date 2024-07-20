import streamlit as st 
from database.database import Database
from extra.face_training import Train
import os
#demo_visitor
# if 'test' not in st.session_state:
#     st.session_state['visitor'] = { 'First_Name' : "Sameer",
#                 'Last_Name'  : "Bhute",
#                 'relation' : "Brother",
#     }

# else:
#     st.session_state['visitor'] = { 'First_Name' : "",
#                 'Last_Name'  : "",
#                 'relation' : "",
#     }



class Caretaker:
    def page(self):
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
            st.write(f"First Name: {st.session_state['Form']['fname']}")
            st.write(f"Last Name: {st.session_state['Form']['lname']}")
            st.write(f"Purpose/Relation: {st.session_state['Form']['Purpose']}")
            st.write(f"Contact No: {st.session_state['Form']['contact']}")
        st.write('')

        approve = st.button("Approve",use_container_width=True)
        
        if approve:
            self.dialog_box()
                    

        reject = st.button("Reject",use_container_width=True)

    @st.experimental_dialog("Want to save visitor in the Database ?")
    def dialog_box(self):
        st.write("")
        columns = st.columns([2,2])

        with columns[0]:
            yes = st.button("Yes",use_container_width=True,key='Yes')

        with columns[1]:
            no = st.button("No",use_container_width=True,key='No')
        
        if yes:
            self.save_database()
            del st.session_state['Form']
            st.session_state['test'] = False
            st.rerun()
        if no:
            del st.session_state['visitor']
            st.session_state['test'] = False



    def save_database(self):
        db = Database('Dementia')
        db.add_visitor(first_name=st.session_state['Form']['Name'],relation=st.session_state['Form']['Purpose'],)
        source = 'src/temp'
        destination = 'src/dataset'
        
        # gather all files
        allfiles = os.listdir(source)
        
        # iterate on all files to move them to destination folder
        for f in allfiles:
            src_path = os.path.join(source, f)
            dst_path = os.path.join(destination, f)
            os.rename(src_path, dst_path)  

        Train() 


if __name__ =='__main__':
    ct = Caretaker()
    ct.page()
    db = Database('Dementia')
    db.create_database()
    db.create_table()
