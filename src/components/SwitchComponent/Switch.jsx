import React from "react";
import { Title } from "../Title/Title";
import "./Switch.css";

export const Switch = ({ mode, setMode }) => {
  return (
    // <div className="switch-container">
    //   <Title titleText="Login" mode={mode} setMode={setMode} />
    //   <Title titleText="SignUp" mode={mode} setMode={setMode} />
    // </div>
    <>
      {mode === "Login" ? (
        <div className="switch-container">
          <Title
            titleText="Login"
            buttonColor="#007bff"
            textColor="#ffffff"
            setMode={setMode}
          />
          <Title
            titleText="SignUp"
            buttonColor="rgba(255,255,255,0)"
            textColor="#000000"
            setMode={setMode}
          />
        </div>
      ) : (
        <div className="switch-container">
          <Title
            titleText="Login"
            buttonColor="rgba(255,255,255,0)"
            textColor="#000000"
            setMode={setMode}
          />
          <Title
            titleText="SignUp"
            buttonColor="#007bff"
            textColor="#ffffff"
            setMode={setMode}
          />
        </div>
      )}
    </>
  );
};
