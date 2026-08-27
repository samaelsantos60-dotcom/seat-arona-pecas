# Base de dados detalhada por motorização para SEAT Arona (2017+)

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
        "descricao": "Filtro de óleo de alta eficiência para proteção do motor."
    },
    {
        "id": "oleo-motor",
        "nome": "Óleo de Motor 5W30 (5L)",
        "categoria": "Filtros e Fluidos",
        "motorizacao": "Todas as Motorizações",
        "marca": "Castrol Edge Professional",
        "codigo": "LL III 5W-30 (Norma VW 504 00 / 507 00)",
        "preco": 48.90,
        "compatibilidade": "SEAT Arona Gasolina e Diesel",
        "descricao": "Óleo sintético de tecnologia avançada aprovado pelo grupo VAG."
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
        "descricao": "Retém impurezas e garante o fluxo de ar ideal para a admissão."
    },
    {
        "id": "filtro-habitaculo",
        "nome": "Filtro de Habitáculo (Polen/Carvão Ativado)",
        "categoria": "Filtros e Fluidos",
        "motorizacao": "Todas as Motorizações",
        "marca": "Mann-Filter",
        "codigo": "CUK 26 007",
        "preco": 18.50,
        "compatibilidade": "Todos os modelos SEAT Arona",
        "descricao": "Filtro de carvão ativo que remove odores e poluentes do ar exterior."
    },
    {
        "id": "liquido-refrigerante",
        "nome": "Líquido de Refrigeração G12evo / G13 (1L)",
        "categoria": "Filtros e Fluidos",
        "motorizacao": "Todas as Motorizações",
        "marca": "Febi Bilstein",
        "codigo": "22272 (Norma TL 774 L)",
        "preco": 9.80,
        "compatibilidade": "SEAT Arona (Sistema VAG)",
        "descricao": "Anticongelante de longa duração com proteção anticorrosiva."
    },
    {
        "id": "velas-ignicao",
        "nome": "Velas de Ignição (Jogo de 3)",
        "categoria": "Motor e Ignição",
        "motorizacao": "1.0 TSI (Gasolina)",
        "marca": "NGK",
        "codigo": "94201 (PLFER7A8EG)",
        "preco": 36.00,
        "compatibilidade": "SEAT Arona 1.0 TSI",
        "descricao": "Velas de irídio de alta durabilidade para ignição otimizada."
    },
    {
        "id": "bomba-agua",
        "nome": "Bomba de Água / Sistema de Refrigeração",
        "categoria": "Motor e Ignição",
        "motorizacao": "1.0 TSI (Gasolina)",
        "marca": "INA",
        "codigo": "04C121600H",
        "preco": 89.90,
        "compatibilidade": "SEAT Arona 1.0 TSI",
        "descricao": "Módulo de bomba de água com termostato integrado."
    },
    {
        "id": "kit-distribuicao",
        "nome": "Kit de Correia de Distribuição",
        "categoria": "Motor e Ignição",
        "motorizacao": "1.6 TDI (Diesel)",
        "marca": "Gates",
        "codigo": "KP15670XS",
        "preco": 125.00,
        "compatibilidade": "SEAT Arona 1.6 TDI",
        "descricao": "Kit completo com correia dentada, tensores e roletes guias."
    },
    {
        "id": "suporte-motor",
        "nome": "Suporte / Coxim do Motor (Lado Direito)",
        "categoria": "Motor e Ignição",
        "motorizacao": "1.0 TSI (Gasolina)",
        "marca": "Lemförder",
        "codigo": "38435 01",
        "preco": 54.50,
        "compatibilidade": "SEAT Arona 1.0 TSI",
        "descricao": "Absorve vibrações do motor garantindo o conforto a bordo."
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
        "descricao": "Pastilhas de travão com excelente poder de travagem e baixo ruído."
    },
    {
        "id": "discos-travao-frente",
        "nome": "Discos de Travão Dianteiros (Par)",
        "categoria": "Travagem",
        "motorizacao": "Todas as Motorizações",
        "marca": "Brembo",
        "codigo": "09.C693.11",
        "preco": 78.00,
        "compatibilidade": "SEAT Arona (Ventilados)",
        "descricao": "Discos de travão maquinados com alta resistência térmica."
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
        "descricao": "Amortecedores a gás de alto desempenho para estabilidade em curva."
    },
    {
        "id": "lampada-farol-h7",
        "nome": "Lâmpada Farol Principal H7 (Par)",
        "categoria": "Eletricidade e Iluminação",
        "motorizacao": "Todas as Motorizações",
        "marca": "Philips",
        "codigo": "12972PRC1 (Vision H7)",
        "preco": 15.00,
        "compatibilidade": "SEAT Arona (Médios/Máximos)",
        "descricao": "Lâmpada de halogéneo com feixe de luz alargado."
    },
    {
        "id": "escovas-limpa-vidros",
        "nome": "Escovas Limpa-Para-Brisas (Kit Dianteiro)",
        "categoria": "Eletricidade e Iluminação",
        "motorizacao": "Todas as Motorizações",
        "marca": "Bosch",
        "codigo": "Aerotwiin A863S",
        "preco": 24.90,
        "compatibilidade": "SEAT Arona (2017+)",
        "descricao": "Escovas planas aerodinâmicas para limpeza silenciosa e sem marcas."
    }
]
