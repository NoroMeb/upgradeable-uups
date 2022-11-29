from scripts.utils import get_account, encode_function_data
from brownie import Platinum, ERC1967Proxy, Contract, PlatinumV2


def main():
    account = get_account()
    platinum = Platinum.deploy({"from": account})
    encoded_function_data = encode_function_data(platinum.initialize)
    proxy = ERC1967Proxy.deploy(
        platinum.address, encoded_function_data, {"from": account}
    )

    platinum_proxy = Contract.from_abi("Platinum", proxy.address, Platinum.abi)

    print(platinum_proxy.symbol())
    try:
        print(platinum_proxy.version())
    except AttributeError:
        pass

    platinum_v2 = PlatinumV2.deploy({"from": account})
    platinum_proxy.upgradeTo(platinum_v2.address, {"from": account})
    platinum_v2_proxy = Contract.from_abi("PlatinumV2", proxy.address, PlatinumV2.abi)

    print(platinum_v2_proxy.symbol())
    print(platinum_v2_proxy.version())
