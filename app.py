import streamlit as st
from PIL import Image

# Streamlit interface
st.title("Dark Guard")
st.write("Benchmarking three models - Mobile BERT, DistilBERT, and DistilRoBERTa for the classification task of determining whether a notification is an attempt at a phishing attack or not.")

# Load images
image1 = Image.open('eval_accuracy_l.png')
image2 = Image.open('eval_f1_l.png')
image3 = Image.open('eval_loss_l.png')

# Display images
st.image(image1, caption='Accuracy', use_column_width=True)
st.image(image2, caption='F1 score', use_column_width=True)
st.image(image3, caption='Loss', use_column_width=True)
