"use client";
import { useState } from "react";
import Wrapped from "./wrapped";
import Alert from "./alert";

export default function Content() {
  const [fileValid, setFileValid] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const [year, setYear] = useState("");
  const [yearValid, setYearValid] = useState(false);
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  function handleFileUpload(event: React.ChangeEvent<HTMLInputElement>) {
    const uploadedFile = event.target.files ? event.target.files[0] : null;
    if (uploadedFile && uploadedFile.type === "text/plain") {
      setFileValid(true);
      setFile(uploadedFile);
    } else {
      setFileValid(false);
      setFile(null);
    }
  }

  function handleYearChange(event: React.ChangeEvent<HTMLInputElement>) {
    const yearInput = event.target.value;
    if (/^\d{4}$/.test(yearInput)) {
      setYearValid(true);
      setYear(yearInput);
    } else {
      setYearValid(false);
    }
  }

  function handleSendButton() {
    if (!fileValid || !file) {
      console.log("No valid file selected.");
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);
    const host = "http://127.0.0.1:8000/";
    let url = host + "api/whatsapp-wrapped";
    if (yearValid) {
      url += `?year=${year}`;
    }

    fetch(url, {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error:", error);
        setError("Failed to fetch data");
        setLoading(false);
      });
  }

  return (
    <>
      <div className="join">
        <input
          type="file"
          title="File Input"
          accept=".txt"
          className="file-input file-input-bordered file-input-primary rounded-none"
          onChange={handleFileUpload}
        />
        <label className="input input-bordered input-primary rounded-none flex items-center gap-2">
          Year:
          <input
            type="text"
            className="grow"
            placeholder={new Date().getFullYear().toString()}
            onChange={handleYearChange}
          />
          <span className="badge badge-info">Optional</span>
        </label>
        <button
          className="btn btn-primary join-item rounded-none"
          onClick={handleSendButton}
          disabled={!fileValid}
        >
          Send
        </button>
      </div>
      <div className="flex">
        {" "}
        {loading ? (
          <Alert type="alert-info" text="Loading" />
        ) : data ? (
          <Wrapped data={data} />
        ) : error ? (
          <Alert type="alert-error" text="Error" />
        ) : null}
      </div>
    </>
  );
}
