// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

contract ModelRegistry {

    struct ModelRecord {
        uint round;
        string modelHash;
        uint accuracy;
        uint timestamp;
    }

    ModelRecord[] public records;

    function addModel(
        uint _round,
        string memory _hash,
        uint _accuracy
    ) public {

        records.push(
            ModelRecord(
                _round,
                _hash,
                _accuracy,
                block.timestamp
            )
        );
    }

    function getModel(
        uint index
    )
        public
        view
        returns
    (
        uint,
        string memory,
        uint,
        uint
    )
    {
        ModelRecord memory r = records[index];

        return (
            r.round,
            r.modelHash,
            r.accuracy,
            r.timestamp
        );
    }
}