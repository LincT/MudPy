# TODO: move telnet logic here and out of main.
import telnetlib


# import msvcrt
# import select


class TelnetHandler:
    host_name: str = None
    port_number: int = None
    
    def __init__(self,host_name,port_number):
        pass

    def open(self):
        pass
    
    def close_session(self):
        pass
