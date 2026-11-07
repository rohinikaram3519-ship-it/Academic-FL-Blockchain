import { useState } from "react";

export default function Register({
  onBack
}) {

  const [studentId, setStudentId] =
    useState("");

  const [studentName, setStudentName] =
    useState("");

  const [password, setPassword] =
    useState("");

  const [blockchainData,setBlockchainData] = useState(null);

  const handleRegister = async() => {
    console.log("Register button clicked");

   const response = await fetch(
      "http://127.0.0.1:5000/register",
      {
        method: "POST",

        headers: {
          "Content-Type":
            "application/json"
        },

        body: JSON.stringify({

          studentId,

          studentName,

          password

        })

      }
    );

    const data =
      await response.json();

      console.log(
        "Registration Response:",
        data
      );

    setBlockchainData(data);  

    console.log(
      "Blockchain Data:",
      data);

    alert(
   "Account Created Successfully!"
  );

   //setTimeout(() => {
   //onBack();
//}, 2000);

  };

  return (

    <div className="login-container">

      <div className="login-card">

        <h2>Create Account</h2>

        <input
          type="text"
          placeholder="Student ID"
          value={studentId}
          onChange={(e)=>
            setStudentId(
              e.target.value
            )
          }
        />

        <input
          type="text"
          placeholder="Student Name"
          value={studentName}
          onChange={(e)=>
            setStudentName(
              e.target.value
            )
          }
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e)=>
            setPassword(
              e.target.value
            )
          }
        />

        <button
          onClick={handleRegister}
        >
          Register
        </button>

        {blockchainData !== null && (

       <div className="node-card">

       <h3>
        Blockchain Identity Created
       </h3>
       

       <p>

          Student ID:
          {blockchainData.studentId}

       </p>

       <p>

        Node ID:
        {blockchainData.nodeId}

       </p>

       <p>

       Wallet Address:
      {blockchainData.walletAddress}

      </p>

      <p>

       Status:
       ✅ {blockchainData.status}

      </p>

      </div>
   )}


      </div>

    </div>

  );

}