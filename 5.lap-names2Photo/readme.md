# Setting up the environment and installing libraries
    pip3 install virtualenv 
    virtualenv my_env # create a virtual environment my_env
    source my_env/bin/activate # activate my_env

    # installing required libraries in my_env
    pip3 install langchain==0.1.11 gradio==4.44.0 transformers==4.38.2 bs4==0.0.2 requests==2.31.0 torch==2.2.1

# Gradio : 
    touch image_captioning_app.py
    pip3 install gradio
    pip3 install gradio transformers Pillow