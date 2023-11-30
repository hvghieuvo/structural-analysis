import streamlit as st
from tabs import Test1, Test2, Test3, home

def run():
    st.set_page_config(
        page_title="Structural sus",
        page_icon="🙂",
        layout = 'wide',
        initial_sidebar_state = 'auto'
    )

    # st.write("# Demo GUI")
    
    # Add title to sidear
    st.sidebar.title("Navigation")
    
    # st.sidebar.header("Select a tool above.")
    
    # st.markdown("---")
    # st.markdown(
    #     """
    #     ### STILL UNDER CONSTRUCTION!!!
    #     **👈 Select from the sidebar** to choose a tool
    #     ### Check out source code in [github](https://github.com/hvghieuvo/structural-analysis)
    # """
    # )
    # st.markdown("---")
    
    Tabs = {
    "Home": home,
    "Test 1": Test1,
    "Test 2": Test2,
    "Test 3": Test3
    }
    
    # Create radio option to select the page
    page = st.sidebar.radio("Pages", list(Tabs.keys()))

    Tabs[page].app()

    st.sidebar.info("Made by : [Naze](https://www.linkedin.com/in/hieuvo-naze/)")
if __name__ == "__main__":
    run()
