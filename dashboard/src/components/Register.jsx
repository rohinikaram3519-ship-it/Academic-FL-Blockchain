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

  const handleRegister = () => {

    alert(
      "Account Created Successfully"
    );

    onBack();

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

      </div>

    </div>

  );

}