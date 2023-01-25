// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721 {
    uint256 public tokenCounter;

    constructor() public ERC721("AlNew", "Team") {
        tokenCounter = 0;
    }

    function createCollectible(string memory tokenURI, uint256 MyCounter)
        public
        returns (uint256)
    {
        uint256 newTokenId = MyCounter;

        _safeMint(msg.sender, MyCounter);
        _setTokenURI(MyCounter, tokenURI);
        tokenCounter += 1;
        return newTokenId;
    }
}
