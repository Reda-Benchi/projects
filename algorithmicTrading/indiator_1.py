# @author: Reda Benhci (https://github.com/Reda-Benchi/projects/tree/main/algorithmicTrading)

from ibapi.client import EClient 
# establish connection to IBKR through your python script

from ibapi.wrapper import EWrapper
# EWrapper is an interface that contains methods to handle events from IBKR

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson=""):
        print("Error. Id: {}\nCode: {}\nMsg: {}\n".format(reqId, errorCode, errorString))
    # This method is called when an error occurs. It prints the error message.

app = TradingApp()
app.connect("127.0.0.1", 7497, 1)
# Connect to the IBKR TWS or Gateway. The parameters are host, port, and

app.run()
