import streamlit as st
from json import loads
from pandas import read_csv

st.markdown('''
# Bem vindo ao exibidor de arquivos
''')

status = 'desconectado'

if(status == 'desconectado'):
    usuario = st.text_input('Usuário')
    senha = st.text_input('Senha', type='password')
    if(usuario == 'well' and senha == '123'):
        status = 'conectado'
        if(usuario != 'well' and senha != '123'):
            st.error('Usuário e senha invalidos')
if(status == 'conectado'):
    st.markdown('''
    ## Carregue um arquivo :smile::heart:
    ''')

    arquivo = st.file_uploader(
        'Selecione um arquivo aqui:',
        type=['jpg','png','py','wav','csv','json','ogg','mp4']
        )

    if arquivo:
        match arquivo.type.split('/'):
            case 'application','json':
                st.json(loads(arquivo.read()))
            case 'image', _:
                st.image(arquivo)
            case 'text','csv':
                df = read_csv(arquivo).transpose()
                st.dataframe(df)
                st.line_chart(df)
            case 'text','x-python':
                st.code(arquivo.read().decode())
            case 'audio',_:
                st.audio(arquivo)
            case 'video',_:
                st.video(arquivo)
    else:
        st.error('Ainda não tenho arquivo')
        