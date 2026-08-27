# Base de dados com links diretos de compra para SEAT Arona (2017+)

CATEGORIAS = [
    "Filtros e Fluidos",
    "Motor e Ignição",
    "Travagem",
    "Suspensão e Direção",
    "Eletricidade e Iluminação"
]

MODELOS = [
    "SEAT Arona (2017+)"
]

MOTORIZACOES = [
    "Todas as Motorizações",
    "1.0 TSI (Gasolina)",
    "1.6 TDI (Diesel)",
    "1.5 TSI / Outras"
]

DICAS_GERAIS = [
    "Verifique sempre a referência OEM antes de efetuar a substituição.",
    "Para motores 1.0 TSI, utilize exclusivamente óleos com norma VW 504 00 / 507 00."
]

LOJAS = [
    {"nome": "AutoDoc Online", "dominio": "autodoc.pt", "url": "https://www.autodoc.pt"},
    {"nome": "Oscaro Portugal", "dominio": "oscaro.pt", "url": "https://www.oscaro.pt"},
    {"nome": "Norauto", "dominio": "norauto.pt", "url": "https://www.norauto.pt"}
]

PARTES = [
    {
        "id": "filtro-oleo",
        "nome": "Filtro de Óleo",
        "categoria": "Filtros e Fluidos",
        "motorizacao": "Todas as Motorizações",
        "marca": "Mann-Filter",
        "codigo": "W 712/95",
        "preco": 11.50,
        "compatibilidade": "SEAT Arona 1.0 TSI / 1.6 TDI",
        "descricao": "Filtro de óleo de alta eficiência para proteção do motor.",
        "link_compra": "https://www.autodoc.pt/search?keyword=W+712%2F95"
    },
    {
        "id": "oleo-motor",
        "nome": "Óleo de Motor 5W30 (5L)",
        "categoria": "Filtros e Fluidos",
        "motorizacao": "Todas as Motorizações",
        "marca": "Castrol Edge Professional",
        "codigo": "LL III 5W-30",
        "preco": 48.90,
        "compatibilidade": "SEAT Arona Gasolina e Diesel",
        "descricao": "Óleo sintético de tecnologia avançada aprovado pelo grupo VAG.",
        "link_compra": "https://www.autodoc.pt/search?keyword=Castrol+Edge+5W30+LL+III"
    },
    {
        "id": "filtro-ar",
        "nome": "Filtro de Ar do Motor",
        "categoria": "Filtros e Fluidos",
        "motorizacao": "1.0 TSI (Gasolina)",
        "marca": "Bosch",
        "codigo": "F 026 400 529",
        "preco": 14.20,
        "compatibilidade": "SEAT Arona 1.0 TSI",
        "descricao": "Retém impurezas e garante o fluxo de ar ideal para a admissão.",
        "link_compra": "https://www.autodoc.pt/search?keyword=F+026+400+529"
    },
    {
        "id": "velas-ignicao",
        "nome": "Velas de Ignição (Jogo de 3)",
        "categoria": "Motor e Ignição",
        "motorizacao": "1.0 TSI (Gasolina)",
        "marca": "NGK",
        "codigo": "94201",
        "preco": 36.00,
        "compatibilidade": "SEAT Arona 1.0 TSI",
        "descricao": "Velas de irídio de alta durabilidade para ignição otimizada.",
        "link_compra": "https://www.autodoc.pt/search?keyword=NGK+94201"
    },
    {
        "id": "pastilhas-travao-frente",
        "nome": "Pastilhas de Travão Dianteiras (Jogo)",
        "categoria": "Travagem",
        "motorizacao": "Todas as Motorizações",
        "marca": "Brembo",
        "codigo": "P 85 150",
        "preco": 39.90,
        "compatibilidade": "SEAT Arona (Eixo Dianteiro)",
        "descricao": "Pastilhas de travão com excelente poder de travagem e baixo ruído.",
        "link_compra": "https://www.autodoc.pt/search?keyword=P+85+150"
    },
    {
        "id": "amortecedores-frente",
        "nome": "Amortecedores Dianteiros (Par)",
        "categoria": "Suspensão e Direção",
        "motorizacao": "Todas as Motorizações",
        "marca": "Sachs",
        "codigo": "318 534",
        "preco": 145.00,
        "compatibilidade": "SEAT Arona (Suspensão Standard)",
        "descricao": "Amortecedores a gás de alto desempenho para estabilidade em curva.",
        "link_compra": "https://www.autodoc.pt/search?keyword=318+534"
    },
    {
        "id": "escovas-limpa-vidros",
        "nome": "Escovas Limpa-Para-Brisas (Kit Dianteiro)",
        "categoria": "Eletricidade e Iluminação",
        "motorizacao": "Todas as Motorizações",
        "marca": "Bosch",
        "codigo": "A863S",
        "preco": 24.90,
        "compatibilidade": "SEAT Arona (2017+)",
        "descricao": "Escovas planas aerodinâmicas para limpeza silenciosa e sem marcas.",
        "link_compra": "https://www.autodoc.pt/search?keyword=Bosch+A863S"
    }
]
