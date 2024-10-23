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


# deploy
    touch demo.py Dockerfile requirements.txt
    ibmcloud ce project get current
    ibmcloud ce project get --name "Code Engine - sn-labs-locluu1990"

    cd 

    ibmcloud ce build create --name build-local-dockerfile1 \
                        --build-type local --size large \
                        --image us.icr.io/${SN_ICR_NAMESPACE}/myapp1 \
                        --registry-secret icr-secret
                        /

https://demo1.1ndyawo7vy44.us-south.codeengine.appdomain.cloud

