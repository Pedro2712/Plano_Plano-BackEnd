# CRIAÇÃO DE VARIÁVEIS

#Coeficientes área equivalente:
coef_ático = 1
coef_laje_cob_desc = 0.5
coef_tipo = 1
coef_vazio_tipo = 0.5
coef_térreo = 1
coef_construções_comuns = 1.5
coef_vagas_s_terra = 0.25
coef_jardim_s_terra = 0.25
coef_melhoramento_viário = 0.25
coef_cob_mall = 0.5
coef_mall = 1
coef_reserva_de_calçada = 0.25
coef_ed_garagem = 1
coef_cob_ed_garagem = 0.5

#CA = área computável/área do terreno
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

#Área comum externa 2m² por quantidade de aptos e 0,5 de área comum interna
#Taxa de Ocupação Máxima por zoneamento

# DEFINIÇÃO DE FUNÇÕES

def area_equivalente(categoria, quanto_por_andar, num_torres, num_andares, lazer_externo, área_terreno, área_mall, vagas_ed_garagem):
    if categoria == "ODS 2":
        if quanto_por_andar == 8:
            ático = 0
            laje_cob_desc = 0
            tipo = 0
            vazio_tipo = 0
            térreo = 0
            area_tipo_n_comput = 0
            
        elif quanto_por_andar == 10:
            ático = 100
            laje_cob_desc = 357.1
            tipo = 342.36
            vazio_tipo = 34.7
            térreo = 357.1
            area_tipo_n_comput= 0
            
        else: # elif quanto_por_andar == 12:
            ático = 0
            laje_cob_desc = 0
            tipo = 0
            vazio_tipo = 0
            térreo = 0
            area_tipo_n_comput= 0
    
    elif categoria == "ODS 2 Plus":
        if quanto_por_andar == 8:
            ático = 0
            laje_cob_desc = 0
            tipo = 0
            vazio_tipo = 0
            térreo = 0
            area_tipo_n_comput= 0
            
        elif quanto_por_andar == 10:
            ático = 0
            laje_cob_desc = 0
            tipo = 0
            vazio_tipo = 0
            térreo = 0
            area_tipo_n_comput= 0
            
        else: # elif quanto_por_andar == 12:
            ático = 0
            laje_cob_desc = 0
            tipo = 0
            vazio_tipo = 0
            térreo = 0
            area_tipo_n_comput= 0
    
    elif categoria == "ODS 4":
        if quanto_por_andar == 8:
            ático = 0
            laje_cob_desc = 0
            tipo = 0
            vazio_tipo = 0
            térreo = 0
            area_tipo_n_comput= 0
            
        elif quanto_por_andar == 10:
            ático = 100
            laje_cob_desc = 357.1
            tipo = 342.36
            vazio_tipo = 14.74
            térreo = 357.10
            area_tipo_n_comput= 0
            
        else: # elif quanto_por_andar == 12:
            ático = 114.89
            laje_cob_desc = 482.35
            tipo = 375.36
            vazio_tipo = 34.7
            térreo = 482.35
            area_tipo_n_comput= 0
    
    elif categoria == "ODS 4 Plus":
        if quanto_por_andar == 8:
            ático = 0
            laje_cob_desc = 0
            tipo = 0
            vazio_tipo = 0
            térreo = 0
            area_tipo_n_comput= 0

        elif quanto_por_andar == 10:
            ático = 0
            laje_cob_desc = 0
            tipo = 0
            vazio_tipo = 0
            térreo = 0
            area_tipo_n_comput= 0

        else: # elif quanto_por_andar == 12:
            ático = 0
            laje_cob_desc = 0
            tipo = 0
            vazio_tipo = 0
            térreo = 0
            area_tipo_n_comput= 0
            
    elif categoria == "ODS 6":
        if quanto_por_andar == 8:
            ático = 0
            laje_cob_desc = 0
            tipo = 0
            vazio_tipo = 0
            térreo = 0
            area_tipo_n_comput= 0
            
        elif quanto_por_andar == 10:
            ático = 116.46
            laje_cob_desc = 549.44
            tipo = 418.72
            vazio_tipo = 34.934
            térreo = 549.44
            area_tipo_n_comput= 2681.952
        
        else: # elif quanto_por_andar == 12:
            ático = 0
            laje_cob_desc = 0
            tipo = 0
            vazio_tipo = 0
            térreo = 0
            area_tipo_n_comput= 0
    
    else: # Não Há
        ático = 0
        laje_cob_desc = 0
        tipo = 0
        vazio_tipo = 0
        térreo = 0
        area_tipo_n_comput= 0
    
    implant_mall = 0
    if área_mall> 0:
        implant_mall = (área_mall * coef_mall) + ((área_mall/2) *coef_cob_mall)
    
    # else:
    #     implant_mall = 0
        
    # área_ed_garagem = (num_vagas/qnt)
    
    # INCLUIR ÁREA NÃO COMPUTÁVEL EM TIPO
    
    carac_torre = (ático * coef_ático * num_torres) + (laje_cob_desc * coef_laje_cob_desc *num_torres) + \
                  ((tipo * num_torres * num_andares) + area_tipo_n_comput) * coef_tipo + \
                  (vazio_tipo * coef_vazio_tipo * num_torres * num_andares) + (térreo * coef_térreo * num_torres)
                  
    área_restante = 0.25 *(área_terreno - ((térreo * num_torres) - lazer_externo - área_mall)) # - 1 pavmento do ed garagem
    
    implant = (coef_construções_comuns * lazer_externo) + implant_mall + área_restante # + (área_ed_garagem * coef_ed_garagem + cob_ed_garagem *coef_cob_ed_garagem)

    área_equivalente = carac_torre + implant

    return área_equivalente

#área_equiv = área_equivalente1 + área_equivalente2
    
def área_privativa_total(categoria, quanto_por_andar, num_torres,num_andares, lazer_externo, área_terreno, área_mall):

    qnt_apto2 = (num_andares - 1) * num_torres
    qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
    if categoria == "ODS 2":
        if quanto_por_andar == 8:
            qnt_térreo = 0 
            tam_apto1 = 0
            tam_apto2 = 0
        
        elif quanto_por_andar == 10:
            qnt_térreo = 5
            tam_apto1 = 26.12
            tam_apto2 = 29.42
            # qnt_apto2 = (num_andares - 1) * num_torres
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
        
        else: # elif quanto_por_andar == 12:
            qnt_térreo = 0 
            tam_apto1 = 0
            tam_apto2 = 0
            # qnt_apto2 = (num_andares - 1) * num_torres
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
    
    elif categoria == "ODS 2 Plus":
        if quanto_por_andar == 8:
            qnt_térreo = 0 
            tam_apto1 = 0
            tam_apto2 = 0
            # qnt_apto2 = (num_andares - 1) * num_torres
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
        
        elif quanto_por_andar == 10:
            qnt_térreo = 0 
            tam_apto1 = 0
            tam_apto2 = 0
            # qnt_apto2 = (num_andares - 1) * num_torres
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
        
        else: # elif quanto_por_andar == 12:
            qnt_térreo = 0 
            tam_apto1 = 0
            tam_apto2 = 0
            # qnt_apto2 = (num_andares - 1) * num_torres
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
    
    elif categoria == "ODS 4":
        if quanto_por_andar == 8:
            qnt_térreo = 0
            tam_apto1 = 0
            tam_apto2 = 0
            qnt_apto2 = 0
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
        
        elif quanto_por_andar == 10:
            qnt_térreo = 0
            tam_apto1 = 0
            tam_apto2 = 0
            qnt_apto2 = 0
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
        
        else: # elif quanto_por_andar == 12:
            qnt_térreo = 5
            tam_apto1 = 35.37
            tam_apto2 = 0
            qnt_apto2 = 0
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
    
    elif categoria == "ODS 4 Plus":
        if quanto_por_andar == 8:
            qnt_térreo = 0
            tam_apto1 = 0
            tam_apto2 = 0
            qnt_apto2 = 0
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
        
        elif quanto_por_andar == 10:
            qnt_térreo = 0
            tam_apto1 = 0
            tam_apto2 = 0
            qnt_apto2 = 0
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
        
        else: # elif quanto_por_andar == 12:
            qnt_térro = 0
            tam_apto1 = 0
            tam_apto2 = 0
            qnt_apto2 = 0
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
    
    else: # Ods 6
        if quanto_por_andar == 8:
            qnt_térreo = 0 
            tam_apto1 = 0
            tam_apto2 = 0
            # qnt_apto2 = (num_andares - 1) * num_torres
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
        
        elif quanto_por_andar == 10:
            tam_térreo = 40.357
            #Apto 3 dorm c/ suíte ponta
            tam_apto1 = 52.84
            #Apto 2 dorm c/ suíte ponta
            tam_apto2 = 45.31
            #Apto 2 dorm c/ suíte meio
            tam_apto3 = 43.913
            #Apto 2 dorm s/ suíte meio
            tam_apto4 = 40.357
            
            qnt_térreo = 3 * num_torres
            qnt_apto1  = 2 * num_andares * num_torres 
            qnt_apto2  = 2 * num_andares * num_torres
            qnt_apto3  = 2 * num_andares * num_torres
            qnt_apto4  = 4 * num_andares * num_torres
            
        else: # elif quanto_por_andar == 12:
            qnt_térreo = 0 
            tam_apto1 = 0
            tam_apto2 = 0
            # qnt_apto2 = (num_andares - 1) * num_torres
            # qnt_apto1 = (num_andares - 1) * num_torres * quanto_por_andar
    
    área_privativa_total = (qnt_térreo * tam_térreo) + (tam_apto1 * qnt_apto1) + (tam_apto2 * qnt_apto2) + (tam_apto3 * qnt_apto3) + (tam_apto4 * qnt_apto4)
    if área_mall > 0:
        ###########################
        # Lembrar de acertar o nr #
        ###########################

        # área_privativa_total = (qnt_térreo * tam_térreo) + (tam_apto1 * qnt_apto1) + (tam_apto2 * qnt_apto2) + (tam_apto3 * qnt_apto3) + (tam_apto4 * qnt_apto4) + (56 * 26.55) + (7 * 31.66) + área_mall

        área_privativa_total += (56 * 26.55) + (7 * 31.66) + área_mall
        
    # else:
    #     área_privativa_total = (qnt_térreo * tam_térreo) + (tam_apto1 * qnt_apto1) + (tam_apto2 * qnt_apto2) + (tam_apto3 * qnt_apto3) + (tam_apto4 * qnt_apto4)
    
    return área_privativa_total

# def funcao(categoria, quanto_por_andar, num_torres, num_andares, lazer_externo, área_terreno, área_mall, vagas_ed_garagem):
#     a_equiv_tipo1 = área_equivalente(categoria, quanto_por_andar, num_torres, num_andares, lazer_externo,
#                                      área_terreno, área_mall, vagas_ed_garagem)
#     a_equiv_tipo2 = área_equivalente(categoria, quanto_por_andar, num_torres, num_andares, lazer_externo,
#                                      área_terreno, área_mall, vagas_ed_garagem)
#     a_priv_tot    = área_privativa_total(categoria, quanto_por_andar, num_torres,num_andares, lazer_externo,
#                                       área_terreno, área_mall)
    
#     eficiencia = a_priv_tot/a_equiv_tipo1
#     label_efi = tk.Label(ig.root, text = f'A eficiência desse projeto é {eficiencia:.2}')
#     label_efi.config(font=('Arial', 15))
#     ig.canvas1.create_window(500, 550, window=label_efi)