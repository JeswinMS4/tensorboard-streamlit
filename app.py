import streamlit as st
import subprocess
import time
import os

# Function to start TensorBoard
def start_tensorboard(logdir):
    command = f'tensorboard --logdir={logdir} --host=0.0.0.0 --port=6006'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

# Streamlit interface
st.title("Dark Guard")
st.write("Benchmarking three models - Mobile BERT, DistilBERT, and DistilRoBERTa for the classification task of determining whether a notification is an attempt of social engineering or not.")

# Input for log directory
logdir = st.text_input("Log Directory", value="ALL_RUNS")

# Button to start TensorBoard
if st.button("Start TensorBoard"):
    if logdir:
        process = start_tensorboard(logdir)
        st.success(f"TensorBoard started with log directory: {logdir}")
        st.write("You can access TensorBoard [here](http://localhost:6006)")
        # Give some time for TensorBoard to start
        time.sleep(5)
    else:
        st.error("Please enter a valid log directory.")

# Instructions to stop TensorBoard
st.write("To stop TensorBoard, you can interrupt the kernel or kill the process manually.")
