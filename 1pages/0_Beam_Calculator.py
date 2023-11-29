from typing import Any
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

st.set_page_config(page_title="Beam Calculator", page_icon="🙃")
st.markdown("# Beam Calculator")
st.sidebar.header("Beam Calculator Tool")
st.markdown("---")
tab1, tab2 = st.tabs(["Theory", "Input"])
with tab1:
    st.header('Theory')
    st.markdown('''<p style="font-size:20px; text-align:justyfy">A brief overview of the engineering theory and conventions used in this program are illustrated below. Theory is adapted from the Hibbeler textbook [2]. A more rigorous overview of the basic theory behind statically determinate structures is presented in the beambending package documentation.</p>''',unsafe_allow_html=True)
    st.link_button('Click here!','https://indeterminatebeam.readthedocs.io/en/main/theory.html?fbclid=IwAR18lJpYVJm1MnqkVdXydhA0eLWQwSmCV4w6VzKAIK5dueK9zq-_gYrxMy0')
with tab2:
    select = st.selectbox('Beam type',
    ('Console', '2 supports'))
    if select == 'Console':
        length = st.number_input('Length',min_value=0,max_value=None,step=1, placeholder='Type a number...')
            
        point_load = st.number_input('Amount of force want to add?', min_value=0,max_value=None,step=1, placeholder='Type a number...')
        equivalent_forces = [f'Force {i}' for i in range(1, point_load + 1)]
        st.write(equivalent_forces)
        for force in equivalent_forces:
            st.subheader(force)
            position = st.number_input(f"Position {force}", min_value=0, max_value=length, step=1)
            magnitude = st.number_input(f"Magnitude {force}")
            if position > length:
                st.warning(f"The position of {force} must be on the beam.")
        distributed_load = st.number_input('Amount of distributed load want to add?', min_value=0,max_value=None,step=1, placeholder='Type a number...')
            
        moment = st.number_input('Magnitude of moment',min_value=0,max_value=None,step=1, placeholder='Type a number...')
            
            

                        