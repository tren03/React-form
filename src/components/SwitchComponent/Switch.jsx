import React, { useContext } from "react";
import { GlobalContext } from "../../context/GlobalContext";
import { Title } from "../Title/Title";
import "./Switch.css";

export const Switch = () => {
  const { mode, setMode } = useContext(GlobalContext);
  return (
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
            titleText="Sign Up"
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
            titleText="Sign Up"
            buttonColor="#007bff"
            textColor="#ffffff"
            setMode={setMode}
          />
        </div>
      )}
    </>
  );
};
