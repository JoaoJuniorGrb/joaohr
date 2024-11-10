import streamlit as st
import CoolProp.CoolProp as prop
from CoolProp.CoolProp import PropsSI,PhaseSI
from pathlib import Path
from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px
from scipy.optimize import fsolve
import requests
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import requests
from io import BytesIO
import firebase_admin
from firebase_admin import credentials, storage, initialize_app
import json
from streamlit_autorefresh import st_autorefresh
import time
from datetime import datetime
import pytz
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials, storage
import json
import control as ctrl

url_imagem = "https://www.madeiratotal.com.br/wp-content/uploads/2024/10/Submarca-Fiedler-01-1024x358.webp"
# Esconde o cabeçalho e o rodapé padrão do Streamlit
st.set_page_config(page_title="Fiedler Automação", page_icon="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAqFBMVEUuMo0rMI0oLY8lK48kKpARHJIwNIZiX3ZybXQFFZN2cWvUxS/55wj/7gD/8AD/8wDh0SAdJI9ZVnro1x//9gD/7wB+eGcWIJKPh1/u3ROakVZFRoExNYAmLIPz4RSFfmRNTH0qL44+QITLvTN4c2a4q0jBtD7JvD+VjV47PYfayyqqoE9gXnCIgGNbWXivpEtmY25SUnwAEJRKS34AAJamnFSflVfOwC7jtOtQAAAA/0lEQVR4AWIYcACgih60GIahAIDWippas1f7/79sXrLd4+BRlGTu/0pRNd3gNIGTTAtAhL+ITfkddVzPRxwJFHYXRshHxI/dL5vfqQlBxI7SbMGILKbl4WWwApBHXW8+d5stJLt9TDgPUJbw4B0TTODpHHysHOn78QKvK0LyIgfXjx3LqJS48pbF0fOw/0ZqFpWC+gQr27tGevVx+f4UM7/BFcABpfKLJEm8jzModxZqTboRn4Rfqttc26vRBa7/hInBF7Lp4/Sq2cMYj+enlbMRGDqep2Cy9N0Yzw/AogIn29JMwZAneRc+/S1Zq8RKaDfrlt6HLW0oQqAiw6AAACorHoO4OiwrAAAAAElFTkSuQmCC", layout="wide")

st.sidebar.markdown(
    f"<img src='{url_imagem}' style='width:200px;'/>",
    unsafe_allow_html=True
)
#remove estilo stream lit
remove_st_estilo = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""

st.markdown(remove_st_estilo,unsafe_allow_html=True)

