import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def app():

    st.title("Beam Calculator")
    st.sidebar.header("Beam Calculator")
    st.markdown("---")

    selected = option_menu(None, ["Theory", "Implementation", 'Result','Inference'], 
    default_index=0, orientation="horizontal",styles={
        "container": {"padding": "0!important", "background-color": "#252A33"},
        "icon": {"color": "orange", "font-size": "20px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "blue"},
    })
    selected
      
    if selected == "Theory":
        st.markdown('''<p style="font-size:20px; text-align:justify">A brief overview of the engineering theory and conventions used in this program are illustrated below. 
                    Theory is adapted from the Hibbeler textbook. A more rigorous overview of the basic theory behind statically determinate structures is presented in the 
                    beambending package.</p>''', unsafe_allow_html=True)
        st.link_button('Click here to view full theory!','https://indeterminatebeam.readthedocs.io/en/main/theory.html')
        
    if selected == "Implementation":
        st.subheader("Pseudocode")
        st.code('''
                beam = create_beam(10)
                add_sp(0, "fixed")
                add_sp(10, "pin")
                add_sp(5, "roller")
                add_load(2, -10, "pload")
                add_load(7, -15, "dlv", 10)
                add_load(5, 20, "ptorque")
                lot_diagram(0)
                plot_diagram(1)
                ''')
        
    if selected == "Result":
        # Streamlit app
        st.header("Beam calculator input")
        st.divider()
        col1,col2 = st.columns([1,2])
        # Sliders to adjust parameters
        with col1:
            beam_length = st.number_input("Insert beam length (m)", min_value=1, placeholder="Type a number...")
            
            on = st.toggle('Advance input')
            if on:
                E = st.number_input("Insert Young's Modulus", value=None, placeholder="Type a number...")
                A = st.number_input("Insert Second Moment of Area", value=None, placeholder="Type a number...")
                I = st.number_input("Insert Cross-Sectional Area", value=None, placeholder="Type a number...")
            
            st.divider()
            
            st.subheader("Insert beam supports")
            sp1 = st.text_input("Insert 1st support type", value=None, placeholder="Type a text...")
            sp1_loc = st.slider("Support 1st location", min_value=0.0, max_value=float(beam_length), step=0.1)
            
            sp2 = st.text_input("Insert 2nd support type", value=None, placeholder="Type a text...")
            sp2_loc = st.slider("Support 2nd location", min_value=0.0, max_value=float(beam_length), step=0.1)
            
            st.divider()

            # st.subheader("Insert loads")
            # load1 = st.number_input("Insert load type", value=None, placeholder="Type a text...")
            # load1_mag = st.number_input("Insert magnitude", value=None, placeholder="Type a text...")
            # load1_loc = st.slider("Load location", min_value=0.0, max_value=float(beam_length), step=0.1)

            load_type = st.selectbox('Choose load type',('Point Load','Distributed Load','Point Torque'))
            load_magnitude = st.number_input("Insert magnitude", value=None, placeholder="Type a number...")
            load_location = st.slider("Load location", min_value=0.0, max_value=float(beam_length), step=0.1)

            def add_load(load_list, load_container):
                load_list.append({
                    "type": load_type,
                    "magnitude": load_magnitude,
                    "location": load_location,
                    "delete": False  # Thêm trường để kiểm soát việc xoá
                })
                
                # Tạo một ô trống mới để hiển thị khung nhập tiếp theo
                st.session_state["load_magnitude"] = ""
                
                load_container.text("Load added successfully!")

            # Khởi tạo danh sách để lưu trữ thông tin về các tải
            loads = []

            # Tạo khung nhập cho tải mới
            load_container = st.empty()

            # Hiển thị nút "Add load"
            st.button("Add load", on_click=add_load):
                
            # Hiển thị thông tin tải đã thêm và nút để xoá
            st.subheader("Added loads:")
            for i, load in enumerate(loads, start=1):
                delete_load = st.checkbox(f"Delete Load {i}")
                
                # Kiểm tra nếu nút xoá được chọn
                if delete_load:
                    loads[i - 1]["delete"] = True

                # Hiển thị thông tin tải nếu không được chọn để xoá
                if not loads[i - 1]["delete"]:
                    st.write(f"Load {i}: Type - {load['type']}, Magnitude - {load['magnitude']}, Location - {load['location']}")


        with col2:
            
            st.image('images/fig_beam.png', caption='Beam schematic')
            st.divider()
            st.image('images/fig_reac.png', caption='Beam reaction force diagram')
            st.divider()
        
    if selected == "Inference":
        st.subheader("Merits:")
        st.write("- Simplicity: Linear activation is straightforward and computationally efficient. It involves a simple linear transformation of the input data, making it easy to implement and understand.")
        st.write("- No Saturation: Unlike some other activation functions like sigmoid or tanh, linear activation doesn't suffer from the vanishing gradient problem. This means that gradients don't become extremely small, which can make training more stable, especially in deep neural networks.")
        st.write("- Interpretability: Linear activation retains the interpretability of the input features since it's essentially a linear combination of those features. This can be advantageous in cases where interpretability and feature importance are critical.")
        st.write("- Use in Regression: Linear activation is well-suited for regression problems, where the network is tasked with predicting continuous numeric values. In regression, the model needs to approximate a linear relationship between input features and output.")
        st.divider()
        st.subheader("Demerits")
        st.write("- Limited Expressiveness: Linear activation can only model linear relationships between input and output. It lacks the capacity to capture complex, nonlinear patterns in data. In many real-world problems, the relationships are nonlinear, which can limit the usefulness of linear activation.")
        st.write("- Not Suitable for Classification: For classification tasks, where the goal is to separate data into distinct classes, linear activation is not suitable. It can't create decision boundaries that separate classes effectively since it only performs linear transformations.")
        st.write("- Loss of Depth: In deep neural networks, stacking multiple layers with linear activation functions is essentially equivalent to having a single-layer network. This means that deep architectures may not be able to learn hierarchical or complex representations, which are often needed for tasks like image recognition or natural language processing.")
        st.write("- Output Range Limitation: The output of a linear activation function can cover a wide range of values (both positive and negative), which might not be desirable for some tasks. For example, when dealing with probabilities, it's common to use activation functions that restrict outputs to a specific range (e.g., sigmoid for [0, 1]).")
