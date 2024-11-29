import React from "react";
import { SignUp } from "../SignUpComponent/SignUp";
import { Switch } from "../SwitchComponent/Switch";
import { Login } from "../LoginComponent/Login";
import "./Form.css";
import { Heading } from "../HeadingComponent/Heading";

// We need to switch out the login component for the sign in component
export const Form = ({
  setLogFlag,
  mode,
  setMode,
  loginDeets,
  setLoginDeets,
  signinDeets,
  setSigninDeets,
}) => {
  return (
    <div className="form-outer-container">
      <Heading mode={mode} />
      <Switch mode={mode} setMode={setMode} />
      <form className="form-container">
        {mode === "Login" ? (
          <Login
            setLogFlag={setLogFlag}
            mode={mode}
            loginDeets={loginDeets}
            setLoginDeets={setLoginDeets}
          />
        ) : (
          <SignUp
            mode={mode}
            setMode={setMode}
            signinDeets={signinDeets}
            setSigninDeets={setSigninDeets}
          />
        )}
      </form>
    </div>
  );
};
