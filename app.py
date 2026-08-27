import streamlit as st
from data import CATEGORIAS, MODELOS, MOTORIZACOES, DICAS_GERAIS, LOJAS, PARTES

# Configuração da página em modo wide para ocupar todo o ecrã
st.set_page_config(
    page_title="Norauto / AutoPeças PT - SEAT Arona",
    page_icon="🚗",
    layout="wide"
)

# Estilo CSS personalizado para imitar o design profissional da Norauto
st.markdown("""
    <style>
    /* Ocultar elementos padrão do Streamlit para um aspeto mais limpo */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Barra de topo estilo e-commerce */
    .top-bar {
        background-color: #111827;
        padding: 12px 24px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 6px;
        margin-bottom: 20px;
    }
    .logo-text {
        font-size: 26px;
        font-weight: 800;
        color: #f59e0b;
        letter-spacing: -0.5px;
    }
    .user-badge {
        background-color: #1f2937;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 14px;
        border: 1px solid #374151;
        color: #e5e7eb;
    }
    
    /* Cartões de produtos */
    .product-card {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
    }
    .product-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-color: #f59e0b;
    }
    .badge-cat {
        background-color: #fef3c7;
        color: #92400e;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
    }
    .price-tag {
        font-size: 22px;
        font-weight: 700;
        color: #111827;
    }
    </style>
""", unsafe_allow_html=True)

# 1. DEFINIÇÃO DA FUNÇÃO PRIMEIRO (Para evitar NameError)
def renderizar_cartao(peca):
    url_loja = peca['link_compra']
    nome_loja = "Loja Online"
    for loja in LOJAS:
        if loja['url'] in url_loja:
            nome_loja = loja['nome']
            break
            
    st.markdown(f"""
        <div class="product-card">
            <span class="badge-cat">{peca['categoria']}</span>
            <h4 style="margin-top: 8px; margin-bottom: 5px; color: #111827; font-size: 16px;">{peca['nome']}</h4>
            <p style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">Marca: <b>{peca['marca']}</b> | Ref: <code>{peca['codigo']}</code></p>
            <p style="font-size: 13px; color: #374151; margin-bottom: 10px;">{peca['descricao']}</p>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
                <span class="price-tag">{peca['preco']:.2f} €</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(f"🛒 Ver em {nome_loja}", url_loja, use_container_width=True)
    st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

# Cabeçalho Superior Fixo (Estilo Norauto)
st.markdown("""
    <div class="top-bar">
        <div>
            <span class="logo-text">NORAUTO</span> &nbsp;|&nbsp; <span style="font-size: 16px; color: #9ca3af;">AutoPeças PT</span>
        </div>
        <div>
            <span class="user-badge">📍 Évora &nbsp;&nbsp;|&nbsp;&nbsp; 🚗 SEAT ARONA 1.0 TSI &nbsp;&nbsp;|&nbsp;&nbsp; 👤 Utilizador</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Barra de Navegação Horizontal por Categorias (Estilo Abas)
categoria_ativa = st.radio(
    "Navegação por Categorias",
    ["Todas as Categorias"] + CATEGORIAS,
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("---")

# Linha de Pesquisa e Filtros Rápidos
col_search, col_motor = st.columns([3, 1])

with col_search:
    pesquisa_livre = st.text_input(
        "Pesquisa",
        placeholder="🔍 O que procura? (ex: filtro, óleo, velas, pastilhas, pára-choques, escovas...)",
        label_visibility="collapsed"
    )

with col_motor:
    motorizacao_sel = st.selectbox("Motorização", MOTORIZACOES, label_visibility="collapsed")

st.markdown("")

# Layout Principal em Colunas
col_esq, col_dir = st.columns([1, 3])

with col_esq:
    st.markdown("### ⚡ Os mais procurados")
    st.markdown("""
    <div style="background-color: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #e5e7eb;">
        <ul style="padding-left: 15px; margin: 0; font-size: 13px; color: #4b5563; line-height: 2.2;">
            <li><b>Até -100€</b> em Pneus selecionados</li>
            <li>Óleo de Motor 5W30 VW 504/507</li>
            <li>Escovas Limpa-Para-Brisas Bosch</li>
            <li>Pastilhas de Travão Brembo</li>
            <li>Filtros de Óleo e Ar Mann-Filter</li>
            <li>Lâmpadas H7 de Longa Duração</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🏷️ Marcas Parceiras")
    st.markdown("""
    <div style="background-color: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #e5e7eb; margin-top: 10px;">
        <p style="font-size: 12px; color: #6b7280; margin-bottom: 8px;">Parceiros oficiais com entrega em Portugal:</p>
        <span style="display:inline-block; background:#f3f4f6; padding:4px 8px; border-radius:4px; font-size:11px; margin:2px;"><b>AutoDoc</b></span>
        <span style="display:inline-block; background:#f3f4f6; padding:4px 8px; border-radius:4px; font-size:11px; margin:2px;"><b>Oscaro</b></span>
        <span style="display:inline-block; background:#f3f4f6; padding:4px 8px; border-radius:4px; font-size:11px; margin:2px;"><b>Norauto</b></span>
        <span style="display:inline-block; background:#f3f4f6; padding:4px 8px; border-radius:4px; font-size:11px; margin:2px;"><b>Mister-Auto</b></span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("💡 Dicas Técnicas")
    for dica in DICAS_GERAIS:
        st.info(dica)

with col_dir:
    st.markdown(f"### Catálogo de Peças Disponíveis")
    st.markdown(f"<p style='color: #6b7280; font-size: 14px;'>Filtro ativo: <b>{categoria_ativa}</b> | Motorização: <b>{motorizacao_sel}</b></p>", unsafe_allow_html=True)
    
    # Filtragem de Peças
    partes_filtradas = []
    for p in PARTES:
        match_motor = (motorizacao_sel == "Todas as Motorizações" or p["motorizacao"] == motorizacao_sel or p["motorizacao"] == "Todas as Motorizações")
        match_cat = (categoria_ativa == "Todas as Categorias" or p["categoria"] == categoria_ativa)
        
        texto_busca = pesquisa_livre.lower().strip()
        match_texto = True
        if texto_busca:
            t_limpo = texto_busca.replace("á", "a").replace("-", " ")
            n_limpo = p["nome"].lower().replace("á", "a").replace("-", " ")
            d_limpo = p["descricao"].lower().replace("á", "a").replace("-", " ")
            m_limpo = p["marca"].lower()
            c_limpo = p["codigo"].lower()
            
            match_texto = (
                t_limpo in n_limpo or 
                t_limpo in d_limpo or 
                t_limpo in m_limpo or 
                t_limpo in c_limpo or
                any(t in n_limpo for t in t_limpo.split())
            )
            
        if match_motor and match_cat and match_texto:
            partes_filtradas.append(p)

    if not partes_filtradas:
        st.warning("Nenhuma peça encontrada com os critérios especificados. Tente pesquisar por outro termo (ex: 'filtro', 'óleo', 'travão').")
    else:
        # Exibição em grelha de 2 colunas para os produtos
        for i in range(0, len(partes_filtradas), 2):
            c1, c2 = st.columns(2)
            
            with c1:
                if i < len(partes_filtradas):
                    peca = partes_filtradas[i]
                    renderizar_cartao(peca)
                    
            with c2:
                if i + 1 < len(partes_filtradas):
                    peca = partes_filtradas[i + 1]
                    renderizar_cartao(peca)
