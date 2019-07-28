"""
this module just redefines some c structs of rfkill in the header file /usr/include/linux/rfkill.h
"""
RF_Event="IBBBB"
RF_Type={'all':0,"wlan":1,"bluetooth":2,"uwb":3,"wimax":4,"wwan":5,"gps":6,"fm":7,"nfc":8}
RF_Opera={'Op_Add':0,'Op_Del':1,'Op_Change':2,'Op_ChangeAll':3}
RF_State={"unblock":0,"block":1}
RF_Dev="/dev/rfkill"
RF_Sys="/sys/class/rfkill/rfkill{}/{}"
RF_Attr=['name',"type","state"]
RF_Sys_State=['Soft_blocked','Unblocked','Hard_blocked']