# AutoPeças PT

Aplicação web em Python com **Streamlit** para o mercado português, focada em peças, acessórios, pneus e ferramentas para automóveis — com foco inicial no **SEAT Arona** e no grupo **VAG** (SEAT, VW, Audi, Skoda).

## Funcionalidades

- **Menu de categorias completo:**
  1. Óleos e Fluidos (com normas VAG: 507.00, 508.00, TL 774, DOT 4...)
  2. Peças de Desgaste e Motor (filtros, travões, correias, velas, bateria)
  3. Pneus e Jantes (com medidas 215/55 R17, 215/45 R18, TPMS...)
  4. Acessórios e Interior (tapetes, escovas, lâmpadas, barras)
  5. Ferramentas de Oficina (chave dinamométrica, scanner OBD2, macaco...)

- **Pesquisa por texto livre** em toda a base de dados (nome, normas, referências OEM, aplicações, marcas).
- **Dicas de equivalência de marcas brancas** (concorrência OEM) para poupar 30-60%: original / equivalente / económico.
- **Links de pesquisa direta** para lojas online de Portugal (Autodoc, Mister-Auto, Norauto, Feu Vert, Oscaro, Sadas) via Google site-search.
- Filtro por **modelo** e **referências OEM (VAG)**.

## Executar

```bash
pip install -r requirements.txt
streamlit run app.py
```

A aplicação fica disponível em `http://localhost:8501`.

## Estrutura

- `app.py` — interface Streamlit (menu, pesquisa, detalhes, lojas).
- `data.py` — base de dados de peças, categorias, equivalências e lojas.

## Aviso

As referências OEM indicadas são comuns aos motores EA211/EA288 do Arona. Confirme sempre a compatibilidade com o **VIN** do veículo antes de comprar.
