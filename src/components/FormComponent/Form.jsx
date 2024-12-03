import React, { useContext } from "react";
import { SignUp } from "../SignUpComponent/SignUp";
import { Switch } from "../SwitchComponent/Switch";
import { Login } from "../LoginComponent/Login";
import "./Form.css";
import { Heading } from "../HeadingComponent/Heading";
import { GlobalContext } from "../../context/GlobalContext";

// We need to switch out the login component for the sign in component
export const Form = () => {
  const { logFlag, mode } = useContext(GlobalContext);

  return (
    <div className="form-outer-container">
      <Heading />
      <Switch />
      <form className="form-container">
        {mode === "Login" ? <Login /> : <SignUp />}
      </form>
    </div>
  );
};
