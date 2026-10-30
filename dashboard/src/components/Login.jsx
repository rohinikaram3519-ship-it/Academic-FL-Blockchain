import { useState } from "react";
import users from "../data/users.json";


export default function Login({ onLogin, onRegister }) {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = () => {

  const user = users.find(

    u =>

    u.username === username &&

    u.password === password

  );

  if(user){

    onLogin(user);

  }
  else{

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