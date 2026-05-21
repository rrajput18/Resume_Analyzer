import React, { useState, useEffect } from 'react';
import './App.css';

import UploadSection from './components/UploadSection';
import ATSGauge from './components/ATSGauge';
import SkillsDisplay from './components/SkillsDisplay';
import JobRecommendations from './components/JobRecommendations';
import JobDetailsModal from './components/JobDetailsModal';
import { SunIcon, MoonIcon } from './components/Icons';

function App() {
  const [analyzing, setAnalyzing] = useState(false);
  const [error, setError] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);
  const [selectedJob, setSelectedJob] = useState(null);
  const [theme, setTheme] = useState('dark');

  // Bind data-theme attribute on document root whenever theme changes
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
  }, [theme]);

  const handleUploadStart = () => {
    setAnalyzing(true);
    setError(null);
    setAnalysisResult(null);
  };

  const handleUploadSuccess = (data) => {
    setAnalysisResult(data);
    setAnalyzing(false);
  };

  const handleUploadError = (errMsg) => {
    setError(errMsg);
    setAnalyzing(false);
  };

  const handleReset = () => {
    setAnalysisResult(null);
    setError(null);
    setSelectedJob(null);
  };

  return (
    <div className="app-wrapper">
      {/* Persistent Navigation Navbar */}
      <nav className="app-navbar">
        <div className="nav-brand">
          <span className="nav-logo-text">ProfileFit®</span>
          <span className="nav-logo-badge">v1.2.0</span>
        </div>
        
        <div className="nav-actions">
          <button 
            className="theme-toggle-btn" 
            onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            title={`Switch to ${theme === 'dark' ? 'Light' : 'Dark'} Mode`}
            aria-label="Toggle theme"
          >
            {theme === 'dark' ? <SunIcon /> : <MoonIcon />}
          </button>
        </div>
      </nav>

      <main className="app-main-content">
        {/* Error Alert Box */}
        {error && (
          <div className="alert-error" role="alert">
            <strong>Error:</strong> {error}
          </div>
        )}

        {/* Upload / Analysis Section */}
        {!analysisResult && (
          <UploadSection 
            onUploadStart={handleUploadStart}
            onUploadSuccess={handleUploadSuccess}
            onUploadError={handleUploadError}
          />
        )}

        {/* Results Dashboard Layout */}
        {analysisResult && (
          <div className="results-wrapper">
            <div className="dashboard-layout">
              {/* Left Sidebar */}
              <aside className="dashboard-sidebar">
                {/* Active File Card */}
                <div className="glass-card-nested">
                  <h3 className="card-subtitle" style={{ fontSize: '0.8rem', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '0.5rem' }}>
                    Active Profile
                  </h3>
                  <div className="active-file-details">
                    <p style={{ fontWeight: 600, wordBreak: 'break-all', fontSize: '0.9rem' }}>
                      Uploaded_Resume.pdf
                    </p>
                    <p style={{ fontSize: '0.78rem', color: 'var(--text-muted)', marginTop: '0.3rem' }}>
                      Status: Extracted & Indexed
                    </p>
                  </div>
                </div>

                {/* Categorized Skills Card */}
                <SkillsDisplay skillsData={analysisResult.skills_extracted} />
                
                {/* System Pipeline Info Card */}
                <div className="glass-card-nested" style={{ opacity: 0.8 }}>
                  <h3 className="card-subtitle" style={{ fontSize: '0.8rem', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '0.5rem' }}>
                    Pipeline Details
                  </h3>
                  <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', lineHeight: 1.5 }}>
                    NLP Model: spaCy (en_core_web_sm)<br />
                    Similarity: MiniLM-L6 Cosine Embeddings<br />
                    Dataset: Locally Indexed Jobs v1.0
                  </p>
                </div>
              </aside>

              {/* Right Main Pane */}
              <div className="dashboard-main-pane">
                {/* ATS Gauge Card */}
                <ATSGauge 
                  scores={analysisResult.job_matches[0]?.match_scores || { ats_score: 0, semantic_similarity: 0, skills_match: 0, formatting_check: 0 }}
                  formattingAnalysis={analysisResult.formatting_analysis}
                />

                {/* Job Recommendations Grid */}
                <JobRecommendations 
                  jobMatches={analysisResult.job_matches}
                  onSelectJob={setSelectedJob}
                />
              </div>
            </div>

            {/* Reset / upload new resume link */}
            <div className="reset-analysis-container">
              <button className="link-btn" onClick={handleReset}>
                Upload and Analyze another Resume
              </button>
            </div>
          </div>
        )}
      </main>

      {/* Details Modal */}
      {selectedJob && (
        <JobDetailsModal 
          job={selectedJob}
          onClose={() => setSelectedJob(null)}
        />
      )}
    </div>
  );
}

export default App;
