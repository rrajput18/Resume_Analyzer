import React from 'react';

const SkillsDisplay = ({ skillsData }) => {
  const { matched_skills, by_category } = skillsData;

  if (!matched_skills || matched_skills.length === 0) {
    return (
      <div className="skills-container glass-card">
        <h2 className="section-title">Extracted Skills</h2>
        <p className="no-skills-msg">No recognized tech skills were extracted. Ensure your PDF has selectable text.</p>
      </div>
    );
  }

  return (
    <div className="skills-container glass-card">
      <div className="skills-header">
        <h2 className="section-title">Extracted Profile Skills</h2>
        <span className="skills-badge-count">{matched_skills.length} Skills Identified</span>
      </div>
      <p className="section-subtitle">Categorized skills detected in your profile using NLP parsing.</p>

      <div className="skills-categories-grid">
        {Object.entries(by_category).map(([categoryName, skillsList]) => {
          if (!skillsList || skillsList.length === 0) return null;
          
          return (
            <div key={categoryName} className="category-card glass-card-nested">
              <h3 className="category-title">{categoryName}</h3>
              <div className="skills-tag-group">
                {skillsList.map((skill) => (
                  <span key={skill} className="skill-tag">
                    {skill}
                  </span>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default SkillsDisplay;
