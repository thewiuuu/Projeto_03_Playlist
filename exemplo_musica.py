import streamlit as st


# Dados de exemplo
generos = ["Pop", "Trap", "Mpb", "Sertanejo"]

# Dicionário relacionando gêneros aos seus livros
musicas_por_genero = {
    "Pop": ["Michael Jackson", "Justin Bieber", "Bruno Mars"],
    "Trap": ["Alee", "Brandão", "Matue"],
    "Mpb": ["Tim Maia", "Jorge", "Jorge Vercilo"],
    "Sertanejo": ["Marilia Mendonça", "Luan Santana", "Gustavo Lima"]
}

# Selectbox para escolher o gênero                
logo = st.sidebar.image("logo.png")
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    artista_selecionado = st.sidebar.selectbox(
        "Selecione a Musica:", 
        musicas_por_genero[genero_selecionado]
    )
    # Mostrar apenas a musica selecionada
    st.write(f"**Musica selecionado:** {artista_selecionado}")
    st.write(f"**Gênero:** {genero_selecionado}")
    st.image(f"{artista_selecionado}.png")
   

musicas_por_genero = {
    "Pop": ["Michael Jackson", "Justin Bieber", "Bruno Mars"],
    "Trap": ["Alee", "Brandão", "Matue"],
    "Mpb": ["Tim Maia", "Jorge", "Jorge Vercilo"],
    "Sertanejo": ["Marilia Mendonça", "Luan Santana", "Gustavo Lima"]
}
st.markdown("# Musica Popular do Artista")
videos_por_artista = {
    "Michael Jackson": "https://www.youtube.com/watch?v=Zi_XLOBDo_Y&list=RDQNJL6nfu__Q&index=2",
    "Justin Bieber": "https://www.youtube.com/watch?v=fRh_vgS2dFE&list=RDfRh_vgS2dFE&start_radio=1",
    "Bruno Mars": "https://www.youtube.com/watch?v=fLexgOxsZu0&list=RDfLexgOxsZu0&start_radio=1",
    "Alee": "https://www.youtube.com/watch?v=EfJMGfM3c5Q&list=RDEfJMGfM3c5Q&start_radio=1",
    "Brandão": "https://www.youtube.com/watch?v=z7X-zENF4OM&list=RDz7X-zENF4OM&start_radio=1",
    "Matue": "https://www.youtube.com/watch?v=aq-DH4iwviE&list=RDaq-DH4iwviE&start_radio=1",
    "Tim Maia": "https://www.youtube.com/watch?v=cxSzri346W0",
    "Jorge": "https://www.youtube.com/watch?v=xVTee4BJbYA&list=RDxVTee4BJbYA&start_radio=1",
    "Jorge Vercilo": "https://www.youtube.com/watch?v=8FG3JhhKx8c",
    "Marilia Mendonça": "https://www.youtube.com/watch?v=Dt13Wv6Opeo&list=RDDt13Wv6Opeo&start_radio=1",
    "Luan Santana": "https://www.youtube.com/watch?v=tPmS-CfIeNk&list=RDtPmS-CfIeNk&start_radio=1",
    "Gustavo Lima": "https://www.youtube.com/watch?v=-UUe7g8-E0k&list=RD-UUe7g8-E0k&start_radio=1"
}


# Mostrar o vídeo do artista selecionado
st.video(videos_por_artista[artista_selecionado])


