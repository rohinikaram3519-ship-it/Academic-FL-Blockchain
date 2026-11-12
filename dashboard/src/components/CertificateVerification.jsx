import { useState } from "react";
import records from "../data/certificate_records.json";

export default function CertificateVerification({
  history,
  setHistory,
  user
}) {

  const [selectedFile, setSelectedFile] = useState(null);

  const [result, setResult] = useState(null);

  

 const verifyCertificate = async () => {

  if (!selectedFile) {

    alert(
      "Please upload a certificate"
    );

    return;
  }

  
  const formData =
    new FormData();

  formData.append(
    "file",
    selectedFile
  );

  const response =
    await fetch(
      "http://127.0.0.1:5000/extract",
      {
        method: "POST",
        body: formData
      }
    );

  const data =
  await response.json();

  if (
  data.status ===
  "FORGED"
) {

  setResult({
    studentId:
      data.studentId || "Unknown",

    status:
      "FORGED",

    result:
      "INVALID"
  });

  setHistory((prev) => [
    ...prev,
    {
      studentId:
        data.studentId || "Unknown",

      status: "FORGED",

      verification: "Invalid"
    }
  ]);

  return;
}

  if (
  data.status ===
  "GENUINE"
) {

  console.log(
    "✅ Genuine Certificate"
  );

} 

  console.log("Flask Response:", data);

  const studentId =
      data.studentId
      ?.toString()
       .trim();

  console.log(
     "Extracted Student ID:",
     studentId
    );
   


    if (
  data.status === "GENUINE"
) {

  setResult(data);

  setHistory((prev) => [
    ...prev,
    {
      studentId:
        data.studentId || "-",

      module: "-",

      status:
      "GENUINE",

      verification:
      "Verified"
    }
  ]);

  return;
}

setResult(false);

};

  return (

    <div className="card verification-container">

      <h2><b>Certificate Verification Portal</b></h2>

      <p>
        Upload a certificate to verify
      </p>

      <input
        type="file"
        accept=".pdf,.jpg,.jpeg,.png"
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


      {result && result.status !== "FORGED" &&  (

        <div className="result-container">
          <div className="student-info">

          <h3>
            Certificate Analysis
          </h3>

          <p>
  <strong>
    Forgery Status:
  </strong>
  ✅ Genuine
</p>

<p>
  <strong>
    Student ID:
  </strong>
  {result.studentId}
</p>

<p>
  <strong>
    Student Name:
  </strong>
  {result.studentName}
</p>

<p>
  <strong>University:</strong>{" "}
  {result.university}
</p>

<p>
  <strong>Certificate:</strong>{" "}
  {result.certificateName}
</p>


<p>
  <strong>
    USN:
  </strong>
  {result.usn}
</p>

<p>
  <strong>
    SGPA:
  </strong>
  {result.sgpa}
</p>

<p>
  <strong>
    CGPA:
  </strong>
  {result.cgpa}
</p>

         </div> 
          <div className="pdf-preview">

          <h3>Uploaded Certificate</h3>

           <div className="pdf-box">

            {selectedFile ? (

              selectedFile.type.includes("image")

              ? (

               <img
                 src={URL.createObjectURL(selectedFile)}
                 alt="Certificate Preview"
                style={{
                  width: "100%",
                 height: "100%",
                objectFit: "contain"
              }}
             />

           ) : (
           <iframe
            src={URL.createObjectURL(selectedFile)}
            title="PDF Preview"
            width="100%"
            height="100%"
            style={{
            border: "none"
            }}
           />
          )
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

      {result && result.status === "FORGED" && (

  <div className="invalid">

    <h3>
      Forged Certificate Detected
    </h3>

    <p>
      <strong>Student ID:</strong>{" "}
      {result.studentId}
    </p>

    <p>
      <strong>Status:</strong>{" "}
     {result.status}
    </p>

    <p>
      <strong>Result:</strong>{" "}
      {result.result}
    </p>

  </div>

)}

    </div>
  );
}