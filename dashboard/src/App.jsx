import "./App.css";
import { useState } from "react";

import results from "./data/results.json";

import blockchain from "./data/blockchain.json";

import records from "./data/certificate_records.json";
import VerificationTable from "./components/VerificationTable";
import StatCard from "./components/StatCard";
import CertificateVerification from "./components/CertificateVerification";

function App() {
  const [history, setHistory] = useState([]);
  return (
    <div className="dashboard">

     <header>
           <h1>
               Academic Certificate Verification
           </h1>
     </header>

    <div className="table-section">

     <VerificationTable history={history} />

    </div>

    <div className="table-section">

     <CertificateVerification
        history={history}
        setHistory={setHistory}
      />

    </div>


   </div>
  );
}

export default App;