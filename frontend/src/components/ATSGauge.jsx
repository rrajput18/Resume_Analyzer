import React, { useEffect, useState } from 'react';
import { CheckIcon, WarningIcon } from './Icons';

const ATSGauge = ({ scores, formattingAnalysis }) => {
  const [animatedScore, setAnimatedScore] = useState(0);
  const score = scores.ats_score;

  useEffect(() => {
    if (score === 0) {
      setAnimatedScore(0);
      return;
    }

    // Animate score counter on mount
    let start = 0;
    const duration = 1000; // 1s
    const stepTime = Math.max(Math.floor(duration / score), 10);
    
    const timer = setInterval(() => {
      start += 1;
      if (start >= score) {
        clearInterval(timer);
        setAnimatedScore(score);
      } else {
        setAnimatedScore(start);
      }
    }, stepTime);

    return () => clearInterval(timer);
  }, [score]);

  // Determine color theme based on score
  const getThemeColor = (val) => {
    if (val < 50) return { stroke: "#ef4444", text: "text-red", shadow: "rgba(239, 68, 68, 0.2)" };
    if (val < 75) return { stroke: "#f59e0b", text: "text-yellow", shadow: "rgba(245, 158, 11, 0.2)" };
    return { stroke: "#10b981", text: "text-green", shadow: "rgba(16, 185, 129, 0.2)" };
  };

  const theme = getThemeColor(score);
  
  // Circular progress dimensions
  const radius = 60;
  const strokeWidth = 10;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (animatedScore / 100) * circumference;

  return (
    <div className="ats-gauge-container glass-card">
      <h2 className="section-title">ATS Match Prediction</h2>
      <p className="section-subtitle">Overall score representing your profile's compatibility across all listed roles.</p>
      
      <div className="gauge-grid">
        <div className="gauge-circle-wrapper">
          <svg className="gauge-svg" width="160" height="160" viewBox="0 0 160 160">
            <circle
              className="gauge-track"
              cx="80"
              cy="80"
              r={radius}
              strokeWidth={strokeWidth}
            />
            <circle
              className="gauge-fill"
              cx="80"
              cy="80"
              r={radius}
              strokeWidth={strokeWidth}
              stroke={theme.stroke}
              strokeDasharray={circumference}
              strokeDashoffset={strokeDashoffset}
              strokeLinecap="round"
              style={{ filter: `drop-shadow(0 0 6px ${theme.stroke})` }}
            />
          </svg>
          <div className="gauge-score-value">
            <span className="score-num">{animatedScore}%</span>
            <span className="score-label">MATCH</span>
          </div>
        </div>

        <div className="score-breakdowns">
          <h3 className="card-subtitle">Factor Breakdown</h3>
          
          <div className="factor-item">
            <div className="factor-info">
              <span>Contextual Similarity</span>
              <span>{scores.semantic_similarity}%</span>
            </div>
            <div className="factor-bar">
              <div className="factor-bar-fill fill-blue" style={{ width: `${scores.semantic_similarity}%` }}></div>
            </div>
          </div>

          <div className="factor-item">
            <div className="factor-info">
              <span>Skills Requirements</span>
              <span>{scores.skills_match}%</span>
            </div>
            <div className="factor-bar">
              <div className="factor-bar-fill fill-purple" style={{ width: `${scores.skills_match}%` }}></div>
            </div>
          </div>

          <div className="factor-item">
            <div className="factor-info">
              <span>Format & Structure</span>
              <span>{scores.formatting_check}%</span>
            </div>
            <div className="factor-bar">
              <div className="factor-bar-fill fill-emerald" style={{ width: `${scores.formatting_check}%` }}></div>
            </div>
          </div>
        </div>
      </div>

      <div className="formatting-feedback-section glass-card-nested">
        <h3 className="card-subtitle flex-items-center">
          <WarningIcon className="w-5 h-5 text-indigo icon-margin-right" />
          Formatting Audit Notes
        </h3>
        {formattingAnalysis.observations.length > 0 ? (
          <ul className="observations-list">
            {formattingAnalysis.observations.map((obs, index) => (
              <li key={index} className="obs-item">
                <span className="bullet-dot red-dot"></span>
                {obs}
              </li>
            ))}
          </ul>
        ) : (
          <div className="obs-success">
            <CheckIcon className="w-5 h-5 text-green" />
            <p>Excellent formatting! No structure issues or standard section omissions detected.</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default ATSGauge;
