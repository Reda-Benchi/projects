1. Setup: TWS & IBKR API
1.1. Visit the U.S. IBKR site
Always select the stable version when downloading.

1.2. Download TWS (Trader Workstation)
TWS Download: https://www.interactivebrokers.com/en/index.php?f=14099#tws-software
TWS is only used to visualize trades made through the API.

1.3. Download the IBKR API
IBKR API Download: https://interactivebrokers.github.io/#
Our code connects to this API to place trades.

Use Paper Trading for demo money or Live Trading for real money.

----------------------------------------------------------------------------------

2. API Architecture (nice to know)
Typical setup: Server → Your Trading App
IBKR setup: Server → TWS → Your Trading App

Note: TWS must be running for your code to place trades via the API.

----------------------------------------------------------------------------------

3. Setup enviroment 
Create and activate a virtual environment inside your project directory:

# Create the virtual environment
python3 -m venv IBKRvenv

# Activate the virtual environment
source IBKRvenv/bin/activate

# (To deactivate the environment when finished)
deactivate

# Install specific Python version (if needed, otherwise skip if already using 3.12.5)
pip install python==3.12.5

# Install required libraries
pip install pandas==2.3.0
pip install matplotlib==3.10.3
pip install setuptools==80.9.0

----------------------------------------------------------------------------------

4. Install API Setup Script 
Navigate to the setup script directory
cd /twsapi_macunix/IBJts/source/pythonclient

# Verify that setup.py exists
ls setup.py

# Install the package
python3 setup.py install

If ibapi was not successfully installed, run the following commend. 
Code: pip install ibapi

----------------------------------------------------------------------------------

5. Gateway API Configuration Settings
# Only the following ports are enabled to listen for API calls. These ports must be enabled and locked down to ensure secure access:

TWS live trading: 7496
TWS paper trading: 7497

How to configure:
5.1 Open the TWS platform.
5.2 When logged inn, go to file (upper left corner)
5.3 file -> global config -> API -> settings 
5.4 Enable "Enable ActiveX and Socket Clients".
5.5 Enable "Read-Only API" to prevent accidental order placement or modification of your code 
5.6 Change port to 7496 for live trading or 7497 for paper trading
5.7 logging level set to "warning"




