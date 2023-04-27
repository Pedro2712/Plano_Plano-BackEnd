# area comum externa 2m² por quantidade de aptos e 0,5 de area comum interna
# Taxa de Ocupação Maxima por zoneamento
# Tipo = área computável

# CRIAÇÃO DE VARIAVEIS

"""
Assumptions:

    1. A versão sem varanda do ODS 2 tem a projeção da torre como sendo a projeção da torre com varanda menos a área das varandas.
    2. Área circular não conta como área computável no terreo em nenhum zoneamento, nem ZEU. (baseado no que vi na planilha).
    3. Àrea da varanda não conta como área computável nem em ZEU, o que conta em ZEU é somente a área circular.
    4. Área do ático veio faltando para Trovatto. Considerei o mesmo que o do ODS 3, por conta que é o maior ático entre os
       modelos de torre.
    5. Projeção da torre do Trovatto veio faltando. Fiz somando todas as outras áreas do andar (aplicar a mesma lógica para
       os demais tipos de torres geram o valor correto para a projeção).
    6. Trovatto não tem aptos no térreo
    7.
"""

# Coeficientes area equivalente:
coef_atico = 1
coef_laje_cob_desc = 0.5
coef_tipo = 1
coef_vazio_tipo = 0.5
coef_terreo = 1
coef_construcoes_comuns = 1.5
coef_vagas_s_terra = 0.25
coef_jardim_s_terra = 0.25
coef_melhoramento_viario = 0.25
coef_cob_mall = 0.5
coef_mall = 1
coef_reserva_de_calcada = 0.25
coef_ed_garagem = 1
coef_cob_ed_garagem = 0.5

# CA = area computavel/area do terreno
CA_max_zeur2v = 4
CA_max_zeupr2v = 2
CA_max_zemr2v = 2
CA_max_zcr2v = 2
CA_max_zeis1r2v = 2.5
CA_max_zeis2r2v = 4
CA_max_zeis3r2v = 4
CA_max_zeis4r2v = 2
CA_max_zeis5r2v = 4
CA_max_zpir2v = 1.5
CA_max_zeuhmp = 5
CA_max_zeuphmp = 2.5
CA_max_zemhmp = 2.5
CA_max_zchmp = 2.5
CA_max_zmhmp = 2.5
CA_max_zeis1hmp = 2.5
CA_max_zeis2hmp = 4
CA_max_zeis3hmp = 4
CA_max_zeis4hmp = 2
CA_max_zeis5hmp = 4
CA_max_zpihmp = 1.875
CA_max_zeuhis = 6
CA_max_zeuphis = 3
CA_max_zemhis = 3
CA_max_zchis = 3
CA_max_zmhis = 3
CA_max_zeis1his = 2.5
CA_max_zeis2his = 4
CA_max_zeis3his = 4
CA_max_zeis4his = 2
CA_max_zeis5his = 4
CA_max_zdehis = 3
CA_max_zpihis = 2.5

# Valores ed_garagem

metragem_por_vaga = {
    "vaga simples edifício garagem": 20.27,
    "vaga dupla edifício garagem": 17.685,
    "vaga tripla edifício garagem": 13.958,
    "vaga simples e dupla edifício garagem": 18.547,
    "vaga dupla e tripla edifício garagem": 17.168,
    "vaga simples subsolo": 24.32,
    "vaga dupla subsolo": 21.22,
    "vaga tripla subsolo": 17.8,
    "vaga simples e dupla subsolo": 22.26,
    "vaga dupla e tripla subsolo": 20.6,
    "não há não há": 0
}

info_plantas = {
    "ODS 2": {
        9: {
            "atico": 98.82,
            "vazio_tipo": 21.83,
            "laje_cob_desc": 297.96,
            "area_circ": 53.76,
            "area_priv_comput": 222.36,
            "area_priv_n_comput": 0,
            "num_aptos_terreo": 4,
            "area_comput_terreo": 99.6,
            "area_priv_n_comput_terreo": 0

        },
        11: {
            "atico": 98.82,
            "vazio_tipo": 21.83,
            "laje_cob_desc": 354.63,
            "area_circ": 61.41,
            "area_priv_comput": 271.38,
            "area_priv_n_comput": 0,
            "num_aptos_terreo": 6,
            "area_comput_terreo": 149.4,
            "area_priv_n_comput_terreo": 0
        },
        13: {
            "atico": 98.82,
            "vazio_tipo": 21.83,
            "laje_cob_desc": 411.29,
            "area_circ": 69.04,
            "area_priv_comput": 320.4,
            "area_priv_n_comput": 0,
            "num_aptos_terreo": 8,
            "area_comput_terreo": 199.2,
            "area_priv_n_comput_terreo": 0
        },
        15: {
            "atico": 98.82,
            "vazio_tipo": 21.83,
            "laje_cob_desc": 467.96,
            "area_circ": 76.69,
            "area_priv_comput": 369.42,
            "area_priv_n_comput": 0,
            "num_aptos_terreo": 10,
            "area_comput_terreo": 249,
            "area_priv_n_comput_terreo": 0
        },
        17: {
            "atico": 98.82,
            "vazio_tipo": 21.83,
            "laje_cob_desc": 524.63,
            "area_circ": 84.34,
            "area_priv_comput": 418.44,
            "area_priv_n_comput": 0,
            "num_aptos_terreo": 12,
            "area_comput_terreo": 298.8,
            "area_priv_n_comput_terreo": 0
        }
    },
    "ODS 2 Plus": {
        9: {
            "atico": 98.82,
            "vazio_tipo": 21.83,
            "laje_cob_desc": 320.01,
            "area_circ": 53.76,
            "area_priv_comput": 222.36,
            "area_priv_n_comput": 22.05,
            "num_aptos_terreo": 4,
            "area_comput_terreo": 99.6 # AREA CIRC. NÃO CONTA NEM EM ZEU NO TERREO.
        },
        11: {
            "atico": 98.82,
            "vazio_tipo": 21.83,
            "laje_cob_desc": 381.58,
            "area_circ": 61.41,
            "area_priv_comput": 271.38,
            "area_priv_n_comput": 26.95,
            "num_aptos_terreo": 6,
            "area_comput_terreo": 149.4
        },
        13: {
            "atico": 98.82,
            "vazio_tipo": 21.83,
            "laje_cob_desc": 443.14,
            "area_circ": 69.04,
            "area_priv_comput": 320.4,
            "area_priv_n_comput": 31.85,
            "num_aptos_terreo": 8,
            "area_comput_terreo": 199.2
        },
        15: {
            "atico": 98.82,
            "vazio_tipo": 21.83,
            "laje_cob_desc": 504.71,
            "area_circ": 76.69,
            "area_priv_comput": 369.42,
            "area_priv_n_comput": 36.75,
            "num_aptos_terreo": 10,
            "area_comput_terreo": 249
        },
        17: {
            "atico": 98.82,
            "vazio_tipo": 21.83,
            "laje_cob_desc": 566.28,
            "area_circ": 84.34,
            "area_priv_comput": 418.44,
            "area_priv_n_comput": 41.65,
            "num_aptos_terreo": 12,
            "area_comput_terreo": 298.8
        }
    },
    "Eng 3": {
        8: {
            "atico": 120.86,
            "vazio_tipo": 21.94,
            "laje_cob_desc": 317.07,
            "area_circ": 44.95,
            "area_priv_comput": 250.18,
            "area_priv_n_comput": 0,
            "num_aptos_terreo": 5,
            "area_comput_terreo": 156.36,
            "area_priv_n_comput_terreo": 0
        },
        10: {  # REF: 12017 - Rua Ferreira Viana - REF C
            "atico": 120.86,
            "vazio_tipo": 23.40,
            "laje_cob_desc": 398.76,
            "area_circ": 62.64,
            "area_priv_comput": 312.72,
            "area_priv_n_comput": 0,
            "num_aptos_terreo": 6,
            "area_comput_terreo": 187.64,
            "area_priv_n_comput_terreo": 0
        },
        12: {  # REF: 8091 - Edu Chaves - Rev A
            "atico": 120.86,
            "vazio_tipo": 33.79,
            "laje_cob_desc": 478.53,
            "area_circ": 69.47,
            "area_priv_comput": 375.27,
            "area_priv_n_comput": 0,
            "num_aptos_terreo": 8,
            "area_comput_terreo": 250.18,
            "area_priv_n_comput_terreo": 0
        },
    },
    "Eng 3 Plus": {
        8: {
            "atico": 120.86,
            "vazio_tipo": 21.94,
            "laje_cob_desc": 338.27,
            "area_circ": 44.95,
            "area_priv_comput": 250.18,
            "area_priv_n_comput": 21.2,
            "num_aptos_terreo": 5,
            "area_comput_terreo": 156.36,
            "area_priv_n_comput_terreo": 21.2

        },
        10: {  # REF: 12017 - Rua Ferreira Viana - REF C
            "atico": 120.86,
            "vazio_tipo": 23.40,
            "laje_cob_desc": 425.26,
            "area_circ": 62.64,
            "area_priv_comput": 312.72,
            "area_priv_n_comput": 26.5,
            "num_aptos_terreo": 6,
            "area_comput_terreo": 187.64,
            "area_priv_n_comput_terreo": 21.2
        },
        12: {  # REF: 8091 - Edu Chaves - Rev A
            "atico": 120.86,
            "vazio_tipo": 33.79,
            "laje_cob_desc": 510.33,
            "area_circ": 69.47,
            "area_priv_comput": 375.27,
            "area_priv_n_comput": 31.8,
            "num_aptos_terreo": 8,
            "area_comput_terreo": 250.18,
            "area_priv_n_comput_terreo": 21.2
        },
    },
    "Trovatto": {
        8: {
            "atico": 120.86,
            "vazio_tipo": 36.15,
            "laje_cob_desc": 657.79,
            "area_circ": 50,
            "area_priv_comput": 461.45,
            "area_priv_n_comput": 110.2,
            "num_aptos_terreo": 0,
            "area_comput_terreo": 0
        },
    },
    "ODS 6": {
        8: {
            "atico": 110,
            "vazio_tipo": 20.76,
            "laje_cob_desc": 414.42,
            "area_circ": 53.97,
            "area_priv_comput": 339.69,
            "area_priv_n_comput": 0,
            "num_aptos_terreo": 5,
            "area_comput_terreo": 249.6
        },
        10: {
            "atico": 110,
            "vazio_tipo": 34.93,
            "laje_cob_desc": 522.62,
            "area_circ": 68.95,
            "area_priv_comput": 418.74,
            "area_priv_n_comput": 0,
            "num_aptos_terreo": 6,
            "area_comput_terreo": 299.52
        }
    },
    "ODS 6 Plus": {
        8: {
            "atico": 110,
            "vazio_tipo": 20.76,
            "laje_cob_desc": 436.02,
            "area_circ": 53.97,
            "area_priv_comput": 339.69,
            "area_priv_n_comput": 21.6,
            "num_aptos_terreo": 5,
            "area_comput_terreo": 249.6
        },
        10: {
            "atico": 110,
            "vazio_tipo": 34.93,
            "laje_cob_desc": 549.44,
            "area_circ": 68.95,
            "area_priv_comput": 418.74,
            "area_priv_n_comput": 26.82,
            "num_aptos_terreo": 6,
            "area_comput_terreo": 299.52
        }
    },
    "Não Há": {
        'Não Há': {
            "atico": 0,
            "laje_cob_desc": 0,
            "tipo": 0,
            "vazio_tipo": 0,
            "terreo": 0,
            "area_tipo_n_comput": 0,
            "tam_apto_terreo": 0,
            "tam_apto_tipo_1": 0,
            "tam_apto_tipo_2": 0,
            "tam_apto_tipo_3": 0,
            "tam_apto_tipo_4": 0,
            "qnt_aptos_terreo": 0,
            "qnt_aptos_tipo_1": 0,
            "qnt_aptos_tipo_2": 0,
            "qnt_aptos_tipo_3": 0,
            "qnt_aptos_tipo_4": 0
        },
    }
}
