import { useState } from "react";

export default function Login({ onLogin }) {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = () => {

    if (
      username === "admin" &&
      password === "1234"
    ) {
      onLogin();
    } else {
      alert("Invalid Login");
    }
  };

  return (
    
    <div className="login-container">

    <div className="login-card">

      <h2>
        Academic Certificate Verification
      </h2>
      
      <h3>
          Login Portal
      </h3>

      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e)=>
          setUsername(e.target.value)
        }
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e)=>
          setPassword(e.target.value)
        }
      />

      <button onClick={handleLogin}>
        Login
      </button>

    </div>
    </div>
  );
}