// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

contract AcademicVerification {

    struct StudentRecord {

        uint studentId;

        string moduleName;

        string status;

        string verificationHash;

        string attestationToken;
    }

    StudentRecord[] public records;

    function addRecord(
        uint _studentId,
        string memory _module,
        string memory _status,
        string memory _hash,
        string memory _token
    ) public {

        records.push(
            StudentRecord(
                _studentId,
                _module,
                _status,
                _hash,
                _token
            )
        );
    }

    function getRecord(
        uint index
    )
    public
    view
    returns(
        uint,
        string memory,
        string memory,
        string memory,
        string memory
    ){

        StudentRecord memory r =
        records[index];

        return(
            r.studentId,
            r.moduleName,
            r.status,
            r.verificationHash,
            r.attestationToken
        );
    }
}