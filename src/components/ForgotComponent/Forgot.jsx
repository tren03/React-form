import React, { useContext } from "react";
import { GlobalContext } from "../../context/GlobalContext";
import "./Forgot.css";
export const Forgot = () => {
  const { setLogFlag } = useContext(GlobalContext);
  return (
    <div className="forgot-container">
      <span
        onClick={() => {
          setLogFlag({
            loginSuccess: false,
            forgotPass: true,
          });
        }}
      >
        {" "}
        Forgot Password?{" "}
      </span>
    </div>
  );
};
