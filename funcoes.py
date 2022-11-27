
# CRIAÇÃO DE VARIaVEIS

# Coeficientes area equivalente:
coef_atico = 1
coef_laje_cob_desc = 0.5
coef_tipo = 1
coef_vazio_tipo = 0.5
coef_terreo = 1
coef_construções_comuns = 1.5
coef_vagas_s_terra = 0.25
coef_jardim_s_terra = 0.25
coef_melhoramento_viario = 0.25
coef_cob_mall = 0.5
coef_mall = 1
coef_reserva_de_calçada = 0.25
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
    "vaga tripla edifício garagem": 14.823,
    "vaga simples e dupla edifício garagem": 18.547,
    "vaga dupla e tripla edifício garagem": 17.168,
    "vaga simples subsolo": 29.1,
    "vaga dupla subsolo": 25.685,
    "vaga tripla subsolo": 24.823,
    "vaga simples e dupla subsolo": 26.547,
    "vaga dupla e tripla subsolo": 25.168,
    "vaga simples sobressolo": 29.1,
    "vaga dupla sobressolo": 25.685,
    "vaga tripla sobressolo": 24.823,
    "vaga simples e dupla sobressolo": 26.547,
    "vaga dupla e tripla sobressolo": 25.168,
    "não há não há": 0
}

info_plantas = {
    "ODS 2": {
        9: {
            "atico": 100,
            "laje_cob_desc": 298.87,
            "tipo": 238.38,
            "vazio_tipo": 14.74,
            "terreo": 298.87,
            "area_tipo_n_comput": 45.75,
            "tam_terreo": 4,  # Apto 1 dorm no terreo
            "tam_apto1": 26.12,  # Apto 2 dorm
            "tam_apto2": 29.42,  # Apto 2 dorm c/ suíte ponta
            "tam_apto3": 0,  # Apto 2 dorm c/ suíte meio
            "tam_apto4": 0,  # Apto 2 dorm s/ suíte meio
            "qnt_terreo": 4,
            "qnt_apto1": 8,
            "qnt_apto2": 1,
            "qnt_apto3": 0,
            "qnt_apto4": 0,
        },
        10: {
            "atico": 100,
            "laje_cob_desc": 357.1,
            "tipo": 342.36,
            "vazio_tipo": 34.7,
            "terreo": 357.1,
            "area_tipo_n_comput": 0,
            "tam_terreo": 0,  # Apto 1 dorm no terreo
            "tam_apto1": 0,  # Apto 2 dorm
            "tam_apto2": 0,  # Apto 2 dorm c/ suíte ponta
            "tam_apto3": 0,  # Apto 2 dorm c/ suíte meio
            "tam_apto4": 0,  # Apto 2 dorm s/ suíte meio
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0,
        },
        11: {  # colocar valores corretos
            "atico": 100,
            "laje_cob_desc": 357.1,
            "tipo": 342.36,
            "vazio_tipo": 34.7,
            "terreo": 357.1,
            "area_tipo_n_comput": 0,
            "tam_terreo": 4,  # Apto 1 dorm no terreo
            "tam_apto1": 26.12,  # Apto 2 dorm
            "tam_apto2": 29.42,  # Apto 2 dorm c/ suíte ponta
            "tam_apto3": 0,  # Apto 2 dorm c/ suíte meio
            "tam_apto4": 0,  # Apto 2 dorm s/ suíte meio
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0,
        },
        15: {  # colocar valores corretos
            "atico": 100,
            "laje_cob_desc": 357.1,
            "tipo": 342.36,
            "vazio_tipo": 34.7,
            "terreo": 357.1,
            "area_tipo_n_comput": 0,
            "tam_terreo": 4,  # Apto 1 dorm no terreo
            "tam_apto1": 0,  # Apto 2 dorm
            "tam_apto2": 0,  # Apto 2 dorm c/ suíte ponta
            "tam_apto3": 0,  # Apto 2 dorm c/ suíte meio
            "tam_apto4": 0,  # Apto 2 dorm s/ suíte meio
            "qnt_terreo": 3,
            "qnt_apto1": 2,
            "qnt_apto2": 2,
            "qnt_apto3": 2,
            "qnt_apto4": 4,
        },
        17: {  # colocar valores corretos
            "atico": 100,
            "laje_cob_desc": 357.1,
            "tipo": 342.36,
            "vazio_tipo": 34.7,
            "terreo": 357.1,
            "area_tipo_n_comput": 0,
            "tam_terreo": 4,  # Apto 1 dorm no terreo
            "tam_apto1": 0,  # Apto 2 dorm
            "tam_apto2": 0,  # Apto 2 dorm c/ suíte ponta
            "tam_apto3": 0,  # Apto 2 dorm c/ suíte meio
            "tam_apto4": 0,  # Apto 2 dorm s/ suíte meio
            "qnt_terreo": 3,
            "qnt_apto1": 2,
            "qnt_apto2": 2,
            "qnt_apto3": 2,
            "qnt_apto4": 4,
        },
    },
    "ODS 2 Plus": {
        8: {  # colocar valores corretos
            "atico": 100,
            "laje_cob_desc": 357.1,
            "tipo": 342.36,
            "vazio_tipo": 34.7,
            "terreo": 357.1,
            "area_tipo_n_comput": 0,
            "tam_terreo": 0,
            "tam_apto1": 0,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
        10: {  # colocar valores corretos
            "atico": 100,
            "laje_cob_desc": 357.1,
            "tipo": 342.36,
            "vazio_tipo": 34.7,
            "terreo": 357.1,
            "area_tipo_n_comput": 0,
            # Apto 1 dorm no terreo com varanda (metragem media)
            "tam_terreo": 27.158,
            # Apto 1 dorm (varanda = 2.45 m / apto seco = 24.90)
            "tam_apto1": 27.35,
            # Apto 1 dorm (varanda = 2.45 m / apto seco = 24.72)
            "tam_apto2": 26.962,
            # Apto 1 dorm (varanda = 2.45 m / apto seco = 24.51)
            "tam_apto3": 27.17,
            "qnt_terreo": 5,
            "qnt_apto1": 4,
            "qnt_apto2": 4,
            "qnt_apto3": 1
        },
        11: {
            "atico": 98.82,
            "laje_cob_desc": 381.58,
            "tipo": 271.39,
            "vazio_tipo": 22.25,
            "terreo": 381.58,
            "area_tipo_n_comput": 0,  # colocar valor correto
            "tam_terreo": 0,
            "tam_apto1": 0,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
        12: {
            "atico": 100,
            "laje_cob_desc": 357.1,
            "tipo": 342.36,
            "vazio_tipo": 34.7,
            "terreo": 357.1,
            "area_tipo_n_comput": 0,
            "tam_terreo": 0,
            "tam_apto1": 0,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
    },
    "ODS 4": {
        8: {  #REF: 11445 - Sapopemba - Rev E
            "atico": 85,
            "laje_cob_desc": 314.7,
            "tipo": 301.08,
            "vazio_tipo": 13.09,
            "terreo": 314.17,
            "area_tipo_n_comput": 42.84, #a confirmar (em ZEU não considerar esse valor)
            "tam_terreo": 32.28,
            "tam_apto1": 32.28,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 4,
            "qnt_apto1": 8,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0,
        },

        #SEGUNDO OBRAS O 9 NÃO EXISTE 

        10: { #REF: 12017 - Rua Ferreira Viana - REF C
            "atico": 120.84,
            "laje_cob_desc": 411.39,
            "tipo": 327.20,
            "vazio_tipo": 24.72,
            "terreo": 411.39,
            "area_tipo_n_comput": 59.47, # Não considerar em ZEU
            "tam_terreo": 32.72,
            "tam_apto1": 32.72,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 4,
            "qnt_apto1": 10,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0  
        },
        12: { # REF: 8091 - Edu Chaves - Rev A
            "atico": 120.84,
            "laje_cob_desc": 513.9249,
            "tipo": 392.688,
            "vazio_tipo": 43.23,
            "terreo": 513.9249,
            "area_tipo_n_comput": 78.0069,
            "tam_terreo": 32.724,  # Apto 2 dorm no terreo
            "tam_apto1": 32.724,  # Apto 2 dorm seco
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 8,
            "qnt_apto1": 12,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0,
        },
    },
    "ODS 4 Plus": {
        8: { #REF: 8602 - Rua Miragaia - Rev L
            "atico": 120.84,
            "laje_cob_desc": 346.98,
            "tipo": 304.16,
            "vazio_tipo": 21.62,
            "terreo": 346.98,
            "area_tipo_n_comput": 21.20,
            "tam_terreo": 34.87, #Sacada = 2.65
            "tam_apto1": 34.87,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 4,
            "qnt_apto1": 8,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
        10: { #REF: 8602: Rua Miragaia - Rev L
            "atico": 120.84,
            "laje_cob_desc": 437.89,
            "tipo": 386.67,
            "vazio_tipo": 24.72,
            "terreo": 437.89,
            "area_tipo_n_comput": 26.50,
            "tam_terreo": 35.37,
            "tam_apto1": 35.37,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 6,
            "qnt_apto1": 10,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
        12: { #REF: 8091 - Edu Chaves - Rev A
            "atico": 120.84,
            "laje_cob_desc": 545.7249,
            "tipo": 392.688,
            "vazio_tipo": 43.23,
            "terreo": 545.7249,
            "area_tipo_n_comput": 109.8069,
            "tam_terreo": 35.37,
            "tam_apto1": 35.37,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 8,
            "qnt_apto1": 12,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
    },
    # ! Valores possivelmente incorretos
    "Eng 1": {
        8: {  # colocar valores corretos
            "atico": 100,
            "laje_cob_desc": 357.1,
            "tipo": 342.36,
            "vazio_tipo": 34.7,
            "terreo": 357.1,
            "area_tipo_n_comput": 0,
            "tam_terreo": 0,
            "tam_apto1": 0,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
        10: {  # colocar valores corretos
            "atico": 100,
            "laje_cob_desc": 357.1,
            "tipo": 342.36,
            "vazio_tipo": 34.7,
            "terreo": 357.1,
            "area_tipo_n_comput": 0,
            "tam_terreo": 0,
            "tam_apto1": 0,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
        12: {
            "atico": 120.86,
            "laje_cob_desc": 478.53,
            "tipo": 375.27,
            "vazio_tipo": 33.79,
            "terreo": 478.53,
            "area_tipo_n_comput": 69.47,
            "tam_terreo": 31.2725,
            "tam_apto1": 31.2725,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 8,
            "qnt_apto1": 12,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
    },
    # ! Valores possivelmente incorretos
    "Eng 1 Plus": {
        8: {  # colocar valores corretos
            "atico": 100,
            "laje_cob_desc": 357.1,
            "tipo": 342.36,
            "vazio_tipo": 34.7,
            "terreo": 357.1,
            "area_tipo_n_comput": 0,
            "tam_terreo": 0,
            "tam_apto1": 0,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
        10: {  # colocar valores corretos
            "atico": 100,
            "laje_cob_desc": 357.1,
            "tipo": 342.36,
            "vazio_tipo": 34.7,
            "terreo": 357.1,
            "area_tipo_n_comput": 0,
            "tam_terreo": 0,
            "tam_apto1": 0,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
        12: {
            "atico": 120.86,
            "laje_cob_desc": 510.33,
            "tipo": 375.27,
            "vazio_tipo": 33.79,
            "terreo": 510.33,
            "area_tipo_n_comput": 101.27,
            "tam_terreo": 33.9225,
            "tam_apto1": 33.9225,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 8,
            "qnt_apto1": 12,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
    },
    "ODS 6": {
        8: {  # colocar valores corretos
            "atico": 120.84,
            "laje_cob_desc": 346.98,
            "tipo": 304.16,
            "vazio_tipo": 21.62,
            "terreo": 346.98,
            "area_tipo_n_comput": 21.20,
            "tam_terreo": 0,
            "tam_apto1": 0,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
        10: {
            "atico": 116.46,
            "laje_cob_desc": 549.44,
            "tipo": 418.72,
            "vazio_tipo": 34.934,
            "terreo": 549.44,
            "area_tipo_n_comput": 0,
            "tam_terreo": 0,
            "tam_apto1": 0,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0  # colocar valor correto
        },
        12: {  # colocar valores corretos
            "atico": 120.84,
            "laje_cob_desc": 545.7249,
            "tipo": 392.688,
            "vazio_tipo": 43.23,
            "terreo": 545.7249,
            "area_tipo_n_comput": 109.8069,
            "tam_terreo": 0,
            "tam_apto1": 0,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
    },
    "Não Há": {
        'Não Há': {
            "atico": 0,
            "laje_cob_desc": 0,
            "tipo": 0,
            "vazio_tipo": 0,
            "terreo": 0,
            "area_tipo_n_comput": 0,
            "tam_terreo": 0,
            "tam_apto1": 0,
            "tam_apto2": 0,
            "tam_apto3": 0,
            "tam_apto4": 0,
            "qnt_terreo": 0,
            "qnt_apto1": 0,
            "qnt_apto2": 0,
            "qnt_apto3": 0,
            "qnt_apto4": 0
        },
    }
}

# area comum externa 2m² por quantidade de aptos e 0,5 de area comum interna
# Taxa de Ocupação Maxima por zoneamento

# DEFINIÇÃO DE FUNÇÕES


def caracteristica_torre(categoria, quanto_por_andar, num_torres, num_andares):

    dict_tipo = info_plantas[categoria]
    info_andar = dict_tipo[quanto_por_andar]

    atico = info_andar['atico']
    laje_cob_desc = info_andar['laje_cob_desc']
    tipo = info_andar['tipo']
    vazio_tipo = info_andar['vazio_tipo']
    terreo = info_andar['terreo']
    area_tipo_n_comput = info_andar['area_tipo_n_comput']
    qnt_terreo = info_andar['qnt_terreo']

    # INCLUIR aREA NÃO COMPUTaVEL EM TIPO

    carac_torre = (atico * coef_atico * num_torres) + \
                  (laje_cob_desc * coef_laje_cob_desc * num_torres) + \
                  ((tipo * num_torres * num_andares) + area_tipo_n_comput * num_torres * num_andares) * coef_tipo + \
                  (vazio_tipo * coef_vazio_tipo * num_torres * num_andares) + \
                  (terreo * coef_terreo * num_torres)
    area_terreo = qnt_terreo * num_torres
    area_andares = num_torres * num_andares * quanto_por_andar

    return carac_torre, area_terreo, area_andares, terreo*num_torres


def area_privativa_torre(categoria, quanto_por_andar, num_torres, num_andares, area_mall):

    dict_plantas = info_plantas[categoria]
    dict_caract = dict_plantas[quanto_por_andar]
    tam_terreo = dict_caract['tam_terreo']
    tam_apto1 = dict_caract['tam_apto1']
    tam_apto2 = dict_caract['tam_apto2']
    tam_apto3 = dict_caract['tam_apto3']
    tam_apto4 = dict_caract['tam_apto4']
    fator_terreo = dict_caract['qnt_terreo']
    fator_apto1 = dict_caract['qnt_apto1']
    fator_apto2 = dict_caract['qnt_apto2']
    fator_apto3 = dict_caract['qnt_apto3']
    fator_apto4 = dict_caract['qnt_apto4']

    qnt_terreo = fator_terreo * num_torres
    qnt_apto1 = fator_apto1 * num_andares * num_torres
    qnt_apto2 = fator_apto2 * num_andares * num_torres 
    qnt_apto3 = fator_apto3 * num_andares * num_torres
    qnt_apto4 = fator_apto4 * num_andares * num_torres

    tam_total_terreo = qnt_terreo * tam_terreo
    tam_total_andares = (tam_apto1 * qnt_apto1) + (tam_apto2 * qnt_apto2) + (tam_apto3 * qnt_apto3) + (tam_apto4 * qnt_apto4)

   # Em zoneamnetos de transformação, como ZEU, a area de circulação entra como area computavel
    if area_mall > 0:
        ###########################
        # Lembrar de acertar o nr #
        ###########################

        area_privativa_total = (qnt_terreo * tam_terreo) + (tam_apto1 * qnt_apto1) + (tam_apto2 * qnt_apto2) + (tam_apto3 * qnt_apto3) + (tam_apto4 * qnt_apto4) + (56 * 26.55) + (7 * 31.66)

    else:
        area_privativa_total = tam_total_terreo + tam_total_andares

    return area_privativa_total, tam_total_andares, tam_total_terreo

# Definição da função do comendo NR (Não residencial)
# if NR == "SIM"
#  NR = 0.2 * area_privativa_total (talvez seja a area computavel)
# else
#   NR = 0

# Edifício Garagem
# Vaga simples = 17.27
# Vaga Dupla = 14.685

def funcao(categoria, quanto_por_andar, num_torres, num_andares, area_terreno, 
           area_mall, tipo_garagem, vagas_ed_garagem, disp_vagas, num_andares_garagem):

    area_terreo = 0
    a_priv_torre_total = 0
    carac_torre_total = 0
    area_andares_total = 0
    tam_total_terreo = 0
    tam_total_andares = 0
    terreo_total = 0

    for i in range(len(categoria)):
        if str.lower((categoria[i])) != "não há":
            carac_torre, area_terreo, area_andares, terreo = caracteristica_torre(
                categoria=categoria[i],
                quanto_por_andar=int(quanto_por_andar[i]),
                num_torres=int(num_torres[i]),
                num_andares=int(num_andares[i])
            )
            carac_torre_total += carac_torre
            area_andares_total += area_andares
            terreo_total += terreo
            
            a_priv_torre, tam_total_terreo_tipo , tam_total_andares_tipo = area_privativa_torre(
                categoria=categoria[i],
                quanto_por_andar=int(quanto_por_andar[i]),
                num_torres=int(num_torres[i]),
                num_andares=int(num_andares[i]),
                area_mall=area_mall
            )
            a_priv_torre_total += a_priv_torre
            tam_total_terreo += tam_total_terreo_tipo
            tam_total_andares += tam_total_andares_tipo

    implant_mall = 0
    if area_mall > 0:
        implant_mall = area_mall * coef_mall + area_mall * coef_cob_mall

    area_ed_garagem_andar = 0
    if num_andares_garagem > 0:
        area_ed_garagem_andar = vagas_ed_garagem * metragem_por_vaga[f"{str.lower(disp_vagas)} {str.lower(tipo_garagem)}"] / num_andares_garagem
    
    lazer_externo = 0.5 * (area_andares_total + area_terreo)

    area_restante = 0.25 * (area_terreno - terreo_total - lazer_externo - area_mall - area_ed_garagem_andar)

    implant = (coef_construções_comuns * lazer_externo) + ((num_andares_garagem - 1) * area_ed_garagem_andar * coef_ed_garagem + area_ed_garagem_andar * coef_cob_ed_garagem) + implant_mall + area_restante

    a_priv_tot = a_priv_torre_total + implant_mall
    a_equiv_tot = carac_torre_total + implant

    eficiencia = a_priv_tot / a_equiv_tot

    area_comput = tam_total_terreo + tam_total_andares

    coef_aprov = area_comput / area_terreno

    return eficiencia, coef_aprov

# print(funcao(['ODS 4 Plus'], [10], [2], [18], 4476, 0, 'não há', 0, 'não há', 0))

