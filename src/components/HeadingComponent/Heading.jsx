import React, { useContext } from "react";
import { GlobalContext } from "../../context/GlobalContext";
import "./Heading.css";
export const Heading = () => {
  const { mode } = useContext(GlobalContext);
  return (
    <div className="heading-container" style={{ textAlign: "center" }}>
      <h1>{mode}</h1>
    </div>
  );
};
