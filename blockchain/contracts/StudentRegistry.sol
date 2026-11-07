// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

contract StudentRegistry {

    struct Student {

    uint studentId;

    string nodeId;

    address walletAddress;

}

    Student[] public students;

    function registerStudent(
        uint _studentId,
        string memory _nodeId,
        address _walletAddress
    ) public {

        students.push(
            Student(
                _studentId,
                _nodeId,
                _walletAddress
            )
        );
    }

    function getStudent(
        uint index
    )
        public
        view
        returns
    (
        uint,
        string memory,
        address
    )
    {
        Student memory s = students[index];

        return (
            s.studentId,
            s.nodeId,
            s.walletAddress
        );
    }
}
