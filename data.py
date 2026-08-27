import streamlit as st
from data import CATEGORIAS, DICAS_GERAIS, LOJAS, MODELOS, PARTES

st.set_page_config(
    page_title="AutoPeças PT - SEAT Arona",
    page_icon="🚗",
    layout="wide"
)

def main():
    st.title("AutoPeças PT")
    st.markdown("Catálogo inteligente de peças, acessórios e referências para **SEAT Arona** e grupo VAG.")
    
    st.sidebar.header("Filtros de Pesquisa")
    modelo_sel = st.sidebar.selectbox("Selecione o Modelo", MODELOS)
    
    # Menu lateral de navegação
    menu = st.sidebar.radio("Navegação", ["Catálogo de Peças", "Dicas para Poupar", "Lojas Recomendadas"])
    
    if menu == "Catálogo de Peças":
        pagina_catalogo(modelo_sel)
    elif menu == "Dicas para Poupar":
        pagina_dicas()
    elif menu == "Lojas Recomendadas":
        pagina_lojas()

def pagina_catalogo(modelo):
    st.header("Catálogo de Peças")
    st.markdown(f"Peças, normas e preços de referência para: **{modelo}**")
    
    # Filtros por categoria e pesquisa livre
    col1, col2 = st.columns(2)
    with col1:
        cat_sel = st.selectbox("Categoria", ["Todas as Categorias"] + CATEGORIAS)
    with col2:
        pesquisa = st.text_input("Pesquisa livre (ex: filtro, óleo, velas, pastilhas...)")
    
    # Filtragem das peças
    resultados = PARTES
    
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
        st.warning("Nenhuma peça encontrada com os critérios selecionados. Tente termos mais genéricos.")
        return
        
    st.success(f"Encontradas {len(resultados)} peça(s) correspondentes.")
    
    for peca in resultados:
        with st.container():
            st.subheader(f"{peca['nome']} — {peca['preco']:.2f} €")
            col_a, col_b = st.columns([2, 1])
            with col_a:
                st.write(f"**Marca:** {peca['marca']}")
                st.write(f"**Referência/Código:** `{peca['codigo']}`")
                st.write(f"**Descrição:** {pecs_desc(peca)}") if 'descricao' in peca else st.write(f"**Compatibilidade:** {peca['compatibilidade']}")
            with col_b:
                st.info(f"Categoria: {peca['categoria']}")
            st.markdown("---")

def pecs_desc(peca):
    return f"{peca['descricao']} ({peca['compatibilidade']})"

def pagina_dicas():
    st.header("Dicas para Poupar na Manutenção")
    for i, dica in enumerate(DICAS_GERAIS, 1):
        st.markdown(f"**{i}.** {dica}")

def pagina_lojas():
    st.header("Lojas Recomendadas de Peças")
    st.markdown("Consulte os principais fornecedores online com envio para Portugal:")
    for loja in LOJAS:
        st.markdown(f"- **[{loja['nome']}]({loja['url']})** (Domínio: `{loja['dominio']}`)")

if __name__ == "__main__":
    main()
