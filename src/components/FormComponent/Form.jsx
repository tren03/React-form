import React from "react";
import { SignIn } from "../SignInComponent/SignIn";
import { Switch } from "../SwitchComponent/Switch";
import { Login } from "../LoginComponent/Login";
import "./Form.css";
import { Heading } from "../HeadingComponent/Heading";

// We need to switch out the login component for the sign in component
export const Form = ({
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
      <Switch setMode={setMode} />
      <form className="form-container">
        {mode === "Login" ? (
          <Login
            mode={mode}
            loginDeets={loginDeets}
            setLoginDeets={setLoginDeets}
          />
        ) : (
          <SignIn
            mode={mode}
            signinDeets={signinDeets}
            setSigninDeets={setSigninDeets}
          />
        )}
      </form>
    </div>
  );
};
