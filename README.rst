# Welcome to TradeFramework

Everything you need to trade Binance Futures from the console


This is Python TradeFramework for the Binance Futures. Use at your own RISK!

For use this you need:
  - Python 3.9.7
  - Ubuntu 20.04 
  - pip 21.2.4
  - or other specifications
  - Recommended: Stable VPS 5$/month `Inferno Solutions <https://cp.inferno.name/aff.php?aff=3406>`_ 
  
 Start step by step:
   - `Login Binance account <https://www.binance.com/?ref=MNJSQTZI>`_ 
   - Generate API for Futures
   - Recommended: For easy trading analysis `Trading journal - Trader Make Money <https://tradermake.money/?ref=KGMY8G>`_
   

.. code:: bash

    :~$ sudo apt-get update
    :~$ sudo apt-get upgrade
    :~$ sudo dpkg-reconfigure tzdata
    
    :~$ lsb_release -a
    Description:  Ubuntu 20.04.3 LTS
    Release:  20.04
        
    :~$ python3 -V
    Python 3.9.7
    
    :~$ sudo apt install python3-pip
    :~$ pip3 -V
    pip 21.2.4 from /usr/lib/python3.9/dist-packages/pip (python 3.9)
    
    :~$ pip3 install python-binance
    :~$ pip3 install datetime
    
    :~$ apt install git
    :~$ git clone https://github.com/it-viktor/TradeFramework.git
    :~$ cd TradeFramework
    :~$ python3
    Python 3.9.7 (default, Sep 16 2021, 08:50:36)
    [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from trades import *                                                                                                                                                                                    
    Enter Binance Futures api key:                                                                                                                                                                              
    ****************************************************************                                                                                                                                            
                                                                                                                                                                                                            
    Enter Binance Futures api secret key:                                                                                                                                                                       
    ****************************************************************                                                                                                                                            
                                                                                                                                                                                                            
    The config.cfg file will be saved to /opt/TradeFramework/TradeFramework                                                                                                                                     
    Save keys?  YES/NO:                                                                                                                                                                                         
    yes                                                                                                                                                                                                         
                                                                                                                                                                                                            
    The config.cfg file is saved in /opt/TradeFramework/TradeFramework directory.                                                                                                                               
    >>> chz = newTrade('chz', 20)                                                                                                                                                                               
    ----01.11.2022 17:25                                                                                                                                                                                        
            Symbol   : CHZUSDT                                                                                                                                                                                  
            Leverage : 20                                                                                                                                                                                                                    
    >>> chz.checkBalnc()                                                                                                                                                                                        
    ----01.11.2022 17:25                               
    Balance: 49.09818806 USDT                          
    >>> chz.buy_market(50)                             
    ----01.11.2022 17:26                               
            Symbol :   CHZUSDT                         
            OrderId:   7670616091                      
            origQty:   50                              
            Side   :   BUY                             
            Status :   NEW                             
    >>> chz.sl(0.22288)                                
    ----01.11.2022 17:26                               
            Symbol    : CHZUSDT                        
            OrderId   : 7670618519                     
            Side      : SELL                           
            Status    : NEW                            
            stopPrice : 0.22288                        
    >>> chz.checkPos()                                 
    ----01.11.2022 17:26                               
            Symb: CHZUSDT                              

            entryPrice:  0.22413                       
            Liquidation: 0                             
            Amt:  50 Coins                             
            Amt:  11 Dollars                           

            PNL:  0.01450000                           
    >>> chz.sell_market(50)
    ----01.11.2022 17:27
            Symbol :   CHZUSDT
            OrderId:   7670627234
            origQty:   50
            Side   :   SELL
            Status :   NEW
    >>> chz.checkPos()
    ----01.11.2022 17:27
            Symb: CHZUSDT

            entryPrice:  0.0
            Liquidation: 0
            Amt:  0 Coins
            Amt:  0 Dollars

            PNL:  0.00000000
    >>> chz.checkOpenOrders()
    ----01.11.2022 17:27
            Symbol :   CHZUSDT
            OrderId:   7670618519
            origQty:   0
            Side   :   SELL
            Price  :   0
            slPrice:   0.22288
            Status :   NEW
            Type   :   STOP_MARKET
    All 1 open orders
    >>> chz.cancelOrders()
    ----01.11.2022 17:27
    code:200 The operation of cancel all open order is done.
    All 0 open orders
    >>> chz.checkOpenOrders()
    All 0 open orders
    >>> quit()
    :~$ 

 
 Works! GOOD LUCK!!


