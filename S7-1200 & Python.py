# Snap7
# Description: Projeto que lê o pulso da primeira entrada digital e faz um log do tamanho(tempo) de pulso.
# Author: Rafael Kruger Schwertz
# Creation date: 2023-03-31
# Last update: 2023-03-31
# Version: 1.0
# Platform: Windows 10
# Programming language: Python
# Libraries used: snap7
# Additional Notes: N/A

import snap7
from snap7.util import *
from snap7.types import *
from snap7.exceptions import *

plc = snap7.client.Client()
plc.connect('192.168.0.1', 0, 1)

pe_area = S7AreaPE
buffer = plc.read_area(pe_area.value, 0, 0, 1)
bit_value = get_bool(buffer, 0, 0)

#A função read_area lê uma área de memória do PLC. O primeiro parâmetro (PE) especifica a área de memória, 
# o segundo parâmetro (0) especifica o endereço do primeiro byte na área de memória, 
# o terceiro parâmetro (0) especifica o deslocamento em bits no byte e o quarto parâmetro (1) especifica o número de bytes a serem lidos. 
# A função get_bool é usada para obter o valor do primeiro bit do buffer lido.

import time

start_time = None
while True:
    buffer = plc.read_area(S7AreaPE, 0, 0, 1)
    bit_value = get_bool(buffer, 0, 0)
    
    if bit_value:
        if start_time is None:
            start_time = time.monotonic()
    else:
        if start_time is not None:
            pulse_duration = time.monotonic() - start_time
            print(f"Pulse duration: {pulse_duration:.2f} seconds")
            start_time = None
            
    time.sleep(0.01)

#O loop verifica se o valor do bit é 1 ou 0. Se o valor do bit for 1 e o tempo de início do pulso ainda não tiver sido registrado, 
# o tempo de início do pulso é registrado usando a função time.monotonic(). 
# Se o valor do bit for 0 e o tempo de início do pulso tiver sido registrado, 
# o tempo de duração do pulso é calculado subtraindo o tempo de início do pulso do tempo atual usando a função time.monotonic(). 
# O tempo de duração do pulso é então registrado no log. 
# O loop espera 10 milissegundos a cada iteração para evitar que o loop execute muito rapidamente.