import telnetlib
import sys
import os

os.system("color")

# telnet to a mud within your compiler!


def main():
    curr_session = telnetlib.Telnet("tiopon.mudmagic.com", 3500)
    
    with curr_session:
        curr_session.interact()
        # makes ansi work on pycharm on the run screen.
        # no fix yet for if script called via cmd
        line = (str(sys.stdin)).encode(encoding='UTF-8')
        
        sys.stdout = line
        if "quit" in str(sys.stdin):
            curr_session.close()
            exit(code=0)

 
if __name__ == '__main__':
    main()
