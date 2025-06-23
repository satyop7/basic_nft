import base64
from src import mood_nft

def deploy_mood():
    happy_svg_uri = ""
    sad_svg_uri = ""
    with open("./images/happy.svg", "r") as f:
        happy_svg = f.read()
        happy_svg_uri = svg_to_base64_uri(happy_svg)
    with open("./images/sad.svg", "r") as f:
        sad_svg = f.read()
        sad_svg_uri = svg_to_base64_uri(sad_svg)

    mood_contract = mood_nft.deploy(happy_svg_uri , sad_svg_uri)
    mood_contract.mint_nft()
    mood_contract.flip_mood(0)  # Flipping the mood of the first NFT
    print(f"tokenURI: {mood_contract.tokenURI(0)}")

def moccasin_main():
    deploy_mood()

def svg_to_base64_uri(svg):
    """
    Convert SVG content to a base64 encoded string.
    """
    svg_bytes = svg.encode('utf-8')
    base64_svg = base64.b64encode(svg_bytes).decode('utf-8')
    return f"data:image/svg+xml;base64,{base64_svg}"