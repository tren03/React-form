import React from "react";
import { Title } from "../Title/Title";
import "./Switch.css";

export const Switch = ({ setMode }) => {
  return (
    <div className="switch-container">
      <Title titleText="Login" setMode={setMode} />
      <Title titleText="SignUp" setMode={setMode} />
    </div>
  );
};
