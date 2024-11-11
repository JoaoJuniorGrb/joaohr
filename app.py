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

------------------------------------------------------------------------------------------------------------------------------

if True:
    arqivo_css = 'https://github.com/JoaoJuniorGrb/app/blob/4ef7f6d97028d111ca7ddc34ff1a2e6c6e9b0a3f/propriedades/styles/main.css'
    arqivo_pdf = 'https://github.com/JoaoJuniorGrb/app/blob/4ef7f6d97028d111ca7ddc34ff1a2e6c6e9b0a3f/propriedades/assets/Curriculo.pdf'
    arqivo_img = 'https://github.com/JoaoJuniorGrb/appestreamlit/blob/624cf41fb2c6bc7152359344c6d0b29f264228e1/Foto_.jpg?raw=true'
    titulo = "Curriculum | João Ferreira Junior"
    nome = "João Hering Ferreira"
    descrição = "Engenheiro de Energia, Pós graduação em Automação e controle de processos Conhecimento em Python e microcontroladores"
    st.title('Desenvolvido por',nome)
    # Fazer o download da imagem
    response = requests.get(arqivo_img)
    if response.status_code == 200:
        # Abrir a imagem a partir do conteúdo binário
        img = Image.open(BytesIO(response.content))

    email = "joaojunior.grb@hotmail.com"
    midia_social = {"LinkedIn": "https://www.linkedin.com/in/jo%C3%A3o-ferreira-junior-b2698163/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BAjwOn5KcRhmkdM6UuXiVjw%3D%3D"}

    projetos = {":toolbox: Ferramenta 1": "ferramenta 1",
                ":toolbox: Ferramenta 2": "ferramenta 2",
                ":toolbox: Ferramenta 3": "ferramenta 2"}

    col1, col2 = st.columns(2, gap="small")

    with col1:
        st.image(img,width=250)

    with col2:
        st.title(nome,anchor=False)
        st.write(descrição,anchor=False)
        st.write(":email:", email)

    # midias sosiais
    st.write("#")
    colunas = st.columns(len(midia_social))
    for indice, (plataforma, link) in enumerate(midia_social.items()):
        colunas[indice].write(f"[{plataforma}]({link})")
    # experiencias
    st.write("#")
    st.subheader("Experiências",anchor=False)
    st.write(""":white_check_mark: Fiedler Automação industrial""", anchor=False)
    st.write(""" 	:white_check_mark: Termosul engenharia e aquecimento """,
        anchor = False
    )


#------------------------------------------------------------------------------------------------------------------------------

