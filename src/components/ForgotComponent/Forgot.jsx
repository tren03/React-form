import React, { useContext } from "react";
import { useNavigate } from "react-router";
import { GlobalContext } from "../../context/GlobalContext";
import "./Forgot.css";
export const Forgot = () => {
  let navigate = useNavigate();
  return (
    <div className="forgot-container">
      <span
        onClick={() => {
          navigate("/forgotpass");
        }}
      >
        {" "}
        Forgot Password?{" "}
      </span>
    </div>
  );
};
