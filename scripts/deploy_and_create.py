from scripts.helpful_scripts import get_account
from brownie import SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/QmY62ZaLYjC1y22eSGecCoifEEwZybZ9qNG37LfDcoUkp2?filename=ARJ.json"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awsome you can view your nft at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter()-1)}"
    )
    return SimpleCollectible


def main():
    deploy_and_create()
