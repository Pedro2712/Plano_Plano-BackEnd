"""

TO DO:

1. Testar ed. garagem, se está calculando corretamente, com o exemplo do São Mateus ZPI
2. Incluir lógica da vaga de garagem em baixo da torre
3. Testar lógica da vaga em baixo da torre
4. Incluir mall embaixo da torre
5. Incluir mall separado da torre
6. Testar lógicas dos diferentes tipos de mall.
"""

# import tkinter as tk
from variables import *


def caracteristica_torre(categoria: list, quanto_por_andar: list, num_torres: list, num_andares: list, zoneamento: str):
    a_equiv_total_torre = 0
    area_comp_total_terreo = 0
    area_total_comput_andares = 0
    area_total_comput = 0
    area_total_terreo = 0
    a_priv_total_andares = 0
    a_priv_total_terreo = 0
    unids_tot = 0

    for i in range(len(categoria)):
        if str.lower((categoria[i])) != "não há":
            num_aptos_andar = int(quanto_por_andar[i])
            dict_tipo: dict = info_plantas[categoria[i]]
            carac_torre: dict = dict_tipo[num_aptos_andar]
            num_torres_tipo: int = int(num_torres[i])
            num_andares_torre: int = int(num_andares[i])

            if zoneamento == "ZEU":
                area_comput = carac_torre['area_priv_comput'] + carac_torre['area_circ']
            else:
                area_comput = carac_torre['area_priv_comput']

            area_tipo = carac_torre['laje_cob_desc'] - carac_torre['vazio_tipo']

            a_equiv_torre = num_torres_tipo * ((carac_torre['atico'] * coef_atico) +
                                               (carac_torre['laje_cob_desc'] * (coef_terreo + coef_laje_cob_desc)) +
                                               ((area_tipo * coef_tipo +
                                                 carac_torre['vazio_tipo'] * coef_vazio_tipo) * num_andares_torre))

            a_equiv_total_torre += a_equiv_torre
            area_total_terreo += carac_torre['laje_cob_desc'] * num_torres_tipo
            area_comp_total_terreo = carac_torre['area_comput_terreo'] * num_torres_tipo
            area_total_comput_andares = area_comput * num_torres_tipo * num_andares_torre
            print(area_comp_total_terreo)
            print(area_total_comput_andares)            
            a_priv_total_terreo += (carac_torre['area_comput_terreo'] + carac_torre[
                'area_priv_n_comput_terreo']) * num_torres_tipo
            a_priv_total_andares += (carac_torre['area_priv_comput'] + carac_torre['area_priv_n_comput']) * \
                                    num_torres_tipo * num_andares_torre

            area_total_comput_torre = area_comp_total_terreo + area_total_comput_andares
            area_total_comput += area_total_comput_torre
            unids_tot_tipo = (carac_torre['num_aptos_terreo'] + (num_aptos_andar * num_andares_torre)) * num_torres_tipo
            unids_tot += unids_tot_tipo

    a_priv_total_torres = a_priv_total_terreo + a_priv_total_andares

    return a_equiv_total_torre, area_total_comput, area_total_terreo, a_priv_total_torres, unids_tot


def funcao(categoria, quanto_por_andar, num_torres, num_andares, area_terreno, zoneamento, tipo_garagem, disp_vagas,
           loc_mall
           # root, canvas1,
           , vagas_garagem: int = 0, num_andares_garagem: int = 0, area_mall: int = 0):
    # Características da torre
    a_equiv_total_torre, area_comput_total, area_total_terreo, a_priv_total_torres, total_unidades = \
        caracteristica_torre(categoria=categoria, quanto_por_andar=quanto_por_andar, num_torres=num_torres,
                             num_andares=num_andares, zoneamento=zoneamento)

    print(area_comput_total)
    a_equiv_garagem = 0
    if tipo_garagem == 'Edifício Garagem':
        projecao_garagem = (vagas_garagem * metragem_por_vaga[f"{str.lower(disp_vagas)} {str.lower(tipo_garagem)}"]) / num_andares_garagem
        a_equiv_garagem = (projecao_garagem * num_andares_garagem * coef_ed_garagem) + (projecao_garagem * coef_cob_ed_garagem)

    implant_mall = 0
    jard_sobr_laje = 0
    if loc_mall == 'Sob a torre':
        implant_mall = area_mall * (coef_mall + coef_cob_mall)
        jard_sobr_laje = area_mall - area_total_terreo

    lazer_externo = 0.5 * total_unidades

    area_restante = 0.25 * (area_terreno - (area_total_terreo + lazer_externo + a_equiv_garagem + jard_sobr_laje))

    implant = (coef_construcoes_comuns * lazer_externo) + a_equiv_garagem + implant_mall + jard_sobr_laje * 0.5 \
        + area_restante

    a_priv_tot = a_priv_total_torres + area_mall
    a_equiv_tot = a_equiv_total_torre + implant

    eficiencia = a_priv_tot / a_equiv_tot

    coef_aprov = area_comput_total / area_terreno

    # canvas1.delete('temp')
    # label_efi = tk.Label(root, text=f'A eficiência desse projeto é {eficiencia:.2}')
    # label_efi.config(font=('Arial', 15))
    # canvas1.create_window(800, 600, window=label_efi, tags='temp')
    #
    # label_ca = tk.Label(root, text=f'O C.A. desse projeto é {coef_aprov:.2}')
    # label_ca.config(font=('Arial', 15))
    # canvas1.create_window(200, 600, window=label_ca, tags='temp')

    return eficiencia, coef_aprov


if __name__ == '__main__':
    efic, coef = funcao(categoria=['Eng 3 Plus'],
                        quanto_por_andar=['12'],
                        num_torres=['9'],
                        num_andares=['9'],
                        area_terreno=17973.93,
                        tipo_garagem='Não há',
                        disp_vagas='Não Há',
                        vagas_garagem=0,
                        num_andares_garagem=0,
                        area_mall=0,
                        zoneamento='ZPI'
                        )

    print(f'eficiência: {efic:.3}, \n coeficiente: {coef:.3}')
