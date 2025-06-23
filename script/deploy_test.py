from src import basic_test

IMG_URI = "QmZZn9ktJd5aQv3Yyt9f7U4KrDxn1qqQC832m4hcgYfupb"

def deploy_basic_nft():
    contract = basic_test.deploy()
    contract.mint(IMG_URI)
    token_metadata = contract.tokenURI(0)
    print(token_metadata)

def moccasin_main():
    deploy_basic_nft()