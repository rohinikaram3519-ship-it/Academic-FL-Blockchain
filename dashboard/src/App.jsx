import "./App.css";
import { useState } from "react";

import results from "./data/results.json";

import blockchain from "./data/blockchain.json";

import records from "./data/certificate_records.json";
import VerificationTable from "./components/VerificationTable";
import StatCard from "./components/StatCard";
import CertificateVerification from "./components/CertificateVerification";
import Login from "./components/Login";
import Register from "./components/Register";

function App() {
  const [history, setHistory] = useState([]);
  const [user, setUser] = useState(null);
  const [showRegister, setShowRegister] = useState(false);
  if (showRegister) {

  return (

    <Register
      onBack={() =>
        setShowRegister(false)
      }
    />

  );
  }

  if (!user) {

  return (

    <Login
       onLogin={setUser}
       onRegister={() =>
        setShowRegister(true)
     }
    />

  );
  }
  return (
    <div className="dashboard">

     <header>
           <h1>
               Academic Certificate Verification
           </h1>
     </header>
     
     <h2>

      Welcome  {user.studentName}

     </h2>
    <div className="table-section">

     <VerificationTable history={history} />

    </div>

    <div className="table-section">

     <CertificateVerification
        history={history}
        setHistory={setHistory}
        user={user}
      />

    </div>


   </div>
  );
}

export default App;