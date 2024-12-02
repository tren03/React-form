import React from "react";
import "./TaskButton.css";

export const TaskButton = ({ buttonText }) => {
  return (
    <div className="task-button-container">
      <button>{buttonText}</button>
    </div>
  );
};
