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

        <div className="result-container">
          <div className="student-info">

          <h3>
            Student Record Found
          </h3>

           <p><strong>Student ID:</strong> {result.studentId}</p>

    <p><strong>Student Name:</strong> {result.studentName}</p>

    <p><strong>University:</strong> {result.university}</p>

    <p><strong>Issue Date:</strong> {result.issueDate}</p>

    <p><strong>Certificate:</strong> {result.status}</p>

         </div> 
          <div className="pdf-preview">

          <h3>Uploaded Certificate</h3>

           <div className="pdf-box">

            {selectedFile ? (
           <iframe
            src={URL.createObjectURL(selectedFile)}
            title="PDF Preview"
            width="100%"
            height="100%"
            style={{
            border: "none"
            }}
           />
          ) : (
          <p>No PDF Uploaded</p>
          )}
          </div>
          
          <hr />
          
          <h2 className="valid">
            CERTIFICATE IS VALID
          </h2>

        </div>
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