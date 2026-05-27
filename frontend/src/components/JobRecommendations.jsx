import React, { useState } from 'react';
import { SearchIcon, LocationIcon, BriefcaseIcon, CashIcon } from './Icons';

const JobRecommendations = ({ jobMatches, onSelectJob }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedDept, setSelectedDept] = useState('All');

  // Extract unique departments for filter buttons
  const departments = ['All', ...new Set(jobMatches.map(job => job.department))];

  // Filter jobs based on search term and selected department
  const filteredJobs = jobMatches.filter(job => {
    const matchesSearch = 
      job.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      job.company.toLowerCase().includes(searchTerm.toLowerCase()) ||
      job.skills_analysis.matched_skills.some(s => s.toLowerCase().includes(searchTerm.toLowerCase()));
      
    const matchesDept = selectedDept === 'All' || job.department === selectedDept;
    
    return matchesSearch && matchesDept;
  });

  const getScoreColor = (score) => {
    if (score < 50) return "score-red";
    if (score < 75) return "score-yellow";
    return "score-green";
  };

  const getCompanyInitials = (company) => {
    return company
      .split(' ')
      .map(word => word[0])
      .join('')
      .slice(0, 2)
      .toUpperCase();
  };

  const getCompanyGradient = (company) => {
    let hash = 0;
    for (let i = 0; i < company.length; i++) {
      hash = company.charCodeAt(i) + ((hash << 5) - hash);
    }
    const hue1 = Math.abs(hash % 360);
    const hue2 = (hue1 + 45) % 360;
    return `linear-gradient(135deg, hsl(${hue1}, 70%, 50%) 0%, hsl(${hue2}, 75%, 42%) 100%)`;
  };

  return (
    <div className="recommendations-container glass-card">
      <div className="recommendations-header">
        <h2 className="section-title">Job Recommendations</h2>
        <p className="section-subtitle">Real-time matching scores calculated via semantic representation and skills matrix.</p>
      </div>

      <div className="filters-bar">
        {/* Search Input */}
        <div className="search-wrapper">
          <SearchIcon className="search-svg-icon w-5 h-5" />
          <input 
            type="text" 
            placeholder="Search by role, company, or skills..." 
            className="search-input"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>

        {/* Department Filters */}
        <div className="dept-filters">
          {departments.map(dept => (
            <button
              key={dept}
              className={`dept-tab-btn ${selectedDept === dept ? 'active' : ''}`}
              onClick={() => setSelectedDept(dept)}
            >
              {dept}
            </button>
          ))}
        </div>
      </div>

      <div className="jobs-list-grid">
        {filteredJobs.length > 0 ? (
          filteredJobs.map((job) => {
            const atsScore = job.match_scores.ats_score;
            const topMissingSkills = job.skills_analysis.missing_skills.slice(0, 3);
            const totalMissingCount = job.skills_analysis.missing_skills.length;
            
            return (
              <div key={job.job_id} className="job-card glass-card-nested">
                <div className="job-card-top">
                  <div className="job-meta-primary">
                    <h3 className="job-title-text">{job.title}</h3>
                  </div>
                  <div className={`job-match-badge ${getScoreColor(atsScore)}`}>
                    <span className="badge-score-val">{atsScore}%</span>
                    <span className="badge-score-lbl">Match</span>
                  </div>
                </div>

                <div className="job-meta-secondary">
                  <div className="meta-item">
                    <BriefcaseIcon className="meta-icon w-4 h-4" />
                    <span>{job.department}</span>
                  </div>
                </div>

                <hr className="divider-line" />

                <div className="job-card-skills-summary">
                  <div className="skills-match-header">
                    <span>Matched Skills ({job.skills_analysis.matched_skills.length})</span>
                  </div>
                  <div className="skills-pill-group">
                    {job.skills_analysis.matched_skills.slice(0, 5).map(skill => (
                      <span key={skill} className="skill-pill-matched">{skill}</span>
                    ))}
                    {job.skills_analysis.matched_skills.length > 5 && (
                      <span className="skill-pill-more">+{job.skills_analysis.matched_skills.length - 5} more</span>
                    )}
                    {job.skills_analysis.matched_skills.length === 0 && (
                      <span className="no-skills-pill">No overlapping skills</span>
                    )}
                  </div>
                </div>

                {totalMissingCount > 0 && (
                  <div className="job-card-recommendations">
                    <div className="skills-missing-header">
                      <span>Top Skill Gaps ({totalMissingCount})</span>
                    </div>
                    <div className="skills-pill-group">
                      {topMissingSkills.map(skill => (
                        <span key={skill} className="skill-pill-missing">{skill}</span>
                      ))}
                      {totalMissingCount > 3 && (
                        <span className="skill-pill-more-missing">+{totalMissingCount - 3} more</span>
                      )}
                    </div>
                    <p className="impact-text">
                      Adding these missing skills could improve your score by up to <span className="highlight-text-emerald">{(totalMissingCount * job.skills_analysis.single_skill_value).toFixed(0)}%</span>.
                    </p>
                  </div>
                )}

                <button 
                  className="btn-outline view-details-btn"
                  onClick={() => onSelectJob(job)}
                >
                  View Details & Recommendations
                </button>
              </div>
            );
          })
        ) : (
          <div className="no-jobs-found">
            <p>No matching positions found for current search criteria.</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default JobRecommendations;
