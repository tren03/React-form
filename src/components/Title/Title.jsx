import React from "react";
import "./Title.css";

export const Title = ({ titleText, buttonColor, textColor, setMode }) => {
  return (
    <div className="title-container">
      <button
        onClick={() => setMode(titleText)}
        style={{
          backgroundColor: buttonColor,
          color: textColor,
        }}
      >
        {titleText}
      </button>
    </div>
  );
};
