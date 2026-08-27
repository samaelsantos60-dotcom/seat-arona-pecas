import streamlit as st
from data import CATEGORIAS, DICAS_GERAIS, LOJAS, MODELOS, MOTORIZACOES, PARTES

st.set_page_config(
    page_title="AutoPeças PT - SEAT Arona",
    page_icon="🚗",
    layout="wide"
)

def main():
    st.title("AutoPeças PT")
    st.markdown("Catálogo inteligente de peças, acessórios e referências para **SEAT Arona** e grupo VAG.")
    
    st.sidebar.header("Seleção do Veículo")
    modelo_sel = st.sidebar.selectbox("Modelo", MODELOS)
    motor_sel = st.sidebar.selectbox("Motorização", MOTORIZACOES)
    
    st.sidebar.markdown("---")
    menu = st.sidebar.radio("Navegação", ["Catálogo de Peças", "Dicas para Poupar", "Lojas Recomendadas"])
    
    if menu == "Catálogo de Peças":
        pagina_catalogo(modelo_sel, motor_sel)
    elif menu == "Dicas para Poupar":
        pagina_dicas()
    elif menu == "Lojas Recomendadas":
        pagina_lojas(motor_sel)

def pagina_catalogo(modelo, motor):
    st.header("Catálogo de Peças")
    st.markdown(f"Peças e referências para: **{modelo}** | *Motorização selecionada: `{motor}`*")
    
    col1, col2 = st.columns(2)
    with col1:
        cat_opcoes = ["Todas as Categorias"] + list(CATEGORIAS)
        cat_sel = st.selectbox("Categoria", cat_opcoes)
    with col2:
        pesquisa = st.text_input("Pesquisa livre (ex: filtro, óleo, velas, pastilhas...)")
    
    # Filtragem rigorosa por motorização e categoria
    resultados = PARTES
    
    if motor != "Todas as Motorizações":
        resultados = [p for p in resultados if p["motorizacao"] == motor or p["motorizacao"] == "Todas as Motorizações"]
    
    if cat_sel != "Todas as Categorias":
        resultados = [p for p in resultados if p["categoria"] == cat_sel]
        
    if pesquisa:
        termo = pesquisa.lower()
        resultados = [
            p for p in resultados 
            if termo in p["nome"].lower() 
            or termo in p["marca"].lower() 
            or termo in p["codigo"].lower()
            or termo in p["descricao"].lower()
        ]
    
    st.markdown("---")
    
    if not resultados:
        st.warning("Nenhuma peça encontrada para esta motorização com os critérios selecionados.")
        return
        
    st.success(f"Encontradas {len(resultados)} peça(s) compatíveis.")
    
    for peca in resultados:
        with st.container():
            st.subheader(f"{peca['nome']} — {peca['preco']:.2f} €")
            col_a, col_b = st.columns([2, 1])
            with col_a:
                st.write(f"**Marca:** {peca['marca']}")
                st.write(f"**Referência/Código:** `{peca['codigo']}`")
                st.write(f"**Compatibilidade:** `{peca['motorizacao']}`")
                st.write(f"**Descrição:** {peca['descricao']}")
            with col_b:
                st.info(f"Categoria: {peca['categoria']}")
                query_busca = f"SEAT Arona {peca['codigo']}"
                st.markdown(f"[🔍 Pesquisar referência online](https://www.google.com/search?q={query_busca.replace(' ', '+')})", unsafe_allow_html=True)
            st.markdown("---")

def pagina_dicas():
    st.header("Dicas para Poupar na Manutenção")
    for i, dica in enumerate(DICAS_GERAIS, 1):
        st.markdown(f"**{i}.** {dica}")

def pagina_lojas(motor):
    st.header("Lojas Recomendadas de Peças")
    st.info(f"Ao consultar as lojas abaixo para o seu motor **{motor}**, selecione sempre a motorização exata no filtro da respetiva loja.")
    for loja in LOJAS:
        st.markdown(f"- **[{loja['nome']}]({loja['url']})** (Domínio oficial: `{loja['dominio']}`)")

if __name__ == "__main__":
    main()
