from typing import Any
import numpy as np
import streamlit as st
from streamlit.hello.utils import show_code
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from io import StringIO, BytesIO
from PIL import Image
import base64
import plotly.express as px

st.set_page_config(page_title="Section Designer", page_icon="🙃", layout = 'wide')
st.markdown("# Section Designer")
st.sidebar.header("Section Designer Tool")
st.markdown("---")

tab1, tab2, tab3 = st.tabs(["Theory", "Input", "Output"])
with tab1:
    # Hiển thị lý thuyết với đường link đến tài liệu
    st.header('Introduction')
    st.markdown('''<p style="font-size:20px; text-align:justyfy">The analysis of homogenous cross-sections is particularly relevant in structural design, in particular for the design of steel structures, where complex built-up sections are often utilised. Accurate warping independent properties, such as the second moment of area and section moduli, are crucial input for structural analysis and stress verification. Warping dependent properties, such as the Saint-Venant torsion constant and warping constant are essential in the verification of slender steel structures when lateral-torsional buckling is critical.</p>''',unsafe_allow_html=True)
    st.link_button('Click here!','https://sectionproperties.readthedocs.io/en/stable/user_guide/theory.html')

with tab2:
    select = st.selectbox('Cross section type', ('Rectangle', 'Circle','Annulus','C','I'))
    if select == 'Rectangle':
        col1, col2, col3 = st.columns(3, gap='large')
        with col1:
            high = st.number_input(label='Height', min_value=0.00, max_value=None, step=0.01)
            st.markdown('---')  
            width = st.number_input(label='Width', min_value=0.00, max_value=None, step=0.01)
        with col2:
            max_bending_moment = st.number_input('Maximum bending moment (kNm)', min_value=0.00, max_value=None, step=0.01)
            max_shear_force = st.number_input('Maximum shear force (kN)', min_value=0.00, max_value=None, step=0.01)
            shear_force_at_maximum_moment = st.number_input('Shear force at maximum moment (kN)', min_value=0.00, max_value=None, step=0.01)
            allowable_stress = st.number_input('Allowable stress (N/m^2)', min_value=0.00, max_value=None, step=0.01)
        with col3:
            type_criterion = st.selectbox('Type criterion', ('Tresca', 'von Mises'))
    
    elif select == 'Circle':
        col1_1, col2_1, col3_1 = st.columns(3, gap='large')
        with col1_1:
            R = st.number_input(label="Radius", min_value=0.00, max_value=None, step=0.01)
        with col2_1:
            max_bending_moment = st.number_input('Maximum bending moment (kNm)', min_value=0.00, max_value=None, step=0.01)
            max_shear_force = st.number_input('Maximum shear force (kN)', min_value=0.00, max_value=None, step=0.01)
            shear_force_at_maximum_moment = st.number_input('Shear force at maximum moment (kN)', min_value=0.00, max_value=None, step=0.01)
            allowable_stress = st.number_input('Allowable stress (N/m^2)', min_value=0.00, max_value=None, step=0.01)
        with col3_1:
            type_criterion = st.selectbox('Type criterion', ('Tresca', 'von Mises'))

    elif select == 'Annulus':
        col1_2, col2_2, col3_2 = st.columns(3, gap='large')   
        with col1_2:
            R_in = st.number_input(label='Radius in', min_value=0.00, max_value=None, step=0.01)  
            R_out = st.number_input(label='Radius out', min_value=0.00, max_value=None, step=0.01)
        with col2_2:
            max_bending_moment = st.number_input('Maximum bending moment (kNm)', min_value=0.00, max_value=None, step=0.01)
            max_shear_force = st.number_input('Maximum shear force (kN)', min_value=0.00, max_value=None, step=0.01)
            shear_force_at_maximum_moment = st.number_input('Shear force at maximum moment (kN)', min_value=0.00, max_value=None, step=0.01)
            allowable_stress = st.number_input('Allowable stress (N/m^2)', min_value=0.00, max_value=None, step=0.01)
        with col3_2:
            type_criterion = st.selectbox('Type criterion', ('Tresca', 'von Mises'))

    elif select == 'C':
        st.title('Table data of cross-section C')
        df=pd.read_csv("data/chu_C.csv")
        st.table(df)
        
