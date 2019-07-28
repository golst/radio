import os
import struct
import fcntl
from .RF_constant import *
class RFKILL(): 
    def rfkill_operate(self,index:"the device index",block:"the soft block operation"):
        op=struct.pack(RF_Event,int(index),RF_Type['all'],RF_Opera['Op_Change'],RF_State[block],0).decode()
        with open(RF_Dev,'w') as f:
            f.write(op)
    def rfkill_show(self):
        formart_str="index {:2} name {:25} type {:10} state {:10}"
        length=struct.calcsize(RF_Event)
        with open(RF_Dev,"r") as rfdev:
            flags=fcntl.fcntl(rfdev.fileno(),fcntl.F_GETFL)
            fcntl.fcntl(rfdev.fileno(),fcntl.F_SETFL,flags|os.O_NONBLOCK)
            while True:
                try:
                    res=rfdev.read(length)
                    res=bytes(res,'ascii')
                    if len(res) < length:
                        raise IOError()
                    index=struct.unpack(RF_Event,res)[0]
                    print(formart_str.format(index,*self.rfkill_sys_attr(index)))
                except IOError:
                    break
    def rfkill_sys_attr(self,index:"for /sys/class/rfkill")->"return a list to format show":
        res=[]
        for one in RF_Attr:
            with open(RF_Sys.format(index,one),"r") as f:
                try:
                    res.append(f.read().strip())
                except IOError:
                    print(f"open /sys/ {one} error")
                    res.append('')
        res.append(RF_Sys_State[int(res.pop())])
        return res