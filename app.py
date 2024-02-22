from pygwalker.api.streamlit import init_streamlit_comm
import pygwalker as pyg
import streamlit as st
import streamlit.components.v1 as components
import streamlit as st
from modules.pygwalker import get_df, VIS_SPEC


st.set_page_config(
    page_title="Position Complexity",
    layout="wide",
    page_icon='📈'
)


def main():
    init_streamlit_comm()

    st.sidebar.page_link('app.py', label='Home', icon='🏡')
    st.sidebar.page_link('pages/explorer.py', label='Explorer', icon='🏝️')

    st.title('Data Visualizer')

    st.markdown('''
**:trophy: [Freestyle Chess](https://www.freestyle-chess.com/) G.O.A.T. Challenge 2024** 
                ''')
    # renderer = get_pyg_renderer()
    # renderer.render_explore()

    df = get_df()
    pyg_html = pyg.to_html(df, spec=VIS_SPEC)
    components.html(pyg_html, height=1000, scrolling=True)


if __name__ == '__main__':
    main()
