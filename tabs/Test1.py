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
                def linear_activation(x, a, b):
                    return a * x + b

                x = 2.0
                a = 0.5
                b = 1.0

                output = linear_activation(x, a, b)
                print(output)

                ''')
        
    if selected == "Result":
        # Define the linear activation function
        def linear_activation(x, a, b):
            return a * x + b

        # Streamlit app
        st.subheader("Linear Activation Function Visualization")
        col1,col2 = st.columns([1,2])
        # Sliders to adjust parameters
        with col1:
            a = st.slider("Slope (a)", min_value=-5.0, max_value=5.0, step=0.1, value=1.0)
            b = st.slider("Intercept (b)", min_value=-10.0, max_value=10.0, step=0.1, value=0.0)
            st.divider()
           
            thickness = st.slider("Select Line thickness", min_value=1, max_value=7, step=1, value=1)
            colour = st.selectbox('Choose a colour for line',('blue','red','green','black'))

        with col2:
            # Generate x values
            x = np.linspace(-10, 10, 400)
            
            # Calculate y values using the linear activation function
            y = linear_activation(x, a, b)

            # Plot the function
            fig, ax = plt.subplots()
            ax.plot(x, y,color=colour,linewidth=thickness)
            ax.set_xlabel("Input (x)")
            ax.set_ylabel("Output (f(x))")
            ax.set_ylim(-10,10)
            ax.set_title("Linear Activation Function")
            plt.grid()

            # Display the plot in Streamlit
            st.pyplot(fig)

        
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