from brownie import SimpleCollectible


def main():
    simple_collectible = SimpleCollectible[-1]
    number_of_simple_collectibles = simple_collectible()
    print(f"You have created{number_of_simple_collectibles} collectibles")
