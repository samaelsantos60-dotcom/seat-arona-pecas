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
    
    # Novo campo para Chassis / Matrícula
    st.sidebar.markdown("---")
    st.sidebar.subheader("Validação do Veículo")
    vin_input = st.sidebar.text_input("Matrícula ou Chassis (VIN)", placeholder="Ex: 01-AB-23 ou VSSZZZ...")
    if vin_input:
        st.sidebar.success(f"Veículo associado: `{vin_input}`")
    else:
        st.sidebar.info("Dica: Insira a matrícula para validar peças nas lojas.")
    
    st.sidebar.markdown("---")
    menu = st.sidebar.radio("Navegação", ["Catálogo de Peças", "Dicas para Poupar", "Lojas Recomendadas"])
    
    if menu == "Catálogo de Peças":
        pagina_catalogo(modelo_sel, vin_input)
    elif menu == "Dicas para Poupar":
        pagina_dicas()
    elif menu == "Lojas Recomendadas":
        pagina_lojas(vin_input)

def pagina_catalogo(modelo, vin):
    st.header("Catálogo de Peças")
    if vin:
        st.markdown(f"Peças, normas e preços de referência para: **{modelo}** | *Veículo/Chassis: `{vin}`*")
    else:
        st.markdown(f"Peças, normas e preços de referência para: **{modelo}**")
    
    col1, col2 = st.columns(2)
    with col1:
        cat_opcoes = ["Todas as Categorias"] + list(CATEGORIAS)
        cat_sel = st.selectbox("Categoria", cat_opcoes)
    with col2:
        pesquisa = st.text_input("Pesquisa livre (ex: filtro, óleo, velas, pastilhas...)")
    
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
                st.write(f"**Referência/Código OEM/Ref:** `{peca['codigo']}`")
                st.write(f"**Descrição:** {peca['descricao']}")
                st.write(f"**Compatibilidade:** {peca['compatibilidade']}")
            with col_b:
                st.info(f"Categoria: {peca['categoria']}")
                # Botão de ajuda para pesquisar rapidamente na AutoDoc com o código da peça
                query_busca = f"SEAT Arona {peca['codigo']}"
                st.markdown(f"[🔍 Pesquisar esta referência online](https://www.google.com/search?q={query_busca.replace(' ', '+')})", unsafe_allow_html=True)
            st.markdown("---")

def pagina_dicas():
    st.header("Dicas para Poupar na Manutenção")
    st.markdown("### ⚠️ Cuidados importantes ao comprar online:")
    st.markdown("1. **Confirme sempre a compatibilidade** introduzindo a sua matrícula ou número de chassis (VIN) na loja online antes de pagar.")
    st.markdown("2. **Guarde as faturas**: fundamentais para a garantia das peças e valorização do histórico do veículo.")
    st.markdown("---")
    for i, dica in enumerate(DICAS_GERAIS, 1):
        st.markdown(f"**{i}.** {dica}")

def pagina_lojas(vin):
    st.header("Lojas Recomendadas de Peças")
    if vin:
        st.info(f"Dica: Utilize o seu identificador (`{vin}`) na barra de pesquisa de cada uma das lojas abaixo para garantir 100% de precisão.")
    
    st.markdown("Consulte os principais fornecedores online com envio para Portugal:")
    for loja in LOJAS:
        st.markdown(f"- **[{loja['nome']}]({loja['url']})** (Domínio oficial: `{loja['dominio']}`)")

if __name__ == "__main__":
    main()
