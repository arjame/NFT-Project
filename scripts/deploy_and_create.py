from msilib.schema import PublishComponent
from scripts.helpful_scripts import get_account
from brownie import SimpleCollectible


# I need to update all the links here
sample_token_uri = {
    "Agircola": "https://ipfs.io/ipfs/QmfU1CXTwsg1ZceLSxCDe98tN94eZMdSBSA4Skdd1723MD?filename=Agircola.json",
    "Aimo": "https://ipfs.io/ipfs/QmbFatMn9yz8Syi6jWMB2o25cCCsQMc6Fx7AqU2F68Pvke?filename=Aimo.json",
    "Bargigli_Alpi": "https://ipfs.io/ipfs/QmQTd57YSE9oAAFD5XjR29fy7ymR9PBDLjuJzR4hfEC4gx?filename=Bargigli_Alpi.json",
    "Bargigli_Neos": "https://ipfs.io/ipfs/QmNddawZCeFs23xHXgijDcTTk3jzkMMqTsSKasqSnXXo9P?filename=Bargigli_Neos.json",
    "Beltramo": "https://ipfs.io/ipfs/QmbvxqVQir7EsSakF2vnX5fagEkjnck3vRL5ymR94gFmGF?filename=Beltramo.json",
    "Cafarella": "https://ipfs.io/ipfs/QmUkKUq2hBqrDsBnbvS7P1TUReCGbYNej4TBvU8ha3UVYh?filename=Cafarella.json",
    "Cariani": "https://ipfs.io/ipfs/QmPBqwfxxPry3eHKkX3UNNNQ1MbvwVeP7QdLchUCkY1Edq?filename=Cariani.json",
    "Caruso": "https://ipfs.io/ipfs/QmPnGMUZz5bWHwUbFWuKVuZP6K95abcgbLWryMKKQg9utX?filename=Caruso.json",
    "Ciuccarelli": "https://ipfs.io/ipfs/QmPZv5GprdGayMvcHCCy67SdLt31BSjXJqZq1Me1YTdwnW?filename=Ciuccarelli.json",
    "Elicona": "https://ipfs.io/ipfs/QmVwWMAYWSAgWTDDDnPPj2Cnud4DcMApiCwCqUAyWsRH1Y?filename=Elicona.json",
    "Ferrero": "https://ipfs.io/ipfs/QmXJVFTn9eBDL7zk2FvhbA1faY8je9vxFzng4vc5Hw65ai?filename=Ferrero.json",
    "Ferri": "https://ipfs.io/ipfs/QmXjLBhPVxP28QZjDmZFonq5csKTyu3mvFGr9kT9Ca4csS?filename=Ferri.json",
    "Forti": "https://ipfs.io/ipfs/QmTVeNU2ad5qEDJkX4ZSb365vWhXqspYroRNSwH82v3RhH?filename=Forti.json",
    "Gasparrini": "https://ipfs.io/ipfs/QmRp4QxhwiMPpP2DpS3t1Z13xfep7zwsfuFNYtVfXaoFCy?filename=Gasparrini.json",
    "Irrera": "https://ipfs.io/ipfs/QmVJHSbHkVFVHE5Pp5Q2mtJdWvucm8heSY8tbrELgs4nsU?filename=Irrera.json",
    "Jame": "https://ipfs.io/ipfs/QmXRryC7bEM7UUQDE3XRxUcqfLg4TfCopnFDsSrQRLvJU4?filename=Jame.json",
    "Olgiati": "https://ipfs.io/ipfs/QmUo7ZNdtMQs1phWkDdBR4xkKHD8Y26mk1FEVm4CQ7ftZP?filename=Olgiati.json",
    "Palazzolo": "https://ipfs.io/ipfs/QmdS4tJ3gHcyQs3k7NUh2K6fuEPsLdCUU3gdq4NvLzFT6U?filename=Palazzolo.json",
    "Quaranta": "https://ipfs.io/ipfs/QmSqwGa9eppKW8Gybj8BHPRyD9VoFzFSt1nG9bbmmiyNs3?filename=Quaranta.json",
    "Sarnataro_Alpi": "https://ipfs.io/ipfs/Qmc1UAT7bLxAzAj6T5f56eMp5gdmaoMBQP4nvmTFWQF3vw?filename=Sarnataro_Alpi.json",
    "Sarnataro_Neos": "https://ipfs.io/ipfs/QmeRwBaKsVgJiPHSHuFEv29oWUfmRFcW5b69Gv359Jdzou?filename=Sarnataro_Neos.json",
    "Team": "https://ipfs.io/ipfs/QmShzWYxi4VczGVLcJmi7hhj8NuqQPNHVcbMRj7jmbmGkU?filename=Team.json",
}

OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def deploy_and_create(uri, id):

    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(uri, id, {"from": account})
    tx.wait(1)
    print(
        f"Awsome you can view your nft at {OPENSEA_URL.format(simple_collectible.address, id)}"
    )
    return SimpleCollectible


def main():
    id = 0
    for i in sample_token_uri.values():
        print(i)
        id = id + 1
        print(id)
        deploy_and_create(i, id)
