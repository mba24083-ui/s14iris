import streamlit as st
from variants import variant_simple, variant_sliders, variant_sidebar, variant_batch

st.set_page_config(page_title='🌸 Iris Flower Prediction (Multi-UI)', layout='centered')
st.title('🌸 Iris Flower Prediction — Choose a UI')

option = st.selectbox('Pick a UI variant to open', [
    'Simple Form (default)', 'Sliders UI', 'Sidebar UI', 'Batch CSV Upload'
])

if option == 'Simple Form (default)':
    variant_simple.render()
elif option == 'Sliders UI':
    variant_sliders.render()
elif option == 'Sidebar UI':
    variant_sidebar.render()
else:
    variant_batch.render()
