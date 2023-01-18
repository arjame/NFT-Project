This project runs on goerli and ganache Testnet to Mint nft on Test Opensea.

How to use this project?
1. Create an empty visual studio code directory and in the terminal type brownie init.
2. Put the code and install Brownie, Openzepplin and Solidity from VS code terminal.
3. Make a .env file in the main folder and put the following information:
    export PRIVATE_KEY=[Your PRIVATE_KEY]
    
4. In deploy_and_create.py change sample_token_uri =[url of jason file uploaded on IPFS] 

5.in terminal type: Brownie compile

6.in terminal type: Brownie run Scripts/deploy_and_create.py --network goerli

7. If your wallet is connected correctly, you will see the url of your nft as an output.
