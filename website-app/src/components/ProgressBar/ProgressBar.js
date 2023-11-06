import React from 'react'
import './ProgressBar.css'


function ProgressBar(props) {

  const radius = 80; // Radius of the circle
  const circumference = 2 * Math.PI * radius; // Calculate the circumference

  // Calculate the strokeDasharray and strokeDashoffset
  const strokeDasharray = `${circumference} ${circumference}`;
  const strokeDashoffset = circumference - (props.percentage / 100) * circumference;

  return (
      <div className="circular-progress-bar">
      <svg className="circle" width="200" height="200">
        <circle
          className="circle-background"
          r={radius}
          cx="100"
          cy="100"
          fill="transparent"
          stroke="#7984BC"
          strokeWidth="25"
        />
        <circle
          className="circle-progress"
          r={radius}
          cx="100"
          cy="100"
          fill="transparent"
          stroke="#7367F0"
          strokeWidth="25"
          strokeDasharray={strokeDasharray}
          strokeDashoffset={strokeDashoffset}
        />
      </svg>
      <div className="percentage">
        {props.percentage}%
      </div>
    </div>
  )
}

export default ProgressBar

// Designed & Developed with <3 and C@f3 by AliJenesyx