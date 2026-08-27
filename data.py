# Base de dados completa de peças e estruturas para SEAT Arona (2017+)

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

DICAS_GERAIS = [
    "Verifique sempre a referência OEM antes de efetuar a substituição.",
    "Para motores 1.0 TSI, utilize exclusivamente óleos com norma VW 504 00 / 507 00."
]

LOJAS = [
    {"nome": "AutoDoc Online", "url": "https://www.autodoc.pt"},
    {"nome": "Oscaro Portugal", "url": "https://www.oscaro.pt"}
]

PARTES = [
    # --- FILTROS E FLUIDOS ---
    {
        "id": "filtro-oleo",
        "nome": "Filtro de Óleo",
        "categoria": "Filtros e Fluidos",
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
        "marca": "Bosch",
        "codigo": "F 026 400 529",
        "preco": 14.20,
        "compatibilidade": "SEAT Arona 1.0 TSI / 1.6 TDI",
        "descricao": "Retém impurezas e garante o fluxo de ar ideal para a admissão."
    },
    {
        "id": "filtro-habitaculo",
        "nome": "Filtro de Habitáculo (Polen/Carvão Ativado)",
        "categoria": "Filtros e Fluidos",
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
        "marca": "Febi Bilstein",
        "codigo": "22272 (Norma TL 774 L)",
        "preco": 9.80,
        "compatibilidade": "SEAT Arona (Sistema VAG)",
        "descricao": "Anticongelante de longa duração com proteção anticorrosiva."
    },

    # --- MOTOR E IGNIÇÃO ---
    {
        "id": "velas-ignicao",
        "nome": "Velas de Ignição (Jogo de 3)",
        "categoria": "Motor e Ignição",
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
        "marca": "Gates",
        "codigo": "KP15670XS",
        "preco": 125.00,
        "compatibilidade": "SEAT Arona 1.6 TDI / 1.0 TSI",
        "descricao": "Kit completo com correia dentada, tensores e roletes guias."
    },
    {
        "id": "suporte-motor",
        "nome": "Suporte / Coxim do Motor (Lado Direito)",
        "categoria": "Motor e Ignição",
        "marca": "Lemförder",
        "codigo": "38435 01",
        "preco": 54.50,
        "compatibilidade": "SEAT Arona 1.0 TSI",
        "descricao": "Absorve vibrações do motor garantindo o conforto a bordo."
    },

    # --- TRAVAGEM ---
    {
        "id": "pastilhas-travao-frente",
        "nome": "Pastilhas de Travão Dianteiras (Jogo)",
        "categoria": "Travagem",
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
        "marca": "Brembo",
        "codigo": "09.C693.11",
        "preco": 78.00,
        "compatibilidade": "SEAT Arona (Ventilados)",
        "descricao": "Discos de travão maquinados com alta resistência térmica."
    },
    {
        "id": "pastilhas-travao-tras",
        "nome": "Pastilhas de Travão Traseiras (Jogo)",
        "categoria": "Travagem",
        "marca": "Textar",
        "codigo": "2568301",
        "preco": 32.50,
        "compatibilidade": "SEAT Arona (Eixo Traseiro com travão de disco)",
        "descricao": "Qualidade de origem para máxima segurança traseira."
    },

    # --- SUSPENSÃO E DIREÇÃO ---
    {
        "id": "amortecedores-frente",
        "nome": "Amortecedores Dianteiros (Par)",
        "categoria": "Suspensão e Direção",
        "marca": "Sachs",
        "codigo": "318 534",
        "preco": 145.00,
        "compatibilidade": "SEAT Arona (Suspensão Standard)",
        "descricao": "Amortecedores a gás de alto desempenho para estabilidade em curva."
    },
    {
        "id": "amortecedores-tras",
        "nome": "Amortecedores Traseiros (Par)",
        "categoria": "Suspensão e Direção",
        "marca": "Bilstein",
        "codigo": "19-291778",
        "preco": 85.00,
        "compatibilidade": "SEAT Arona (Eixo Traseiro)",
        "descricao": "Conforto e aderência superior em piso irregular."
    },
    {
        "id": "braco-suspensao",
        "nome": "Braço / Triplo de Suspensão Inferior (Direito/Esquerdo)",
        "categoria": "Suspensão e Direção",
        "marca": "MOOG",
        "codigo": "VO-TC-14389",
        "preco": 68.00,
        "compatibilidade": "SEAT Arona (Dianteiro)",
        "descricao": "Braço de suspensão reforçado com rótula e casquilhos incluídos."
    },

    # --- ELETRICIDADE E ILUMINAÇÃO ---
    {
        "id": "lampada-farol-h7",
        "nome": "Lâmpada Farol Principal H7 (Par)",
        "categoria": "Eletricidade e Iluminação",
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
        "marca": "Bosch",
        "codigo": "Aerotwiin A863S",
        "preco": 24.90,
        "compatibilidade": "SEAT Arona (2017+)",
        "descricao": "Escovas planas aerodinâmicas para limpeza silenciosa e sem marcas."
    }
]
