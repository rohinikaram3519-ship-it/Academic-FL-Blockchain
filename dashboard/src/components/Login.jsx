import { useState } from "react";


export default function Login({ onLogin, onRegister }) {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {

  if (!username || !password) {

    alert(
      "Please enter username and password"
    );

    return;
  }

  const response = await fetch(
    "http://127.0.0.1:5000/login",
    {
      method: "POST",

      headers: {
        "Content-Type":
        "application/json"
      },

      body: JSON.stringify({

        username,

        password

      })
    }
  );

  const data =
    await response.json();

  if (data.success) {

    onLogin(
      data.user
    );

  } else {

    alert(
      "Invalid Credentials"
    );

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

      <p>

        Don't have an account?

      </p>

      <button
        onClick={() =>
        onRegister()
       }
      >

     Create Account

     </button>

    </div>
    </div>
  );
}