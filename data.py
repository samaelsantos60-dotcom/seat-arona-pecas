CATEGORIAS = [
    "Revisão e Óleos",
    "Travões",
    "Filtros",
    "Escovas Limpa-Para-Brisas",
    "Iluminação",
    "Pneus e Jantes"
]

CATEGORIAS_ACESSORIOS = [
    "Transporte e Carga (Barras/Suportes)",
    "Interior e Conforto (Tapetes/Capas)",
    "Tecnologia e Eletrónica",
    "Manutenção e Limpeza"
]

MODELOS = ["SEAT Arona", "Renault Clio", "Peugeot 2008", "Volkswagen Golf"]

MOTORIZACOES = [
    "Todas as Motorizações",
    "1.0 TSI (Gasolina)",
    "1.6 TDI (Diesel)"
]

DICAS_GERAIS = [
    "Verifique sempre a referência OEM antes de efetuar a substituição.",
    "Para motores 1.0 TSI, utilize exclusivamente óleos com norma VW 504 00 / 507 00."
]

LOJAS = [
    {"nome": "AutoDoc", "url": "https://www.autodoc.pt"},
    {"nome": "Oscaro", "url": "https://www.oscaro.es"},
    {"nome": "Norauto Portugal", "url": "https://www.norauto.pt"},
    {"nome": "Mister-Auto", "url": "https://www.mister-auto.pt"}
]

# Peças mecânicas existentes
PARTES = [
    {
        "nome": "Óleo de Motor 5W30 LongLife 5L",
        "marca": "Castrol Edge",
        "codigo": "1535F6",
        "preco": 54.90,
        "categoria": "Revisão e Óleos",
        "motorizacao": "1.0 TSI (Gasolina)",
        "descricao": "Óleo sintético de alta performance compatível com a norma VW 504 00 / 507 00.",
        "link_compra": "https://www.autodoc.pt/castrol/1535f6"
    },
    {
        "nome": "Filtro de Óleo Mann-Filter",
        "marca": "Mann-Filter",
        "codigo": "HU 6013 z",
        "preco": 12.50,
        "categoria": "Filtros",
        "motorizacao": "1.0 TSI (Gasolina)",
        "descricao": "Filtro de óleo de elevada retenção de impurezas para motores do grupo VAG.",
        "link_compra": "https://www.oscaro.es/filtro-de-aceite-mann-filter-hu-6013-z"
    },
    {
        "nome": "Jogo de Pastilhas de Travão Dianteiras",
        "marca": "Brembo",
        "codigo": "P 85 158",
        "preco": 42.00,
        "categoria": "Travões",
        "motorizacao": "Todas as Motorizações",
        "descricao": "Pastilhas de travão com excelente poder de travagem e baixo ruído.",
        "link_compra": "https://www.norauto.pt/pastilhas-de-travao"
    },
    {
        "nome": "Escovas Limpa-Para-Brisas Aerotwin",
        "marca": "Bosch",
        "codigo": "A 863 S",
        "preco": 28.90,
        "categoria": "Escovas Limpa-Para-Brisas",
        "motorizacao": "Todas as Motorizações",
        "descricao": "Conjunto de escovas dianteiras planas específicas para SEAT Arona.",
        "link_compra": "https://www.mister-auto.pt/escovas-bosch"
    }
]

# **NOVO**: Lista de Acessórios dedicados/compatíveis com o veículo
ACESSORIOS = [
    {
        "nome": "Barras de Tejadilho em Alumínio",
        "marca": "Norauto / Thule",
        "codigo": "NOR-BA-882",
        "preco": 149.99,
        "categoria": "Transporte e Carga (Barras/Suportes)",
        "veiculo_compativel": "SEAT Arona",
        "descricao": "Barras de tejadilho aerodinâmicas específicas com kit de fixação integrado para SEAT Arona com barras longitudinais.",
        "link_compra": "https://www.norauto.pt/barras-tejadilho"
    },
    {
        "nome": "Tapetes de Borracha à Medida (Gama Alta)",
        "marca": "Gledring",
        "codigo": "GL-0592-SEAT",
        "preco": 49.90,
        "categoria": "Interior e Conforto (Tapetes/Capas)",
        "veiculo_compativel": "SEAT Arona",
        "descricao": "Jogo de 4 tapetes em borracha com rebordo elevado e aroma a baunilha, desenhados à medida para o habitáculo do SEAT Arona.",
        "link_compra": "https://www.autodoc.pt/tapetes-borracha"
    },
    {
        "nome": "Suporte de Telemóvel Magnético para Grelha de Ventilação",
        "marca": "Ugreen",
        "codigo": "UG-MAG-01",
        "preco": 15.99,
        "categoria": "Tecnologia e Eletrónica",
        "veiculo_compativel": "Universal",
        "descricao": "Suporte magnético robusto com rotação de 360º para smartphones.",
        "link_compra": "https://www.norauto.pt/tecnologia"
    },
    {
        "nome": "Kit de Lavagem e Limpeza Rápida com Balde",
        "marca": "Meguiar's",
        "codigo": "MEG-KIT-PRO",
        "preco": 34.50,
        "categoria": "Manutenção e Limpeza",
        "veiculo_compativel": "Universal",
        "descricao": "Kit completo com champô, luva de microfibra e toalha de secagem para a pintura do carro.",
        "link_compra": "https://www.norauto.pt/limpeza"
    }
]
