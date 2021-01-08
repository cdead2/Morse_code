from colorama import Fore, Back, Style
class Banner:
    RED=Fore.RED
    YELLOW=Fore.YELLOW
    White=Fore.WHITE
    GREEN=Fore.GREEN
    Back=Back.GREEN
#    def __init__(self):
  #      self._help()
      #  self.banner()
       # self.Traingle()
        #self._help()
    def _help(self):
        print (self.GREEN + "en >to encrypt a text")
        print (self.RED + "de >to decrypt a text")
        print (self.GREEN + "To encode_text:")
        print (self.RED + "Example : python3 morse_decoder en hello world")
        print (self.GREEN + "Output :  .... . .-.. .-..   .--   .-. .-.. -..")
        print (self.RED + " To decode_morse:")
        print (self.GREEN + "Example : python3 morse_decoder de .... . .-.. .-..   .--   .-. .-.. -..")
        print (self.RED + "Output : hello world")

    def banner(self):
        print ( f"""
{self.YELLOW}                           #     #                                 #####                       
{self.GREEN} ##   ##  ####  #####   ####  ######    #     #  ####  #####  ###### 
{self.RED} # # # # #    # #    # #      #         #       #    # #    # #      
{self.YELLOW} #  #  # #    # #    #  ####  #####     #       #    # #    # #####  
 #     # #    # #####       # #         #       #    # #    # #      
 #     # #    # #   #  #    # #         #     # #    # #    # #      
 #     #  ####  #    #  ####  ######     #####   ####  #####  ###### 
                                                                    

    """
)
    def Triangle(self):
        n,m,b,v=6,0,6,7
        for _ in range(1):
            for i in range(1,n):
                if i==1:
                    print(' '*6+'*')
            
                print(' '*(n-i),end='')
                print('*',' '*(i+m),end='')
                print('*')
        
                m+=1
            for h in range(n,0,-1):
                print(' '*(n-h),end='')
                print('*',' '*(h+b-2),end='')
                print('*')
                if h==1:
                    print(' '*n+'*')
                b-=1


