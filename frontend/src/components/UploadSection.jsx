import React, { useState, useRef } from 'react';
import { UploadIcon, FileIcon } from './Icons';

const UploadSection = ({ onUploadStart, onUploadSuccess, onUploadError }) => {
  const [dragActive, setDragActive] = useState(false);
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const fileInputRef = useRef(null);

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const droppedFile = e.dataTransfer.files[0];
      validateAndSetFile(droppedFile);
    }
  };

  const handleChange = (e) => {
    e.preventDefault();
    if (e.target.files && e.target.files[0]) {
      validateAndSetFile(e.target.files[0]);
    }
  };

  const validateAndSetFile = (selectedFile) => {
    if (selectedFile.type !== "application/pdf" && !selectedFile.name.toLowerCase().endsWith(".pdf")) {
      onUploadError("Invalid file type. Please upload a PDF file.");
      return;
    }
    if (selectedFile.size > 5 * 1024 * 1024) {
      onUploadError("File is too large. Maximum size is 5MB.");
      return;
    }
    setFile(selectedFile);
  };

  const triggerFileInput = () => {
    fileInputRef.current.click();
  };

  const handleAnalyze = async () => {
    if (!file) return;

    setLoading(true);
    onUploadStart();

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/api/analyze", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Failed to analyze resume.");
      }

      const result = await response.json();
      onUploadSuccess(result);
    } catch (error) {
      console.error("Upload error:", error);
      onUploadError(error.message || "An error occurred while uploading/analyzing the file.");
    } finally {
      setLoading(false);
    }
  };

  const clearFile = () => {
    setFile(null);
  };

  return (
    <div className="upload-container glass-card">
      <h2 className="section-title">Upload Your Resume</h2>
      <p className="section-subtitle">
        Upload your profile in PDF format. Our AI will analyze your skills, formatting, and match you with relevant open positions.
      </p>

      {!file ? (
        <div 
          className={`dropzone ${dragActive ? "drag-active" : ""}`}
          onDragEnter={handleDrag}
          onDragOver={handleDrag}
          onDragLeave={handleDrag}
          onDrop={handleDrop}
          onClick={triggerFileInput}
        >
          <input 
            ref={fileInputRef}
            type="file" 
            className="file-input-hidden"
            accept=".pdf"
            onChange={handleChange}
          />
          <div className="dropzone-content">
            <div className="upload-icon-wrapper">
              <UploadIcon className="w-10 h-10 upload-svg" />
            </div>
            <p className="upload-prompt">
              Drag & Drop your resume here, or <span className="highlight-text">browse files</span>
            </p>
            <p className="file-restrictions">Supports PDF only (Max 5MB)</p>
          </div>
        </div>
      ) : (
        <div className="selected-file-wrapper">
          <div className="file-details glass-card-nested">
            <FileIcon className="w-12 h-12 file-svg" />
            <div className="file-info">
              <p className="file-name">{file.name}</p>
              <p className="file-size">{(file.size / (1024 * 1024)).toFixed(2)} MB</p>
            </div>
            {!loading && (
              <button className="clear-btn" onClick={clearFile} aria-label="Clear file">
                &times;
              </button>
            )}
          </div>

          {loading ? (
            <div className="analysis-progress-wrapper">
              <div className="loader-ring"></div>
              <p className="progress-step-text">Processing...</p>
            </div>
          ) : (
            <button className="btn-primary start-analysis-btn" onClick={handleAnalyze}>
              Analyze Profile & Recommend Jobs
            </button>
          )}
        </div>
      )}
    </div>
  );
};

export default UploadSection;
