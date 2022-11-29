// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "./Platinum.sol";

contract PlatinumV2 is Platinum {
    function version() public view returns (string memory) {
        return "V2";
    }
}
