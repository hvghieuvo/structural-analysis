# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Beam sus",
        page_icon="🙂",
    )

    st.write("# Demo GUI")

    st.sidebar.header("Select a tool above.")
    st.markdown("---")
    st.markdown(
        """
        ### This app is a project by my team at HCMUT.
        ### STILL UNDER CONSTRUCTION!!!
        **👈 Select from the sidebar** to choose a tool
        ### Check out our source code in [github](https://github.com/hvghieuvo/beam-analysis-python)
    """
    )
    st.markdown("---")
if __name__ == "__main__":
    run()
