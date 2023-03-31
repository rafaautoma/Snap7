# Snap7
# Description: Project to Snap7 Librarie
# Author: Rafael Kruger Schwertz
# Creation date: 2023-03-29
# Last update: 2023-03-29
# Version: 1.0
# Platform: Windows 10
# Programming language: Python
# Libraries used: N/A
# Additional Notes: N/A

import snap7.client as c
from snap7.util import *
from snap7.types import *
import time
from datetime import datetime
import os

def ReadMemory(plc,byte,bit,datatype,area1,comeco):
    result = plc.read_area(area1,comeco,byte,datatype)
    if datatype==S7WLBit:
        return get_bool(result,0,bit)
    elif datatype==S7WLByte:
        return get_sint(result,0)
    elif datatype==S7WLWord:
        return get_int(result,0)
    elif datatype==S7WLReal:
        return get_real(result,0)
    elif datatype==S7WLDWord:
        return get_dint(result,0)
    else:
        return None

# def ReadMemory2(plc,byte,bit,datatype,area1,comeco):
#     result = plc.read_area(area1,comeco,byte,datatype)
#     if datatype==S7WLBit:
#         return get_bool(result,0,bit)
#     elif datatype==S7WLByte:
#         return get_sint(result,0)
#     elif datatype==S7WLWord:
#         return get_uint(result,0)
#     elif datatype==S7WLReal:
#         return get_real(result,0)
#     elif datatype==S7WLDWord:
#         return get_dword(result,0)
#     else:
#         return None

if __name__=="__main__":
    plc = c.Client()
    plc.connect('192.168.0.1',0,1,102)
    while(True):
        os.system('cls')
        # Ler Memorias (MK)
        # var = ReadMemory(plc,byte,bit,datatype,Areas.MK,0)
        a = ReadMemory(plc,0,0,S7WLBit,Areas.MK,0) # M0.0
        b = ReadMemory(plc,0,1,S7WLBit,Areas.MK,0) #M0.1
        c = ReadMemory(plc,0,2,S7WLBit,Areas.MK,0) #M0.2
        d = ReadMemory(plc,10,0,S7WLByte,Areas.MK,0) #MB10
        e = ReadMemory(plc,14,0,S7WLWord,Areas.MK,0) #MW14
        f = ReadMemory(plc,16,0,S7WLDWord,Areas.MK,0) #MD16
        g = ReadMemory(plc,20,0,S7WLReal,Areas.MK,0) #MD20
        # Ler Inputs (PE)
        # var = ReadMemory(plc,byte,bit,datatype,Areas.PE,0)
        h = ReadMemory(plc,0,0,S7WLBit,Areas.PE,0) #I0.0
        i = ReadMemory(plc,0,1,S7WLBit,Areas.PE,0) #I0.1
        # Ler Outputs (PA)
        # var = ReadMemory(plc,byte,bit,datatype,Areas.PA,0) #Q0.0
        j = ReadMemory(plc,0,0,S7WLBit,Areas.PA,0)
        # Ler DB (DB)
        # var = ReadMemory(plc,byte,bit,datatype,Areas.MK,numero da db que quero ler)
        k = ReadMemory(plc,0,0,S7WLBit,Areas.DB,120) #DB120.DBX0.0
        l = ReadMemory(plc,0,1,S7WLBit,Areas.DB,120) #DB120.DBX0.1
        m = ReadMemory(plc,0,2,S7WLBit,Areas.DB,120) #DB120.DBX0.2
        n = ReadMemory(plc,8,0,S7WLWord,Areas.DB,120) #DB120.DBW8
        o = ReadMemory(plc,10,0,S7WLWord,Areas.DB,120) #DB120.DBW10
        

        #Mostra a data e a hora
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Imprime o valor das variáveis sempre quebrando uma linha
        print(date_time,
               "\nLiga(M0.0):", a,
               "\nDesliga(M0.1): ", b, 
               "\nMotor(M0.2): ", c, 
               "\nShort Int(MB10): ", d, 
               "\nInt(MW14): ", e, 
               "\nDouble Int(MD16): ", f, 
               "\nReal(MD20): ", g)
        print("-----------")
        print("Liga(I0.0):", h, 
              "\nDesliga(I0.1):", i, 
              "\nMotor(Q0.0):", j)
        print("-----------")
        print("Liga(DB120.DBX0.0):", k, 
              "\nDesliga(DB120.DBX0.1):", l, 
              "\nMotor(DB120.DBX0.2):", m, 
              "\nContador Ligado(DB120.DBW8):", n, 
              "\nContador Desligado(DB120.DBW10):", o)
        time.sleep(1)