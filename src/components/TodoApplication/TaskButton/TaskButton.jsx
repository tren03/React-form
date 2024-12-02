import React from "react";
import "./TaskButton.css";

export const TaskButton = ({ buttonText, handleClick }) => {
  return (
    <div className="task-button-container" onClick={handleClick}>
      <button>{buttonText}</button>
    </div>
  );
};
