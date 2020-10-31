#!/usr/bin/env python3
# shebang!
import telnetlib
import sys
import os

# makes color work in most systems running this script
os.system("color")

# telnet to a mud within python!


def main(arg_list: list):
    
    if len(arg_list) > 1:
        host_name = arg_list[1]
        if str(arg_list[2]).isdigit():
            port_num = int(arg_list[2])
    curr_session = telnetlib.Telnet(host=host_name, port=port_num)
    
    with curr_session:
        # curr_session.open(host_name, port_num)
        curr_session.interact()
        # makes ansi work on the run screen.
        line = (str(sys.stdin)).encode(encoding='UTF-8')
        
        sys.stdout = line
        if "quit" in str(line):
            # curr_session.get_socket().close()
            # exit(code=0)
            curr_session.get_socket().shutdown()
            data = curr_session.read_all()
            curr_session.close()
            print(data)

 
if __name__ == '__main__':
    
    main(sys.argv)
