# Iris Flower Prediction — Streamlit Multi-UI App

This package contains four UI variants implemented in Streamlit for predicting iris species using a pre-trained model (iris_model.pkl).

## Files
- app.py : Launcher to pick a UI variant
- variants/variant_simple.py : Simple form input
- variants/variant_sliders.py : Slider-based input
- variants/variant_sidebar.py : Sidebar-based input with info
- variants/variant_batch.py : CSV upload + batch predictions
- feature_columns.json : List of feature column names required by the model
- iris_model.pkl : Pre-trained model (copied into the package)

## How to run

1. Create a virtualenv and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run Streamlit:

   ```bash
   streamlit run app.py
   ```

3. Choose a UI variant from the dropdown on the app page.

## Notes
- The model file `iris_model.pkl` and `feature_columns.json` are included. If you replace them, keep the same column names in the JSON.
- Variant 4 lets you upload a CSV and download predictions as an Excel file.
