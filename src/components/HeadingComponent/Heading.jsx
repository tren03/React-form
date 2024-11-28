import React from "react";
import "./Heading.css";
export const Heading = ({ mode }) => {
  return (
    <div className="heading-container">
      <h1>{mode}</h1>
    </div>
  );
};
