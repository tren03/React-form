import React from "react";
import "./Title.css";

export const Title = ({ titleText, setMode }) => {
  return (
    <div className="title-container">
      <button onClick={() => setMode(titleText)}> {titleText} </button>
    </div>
  );
};
