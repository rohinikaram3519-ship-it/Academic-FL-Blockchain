import { useState } from "react";
import records from "../data/certificate_records.json";

export default function CertificateVerification({
  history,
  setHistory
}) {

  const [selectedFile, setSelectedFile] = useState(null);

  const [result, setResult] = useState(null);

  

 const verifyCertificate = () => {

  if (!selectedFile) {

    alert(
      "Please upload a certificate"
    );

    return;
  }

  const filename =
    selectedFile.name;

  const studentId =
    filename
      .replace("CERT_", "")
      .replace(".pdf", "");

  const student =
    records.find(

      (record) =>

      record.studentId
      .toString() === studentId

    );

  if (student) {

  setResult(student);

  setHistory((prev) => [
    ...prev,
    {
      studentId: student.studentId,
      module: student.module,
      status: student.status,
      verification: "Verified"
    }
  ]);

} else {

  setResult(false);

  setHistory((prev) => [
    ...prev,
    {
      studentId: studentId,
      module: "-",
      status: "-",
      verification: "Invalid"
    }
  ]);

}

};

  return (

    <div className="card verification-container">

      <h2><b>Certificate Verification Portal</b></h2>

      <p>
        Upload a certificate to verify
      </p>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) =>
          setSelectedFile(
            e.target.files[0]
          )
        }
      />

      <button
       onClick={verifyCertificate}
       >
       Verify Certificate
      </button>


      {result && (

        <div className="verify-result">

          <h3>
            Student Record Found
          </h3>

          <div className="info-row">
            <strong>Student ID:</strong>
            {result.studentId}
          </div>

          <div className="info-row">
            <strong>Module:</strong>
            {result.module}
          </div>

          <div className="info-row">
            <strong>University:</strong>
            Open University
          </div>

          <div className="info-row">
            <strong>Certificate:</strong>
            {result.status}
          </div>

          <div className="info-row">
            <strong>Blockchain:</strong>
            Verified
          </div>

          <div className="info-row">
            <strong>Attestation:</strong>
            Verified
          </div>

          <div className="info-row">
            <strong>Signature:</strong>
            Valid
          </div>

          <hr />

          <h2 className="valid">
            CERTIFICATE IS VALID
          </h2>

        </div>

      )}

      {result === false && (

        <div className="invalid">

          Student ID Not Found

        </div>

      )}

    </div>
  );
}