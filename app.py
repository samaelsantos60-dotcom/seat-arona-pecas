import streamlit as st
from data import CATEGORIAS, CATEGORIAS_ACESSORIOS, MODELOS, MOTORIZACOES, DICAS_GERAIS, LOJAS, PARTES, ACESSORIOS

# Configuração da página em modo wide
st.set_page_config(
    page_title="Norauto / AutoPeças PT - SEAT Arona",
    page_icon="🚗",
    layout="wide"
)

# Base de conhecimento de matrículas em Portugal
MATRICULAS_CONHECIDAS = {
    "13-24-PZ": {"veiculo": "SEAT Arona", "motorizacao": "1.0 TSI (Gasolina)"},
    "48-XT-92": {"veiculo": "SEAT Arona", "motorizacao": "1.6 TDI (Diesel)"},
    "91-AA-05": {"veiculo": "SEAT Arona", "motorizacao": "Todas as Motorizações"},
}

# Inicializar o estado da sessão
if 'veiculo_ativo' not in st.session_state:
    st.session_state.veiculo_ativo = "SEAT Arona"
if 'motorizacao_ativa' not in st.session_state:
    st.session_state.motorizacao_ativa = "1.0 TSI (Gasolina)"
if 'matricula_ativa' not in st.session_state:
    st.session_state.matricula_ativa = "13-24-PZ"
if 'mostrar_modal' not in st.session_state:
    st.session_state.mostrar_modal = False

# Estilo CSS personalizado
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
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
    .badge-acessorio {
        background-color: #e0f2fe;
        color: #0369a1;
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
    .modal-box {
        background-color: #ffffff;
        border: 2px solid #f59e0b;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# Função para renderizar cartões de produtos (Peças ou Acessórios)
def renderizar_cartao(item, tipo="peca"):
    url_loja = item['link_compra']
    nome_loja = "Loja Online"
    for loja in LOJAS:
        if loja['url'] in url_loja:
            nome_loja = loja['nome']
            break
            
    badge_classe = "badge-cat" if tipo == "peca" else "badge-acessorio"
    
    st.markdown(f"""
        <div class="product-card">
            <span class="{badge_classe}">{item['categoria']}</span>
            <h4 style="margin-top: 8px; margin-bottom: 5px; color: #111827; font-size: 16px;">{item['nome']}</h4>
            <p style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">Marca: <b>{item['marca']}</b> | Ref: <code>{item['codigo']}</code></p>
            <p style="font-size: 13px; color: #374151; margin-bottom: 10px;">{item['descricao']}</p>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 15px;">
                <span class="price-tag">{item['preco']:.2f} €</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button(f"🛒 Ver em {nome_loja}", url_loja, use_container_width=True)
    st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

# Cabeçalho Superior Fixo
col_top1, col_top2 = st.columns([3, 1])
with col_top1:
    st.markdown("""
        <div style="padding-top: 5px;">
            <span class="logo-text">NORAUTO</span> &nbsp;|&nbsp; <span style="font-size: 16px; color: #6b7280;">AutoPeças PT</span>
        </div>
    """, unsafe_allow_html=True)

with col_top2:
    if st.button(f"🚗 {st.session_state.veiculo_ativo} ({st.session_state.matricula_ativa})", use_container_width=True):
        st.session_state.mostrar_modal = not st.session_state.mostrar_modal

st.markdown("<hr style='margin: 10px 0 20px 0;'>", unsafe_allow_html=True)

# MODAL DE MATRÍCULA
if st.session_state.mostrar_modal:
    with st.container():
        st.markdown("""
            <div class="modal-box">
                <h2 style="color: #111827; margin-top: 0; font-size: 22px;">Identifique o seu veículo por matrícula</h2>
                <p style="color: #4b5563; font-size: 14px;">Insira a matrícula para desbloquear peças e acessórios compatíveis.</p>
                <p style="font-size: 12px; color: #9ca3af;">💡 Experimente: <code>13-24-PZ</code> (Gasolina 1.0) ou <code>48-XT-92</code> (Diesel 1.6)</p>
            </div>
        """, unsafe_allow_html=True)
        
        col_m1, col_m2, col_m3 = st.columns([2, 1, 1])
        with col_m1:
            input_mat = st.text_input("Matrícula do veículo", value=st.session_state.matricula_ativa, placeholder="Ex: 13-24-PZ")
        with col_m2:
            st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
            if st.button("Pesquisar Matrícula", type="primary", use_container_width=True):
                mat_limpa = input_mat.upper().strip()
                if mat_limpa in MATRICULAS_CONHECIDAS:
                    st.session_state.matricula_ativa = mat_limpa
                    st.session_state.veiculo_ativo = MATRICULAS_CONHECIDAS[mat_limpa]["veiculo"]
                    st.session_state.motorizacao_ativa = MATRICULAS_CONHECIDAS[mat_limpa]["motorizacao"]
                else:
                    st.session_state.matricula_ativa = mat_limpa or "AA-00-BB"
                    st.session_state.veiculo_ativo = "SEAT Arona"
                    st.session_state.motorizacao_ativa = "Todas as Motorizações"
                st.session_state.mostrar_modal = False
                st.rerun()
        with col_m3:
            st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
            if st.button("Fechar", use_container_width=True):
                st.session_state.mostrar_modal = False
                st.rerun()
        st.markdown("---")

# **NOVO**: Seletor Principal de Secção (Peças vs Acessórios)
seccao_principal = st.radio(
    "Escolha a Seção",
    ["🛠️ Peças Auto e Manutenção", "🎒 Acessórios e Equipamentos"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("")

# Aba dinâmica consoante a escolha do utilizador
if seccao_principal == "🛠️ Peças Auto e Manutenção":
    categoria_ativa = st.radio(
        "Categorias Peças",
        ["Todas as Categorias"] + CATEGORIAS,
        horizontal=True,
        label_visibility="collapsed"
    )
    st.markdown("---")
    
    col_search, col_info = st.columns([3, 1])
    with col_search:
        pesquisa_livre = st.text_input("Pesquisa Peças", placeholder="🔍 Pesquisar peça (ex: óleo, filtro, travão...)", label_visibility="collapsed")
    with col_info:
        st.markdown(f"<div style='background-color:#e5e7eb; padding:8px 12px; border-radius:6px; font-size:13px; text-align:center;'>⚙️ Motor: <b>{st.session_state.motorizacao_ativa}</b></div>", unsafe_allow_html=True)

    st.markdown("")
    
    # Filtro de Peças
    itens_filtrados = []
    motor_atual = st.session_state.motorizacao_ativa
    for p in PARTES:
        match_motor = (motor_atual == "Todas as Motorizações" or p["motorizacao"] == motor_atual or p["motorizacao"] == "Todas as Motorizações")
        match_cat = (categoria_ativa == "Todas as Categorias" or p["categoria"] == categoria_ativa)
        
        texto_busca = pesquisa_livre.lower().strip()
        match_texto = True
        if texto_busca:
            t_limpo = texto_busca.replace("á", "a").replace("-", " ")
            n_limpo = p["nome"].lower().replace("á", "a").replace("-", " ")
            d_limpo = p["descricao"].lower().replace("á", "a").replace("-", " ")
            match_texto = (t_limpo in n_limpo or t_limpo in d_limpo or t_limpo in p["marca"].lower())
            
        if match_motor and match_cat and match_texto:
            itens_filtrados.append((p, "peca"))

else:
    categoria_ativa = st.radio(
        "Categorias Acessórios",
        ["Todas as Categorias"] + CATEGORIAS_ACESSORIOS,
        horizontal=True,
        label_visibility="collapsed"
    )
    st.markdown("---")
    
    col_search, col_info = st.columns([3, 1])
    with col_search:
        pesquisa_livre = st.text_input("Pesquisa Acessórios", placeholder="🔍 Pesquisar acessório (ex: barras, tapetes, suporte...)", label_visibility="collapsed")
    with col_info:
        st.markdown(f"<div style='background-color:#e0f2fe; padding:8px 12px; border-radius:6px; font-size:13px; text-align:center; color:#0369a1;'>🚗 Veículo: <b>{st.session_state.veiculo_ativo}</b></div>", unsafe_allow_html=True)

    st.markdown("")
    
    # Filtro de Acessórios
    itens_filtrados = []
    veiculo_atual = st.session_state.veiculo_ativo
    for a in ACESSORIOS:
        match_veiculo = (a["veiculo_compativel"] == "Universal" or a["veiculo_compativel"].lower() in veiculo_atual.lower())
        match_cat = (categoria_ativa == "Todas as Categorias" or a["categoria"] == categoria_ativa)
        
        texto_busca = pesquisa_livre.lower().strip()
        match_texto = True
        if texto_busca:
            t_limpo = texto_busca.replace("á", "a").replace("-", " ")
            n_limpo = a["nome"].lower().replace("á", "a").replace("-", " ")
            d_limpo = a["descricao"].lower().replace("á", "a").replace("-", " ")
            match_texto = (t_limpo in n_limpo or t_limpo in d_limpo or t_limpo in a["marca"].lower())
            
        if match_veiculo and match_cat and match_texto:
            itens_filtrados.append((a, "acessorio"))

# Layout Principal em Colunas
col_esq, col_dir = st.columns([1, 3])

with col_esq:
    st.markdown("### ⚡ Vantagens Norauto")
    st.markdown("""
    <div style="background-color: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #e5e7eb;">
        <ul style="padding-left: 15px; margin: 0; font-size: 13px; color: #4b5563; line-height: 2.2;">
            <li><b>Montagem Gratuita</b> em oficinas parceiras</li>
            <li>Entrega em 24/48h em Portugal</li>
            <li>Garantia de compatibilidade por matrícula</li>
            <li>Devolução até 30 dias</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("💡 Dicas Técnicas")
    for dica in DICAS_GERAIS:
        st.info(dica)

with col_dir:
    st.markdown(f"### Catálogo Compatível com Matrícula `{st.session_state.matricula_ativa}`")
    st.markdown(f"<p style='color: #6b7280; font-size: 14px;'>Filtro ativo: <b>{categoria_ativa}</b></p>", unsafe_allow_html=True)
    
    if not itens_filtrados:
        st.warning("Nenhum produto encontrado com os critérios especificados.")
    else:
        for i in range(0, len(itens_filtrados), 2):
            c1, c2 = st.columns(2)
            
            with c1:
                if i < len(itens_filtrados):
                    item, tipo = itens_filtrados[i]
                    renderizar_cartao(item, tipo)
                    
            with c2:
                if i + 1 < len(itens_filtrados):
                    item, tipo = itens_filtrados[i + 1]
                    renderizar_cartao(item, tipo)
