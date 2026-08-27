import unicodedata
from urllib.parse import quote_plus

import streamlit as st

from data import CATEGORIAS, DICAS_GERAIS, LOJAS, MODELOS, PARTES
from produtos import PRODUTOS

st.set_page_config(
    page_title="AutoPeças PT | SEAT Arona & VAG",
    layout="wide",
    initial_sidebar_state="expanded",
)

PAGINAS = {
    "Catálogo de Peças": "catalogo",
    "Dicas para Poupar": "dicas",
    "Lojas Recomendadas": "lojas",
}

LOJAS_RAPIDAS = [
    loja for loja in LOJAS if loja["dominio"] in ("autodoc.pt", "norauto.pt", "oscaro.pt")
]

CHIPS_COLORES = {
    "normas": "#0d47a1",
    "especificacoes": "#00695c",
}


def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto if unicodedata.category(c) != "Mn").lower()


def chips(lista, cor="#0d47a1"):
    if not lista:
        return ""
    itens = "".join(
        f'<span style="background:{cor};color:#fff;padding:2px 10px;border-radius:12px;'
        f'font-size:13px;margin-right:6px;white-space:nowrap;">{item}</span>'
        for item in lista
    )
    return itens


def google_site_search(consulta, dominio):
    return "https://www.google.com/search?q=" + quote_plus(consulta + " site:" + dominio)


def filtro_partes(pesquisa, categoria, modelo):
    q = normalizar(pesquisa) if pesquisa else ""
    resultado = []
    for parte in PARTES:
        if categoria and parte["categoria"] != categoria:
            continue
        if modelo and modelo not in parte["aplicacoes"]:
            continue
        if q:
            produtos_texto = " ".join(
                " ".join([p.get("marca", ""), p.get("codigo", ""), p.get("nome", ""), p.get("preco", "")])
                for p in PRODUTOS.get(parte["id"], [])
            )
            campo = " ".join(
                [
                    parte["nome"],
                    parte["descricao"],
                    parte["categoria"],
                    " ".join(parte.get("normas", [])),
                    " ".join(parte.get("especificacoes", [])),
                    " ".join(parte.get("aplicacoes", [])),
                    " ".join(parte.get("referencias", [])),
                    parte["marcas"]["original"],
                    parte["marcas"]["equivalente"],
                    parte["marcas"]["economica"],
                    produtos_texto,
                ]
            )
            if q not in normalizar(campo):
                continue
        resultado.append(parte)
    return resultado


def render_lojas(parte, modelo_sel):
    consulta = parte["nome"]
    if modelo_sel and modelo_sel != "Todos os modelos":
        consulta += " " + modelo_sel
    if parte["referencias"]:
        consulta += " " + parte["referencias"][0]
    with st.expander("Pesquisar em lojas online de Portugal (opcional)"):
        cols = st.columns(len(LOJAS))
        for col, loja in zip(cols, LOJAS):
            with col:
                st.link_button(f"{loja['nome']}", google_site_search(consulta, loja["dominio"]))
                st.caption(loja["nota"])
        for loja in LOJAS:
            st.markdown(
                f"- [{loja['nome']}]({loja['site']}) — {loja['nota']}"
            )


def render_produtos(parte):
    produtos = PRODUTOS.get(parte["id"], [])
    if not produtos:
        return
    exata = produtos[0]
    unidade = f" ({exata['unidade']})" if exata.get("unidade") else ""
    st.success(
        f"**Peça exata:** {exata['marca']} **{exata.get('codigo') or '—'}**"
        f" — {exata.get('nome', '')} — **{exata['preco']}**{unidade}"
    )
    linhas = [
        "| Nível | Marca | Código do fabricante | Preço de referência |",
        "|:--|:--|:--|--:|",
    ]
    for i, p in enumerate(produtos):
        codigo = p.get("codigo") or "—"
        if i == 0:
            linhas.append(f"| **{p.get('nivel', '')}** | **{p['marca']}** | **{codigo}** | **{p['preco']}** |")
        else:
            linhas.append(f"| {p.get('nivel', '')} | {p['marca']} | {codigo} | {p['preco']} |")
    st.markdown("\n".join(linhas))
    st.caption(
        "Preços de referência indicativos (mercado PT). Confirme sempre o código pela aplicação exata "
        "do veículo (VIN) antes de comprar."
    )


def render_part(parte, modelo_sel):
    with st.expander(parte["nome"], expanded=True):
        st.markdown(parte["descricao"])
        st.markdown(chips(parte.get("normas", []), CHIPS_COLORES["normas"]) + chips(parte.get("especificacoes", []), CHIPS_COLORES["especificacoes"]), unsafe_allow_html=True)
        st.markdown("**Aplicações:** " + ", ".join(parte["aplicacoes"]))
        st.markdown(
            "**Referências OEM (VAG):** "
            + "".join(
                f'<code style="background:#263238;color:#80cbc4;padding:2px 6px;border-radius:4px;margin-right:6px;">{ref}</code>'
                for ref in parte["referencias"]
            ),
            unsafe_allow_html=True,
        )
        render_produtos(parte)
        c1, c2, c3 = st.columns(3)
        c1.markdown("**Original (OEM)**\n\n" + parte["marcas"]["original"])
        c2.markdown("**Equivalente**\n\n" + parte["marcas"]["equivalente"])
        c3.markdown("**Marcas brancas / Económico**\n\n" + parte["marcas"]["economica"])
        st.info("**Dica para poupar:** " + parte["dica"])
        extra = []
        if parte.get("quando_trocar"):
            extra.append("**Quando trocar:** " + parte["quando_trocar"])
        if parte.get("quantidade"):
            extra.append("**Quantidade:** " + parte["quantidade"])
        if extra:
            st.markdown("  \n".join(extra))
        render_lojas(parte, modelo_sel)


def pagina_catalogo(modelo_sel):
    st.markdown("## Catálogo de Peças")
    st.caption("Peças, normas, equivalências e preços de referência para o SEAT Arona e grupo VAG.")
    st.markdown("---")
    c_sel, m_sel = st.columns(2)
    with c_sel:
        cat_opcoes = ["Todas as categorias"] + list(CATEGORIAS.keys())
        cat_opcoes_nome = {k: CATEGORIAS[k]["nome"] for k in CATEGORIAS}
        cat_selecionada = st.selectbox(
            "Categoria", cat_opcoes, format_func=lambda x: "Todas as categorias" if x == "Todas as categorias" else cat_opcoes_nome[x]
        )
    with m_sel:
        modelo = st.selectbox("Modelo", ["Todos os modelos"] + MODELOS)
    pesquisa = st.text_input(
        "Pesquisa livre (ex.: filtro de óleo, 04E115561C, pastilhas, 215/55 R17, scanner OBD2...)",
        placeholder="Escreva qualquer peça, norma, referência OEM ou medida...",
    )
    st.markdown("---")

    cat_chave = None if cat_selecionada == "Todas as categorias" else cat_selecionada
    modelo_utilizado = None if modelo == "Todos os modelos" else modelo
    resultados = filtro_partes(pesquisa, cat_chave, modelo_utilizado)

    if not resultados:
        if pesquisa.strip():
            pagina_sem_resultados(pesquisa)
        else:
            st.warning("Nenhuma peça encontrada. Tente termos mais genéricos, uma referência OEM ou o nome de uma marca.")
        return

    st.markdown(f"**{len(resultados)} resultado(s)**")
    for parte in resultados:
        render_part(parte, modelo_utilizado)


def pagina_sem_resultados(pesquisa):
    termo = pesquisa.strip()
    st.warning(f"Não encontramos **\"{termo}\"** na base interna de peças.")
    cols = st.columns(len(LOJAS_RAPIDAS))
    for col, loja in zip(cols, LOJAS_RAPIDAS):
        with col:
            st.link_button(
                f"Pesquisar em {loja['nome']}",
                google_site_search(termo, loja["dominio"]),
                width="stretch",
            )
            st.caption(loja["nota"])
    st.markdown(
        "Pesquise a peça nas lojas online de Portugal com o termo exato **"
        + termo
        + "** — qualquer peça, acessório ou ferramenta."
    )
    st.markdown("---")
    with st.expander("Outras formas de pesquisar"):
        st.markdown(
            f"- [Pesquisa geral no Google](https://www.google.com/search?q={quote_plus(termo)})"
        )
        for loja in LOJAS:
            st.markdown(f"- [{loja['nome']}]({loja['site']}) — {loja['nota']}")


def pagina_dicas():
    st.markdown("## Dicas para Poupar Dinheiro")
    st.caption("Como poupar 30-60% em peças VAG sem comprometer a segurança.")
    st.markdown("---")
    for dica in DICAS_GERAIS:
        st.subheader(dica["titulo"])
        st.markdown(dica["texto"])
        st.markdown("---")
    st.info(
        "**Regra de ouro:** para peças de segurança (travagem, pneus, suspensão) exija certificação "
        "ECE R90 / etiqueta UE. Para o resto, as marcas brancas com a norma VAG correta são uma boa escolha."
    )


def pagina_lojas():
    st.markdown("## Lojas Recomendadas em Portugal")
    st.caption("Lojas online e redes físicas onde pesquisar peças por matrícula, VIN ou referência OEM.")
    st.markdown("---")
    for loja in LOJAS:
        c1, c2 = st.columns([1, 3])
        with c1:
            st.link_button(f"Abrir {loja['nome']}", loja["site"])
        with c2:
            st.markdown(f"**{loja['nome']}** — {loja['nota']}")
        st.markdown("---")
    st.info(
        "Dica: em qualquer uma destas lojas use a **pesquisa por matrícula ou VIN** para garantir "
        "a compatibilidade exata com o seu SEAT Arona."
    )


def main():
    st.title("AutoPeças PT")
    st.markdown(
        "Catálogo inteligente de peças, acessórios, pneus e ferramentas para automóveis — "
        "**foco inicial no SEAT Arona e grupo VAG** (SEAT, VW, Audi, Skoda)."
    )

    with st.sidebar:
        st.markdown("## Navegação")
        pagina = st.radio("Menu", list(PAGINAS.keys()), label_visibility="collapsed")
        st.markdown("---")
        st.markdown("**Filtro rápido**")
        modelo_sel = st.selectbox("Modelo de referência", ["Todos os modelos"] + MODELOS)
        st.markdown("---")
        st.caption(
            "As referências OEM apresentadas são comuns ao Arona/motores EA211 e EA288. "
            "Confirme sempre a compatibilidade com o VIN do veículo antes de comprar."
        )

    if PAGINAS[pagina] == "catalogo":
        pagina_catalogo(modelo_sel)
    elif PAGINAS[pagina] == "dicas":
        pagina_dicas()
    else:
        pagina_lojas()


main()
