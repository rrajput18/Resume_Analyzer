import React from 'react';
import { LocationIcon, BriefcaseIcon, CashIcon, CheckIcon, WarningIcon } from './Icons';

const JobDetailsModal = ({ job, onClose }) => {
  if (!job) return null;

  const atsScore = job.match_scores.ats_score;
  const missingCount = job.skills_analysis.missing_skills.length;
  const singleValue = job.skills_analysis.single_skill_value;
  const potentialIncrease = (missingCount * singleValue).toFixed(0);

  const handleBackdropClick = (e) => {
    if (e.target === e.currentTarget) {
      onClose();
    }
  };

  return (
    <div className="modal-backdrop" onClick={handleBackdropClick}>
      <div className="modal-content glass-card animate-modal-in">
        <div className="modal-header">
          <div className="modal-title-area">
            <h2 className="modal-job-title">{job.title}</h2>
          </div>
          <button className="modal-close-btn" onClick={onClose} aria-label="Close modal">
            &times;
          </button>
        </div>

        <div className="modal-body">
          {/* Top Metadata Row */}
          <div className="modal-metadata-row">
            <div className="meta-badge">
              <BriefcaseIcon className="meta-badge-icon" />
              <span>{job.department}</span>
            </div>
            <div className={`meta-badge-score ${atsScore >= 75 ? 'bg-green' : atsScore >= 50 ? 'bg-yellow' : 'bg-red'}`}>
              <span>{atsScore}% Compatibility</span>
            </div>
          </div>

          <div className="modal-grid">
            {/* Left: Description */}
            <div className="modal-desc-col">
              <h3 className="modal-subheading">Job Description</h3>
              <p className="job-description-text">{job.description}</p>
              
              <h3 className="modal-subheading">Why This Score?</h3>
              <ul className="score-explanation-list">
                <li>
                  <strong className="text-blue">Semantic Similarity Match: {job.match_scores.semantic_similarity}%</strong>
                  <p className="sub-text">Our Sentence Transformer model evaluated how close your resume's contextual background aligns with this job description's responsibilities.</p>
                </li>
                <li>
                  <strong className="text-purple">Skills Alignment: {job.match_scores.skills_match}%</strong>
                  <p className="sub-text">You possess {job.skills_analysis.matched_skills.length} out of {job.skills_analysis.matched_skills.length + job.skills_analysis.missing_skills.length} requested skill markers.</p>
                </li>
              </ul>
            </div>

            {/* Right: Skills Analysis & Recommendations */}
            <div className="modal-skills-col">
              <h3 className="modal-subheading">Skills Overlap Analysis</h3>
              
              <div className="skills-comparison-box">
                {/* Matched Skills */}
                <div className="skills-compare-list">
                  <h4 className="compare-title text-green flex-items-center">
                    <CheckIcon className="icon-margin-right" />
                    Matched Skills ({job.skills_analysis.matched_skills.length})
                  </h4>
                  <div className="compare-pills">
                    {job.skills_analysis.matched_skills.map(skill => (
                      <span key={skill} className="pill-compare-matched">{skill}</span>
                    ))}
                    {job.skills_analysis.matched_skills.length === 0 && (
                      <span className="no-compare-pill">No overlapping skills found.</span>
                    )}
                  </div>
                </div>

                {/* Missing Skills */}
                <div className="skills-compare-list margin-top-lg">
                  <h4 className="compare-title text-red flex-items-center">
                    <WarningIcon className="icon-margin-right" />
                    Missing Skills ({job.skills_analysis.missing_skills.length})
                  </h4>
                  <div className="compare-pills">
                    {job.skills_analysis.missing_skills.map(skill => (
                      <span key={skill} className="pill-compare-missing">{skill}</span>
                    ))}
                    {job.skills_analysis.missing_skills.length === 0 && (
                      <span className="no-compare-pill text-green">You have all required skills!</span>
                    )}
                  </div>
                </div>
              </div>

              {missingCount > 0 && (
                <div className="tailoring-recommendations glass-card-nested">
                  <h4 className="recommendation-title">Tailoring Recommendations</h4>
                  <p className="rec-text">
                    By adding keywords related to <strong className="text-indigo">{job.skills_analysis.missing_skills.slice(0, 2).join(' and ')}</strong> into your resume, you could increase your compatibility score by up to <strong className="text-green">{potentialIncrease}%</strong>.
                  </p>
                  <p className="rec-tip">
                    <strong>Tip:</strong> Rather than just listing these skills in a list, weave them into your "Experience" or "Projects" descriptions by detailing how you've applied them (even in academic settings or self-study).
                  </p>
                </div>
              )}
            </div>
          </div>
        </div>

        <div className="modal-footer">
          <button className="btn-secondary" onClick={onClose}>Close</button>
        </div>
      </div>
    </div>
  );
};

export default JobDetailsModal;
