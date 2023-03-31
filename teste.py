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
import array
import struct

def WriteMemory(plc, byte, bit, datatype, area1, start, value):
    if datatype == S7WLBit:
        current_value = plc.read_area(area1, start, byte, datatype)
        set_bool(current_value, 0, bit, value)
        plc.write_area(area1, start, byte, current_value, datatype)
    elif datatype == S7WLByte:
        plc.write_area(area1, start, bytearray(struct.pack('>b', value)), datatype)
    elif datatype == S7WLWord:
        plc.write_area(area1, start, bytearray(struct.pack('>h', value)), datatype)
    elif datatype == S7WLReal:
        plc.write_area(area1, start, bytearray(struct.pack('>f', value)), datatype)
    elif datatype == S7WLDWord:
        plc.write_area(area1, start, bytearray(struct.pack('>i', value)), datatype)
    else:
        raise ValueError('Datatype not supported')

if __name__=="__main__":
    plc = c.Client()
    plc.connect('192.168.0.1',0,1,102)
    while(True):
        os.system('cls')

        # Write value 1234 to address 100 in the DB1 area
        WriteMemory(plc, 14, 0, S7WLWord, Areas.DB, 120, 1234)

        time.sleep(1)
