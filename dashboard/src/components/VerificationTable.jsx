import records from "../data/certificate_records.json";

export default function VerificationTable({
  history
}) {
  return (
    <div className="card verification-card">
      <h2><b>Academic Verification Records</b></h2>
      <div className="summary">

  <div className="summary-box">

    Total Verified :

    {
      history.filter(
        h => h.verification==="Verified"
      ).length
    }

  </div>

  <div className="summary-box">

    Total Invalid :

    {
      history.filter(
        h => h.verification==="Invalid"
      ).length
    }

  </div>

 </div>

      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Student ID</th>
              <th>Module</th>
              <th>Status</th>
              <th>Result</th>
            </tr>
          </thead>

          
      <tbody>

      {history.map((item,index)=>(

        <tr key={index}>

          <td>{item.studentId}</td>

          <td>{item.module}</td>

          <td>{item.status}</td>

          <td>

            {item.verification === "Verified"

            ?

            "✅ Verified"

            :

            "❌ Invalid"}

          </td>

        </tr>

      ))}

    </tbody>

  </table>

</div>

    </div>
  );
}