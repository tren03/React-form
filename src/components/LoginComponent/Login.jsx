import "./Login.css";
import { Input } from "../InputComponent/Input";
import { useState } from "react";
import { Error } from "../ErrorComponent/Error";
import { Forgot } from "../ForgotComponent/Forgot";
export const Login = ({ mode, loginDeets, setLoginDeets }) => {
  const [err, setErr] = useState({
    email: false,
    password: false,
  });
  function handleEmailChange(event) {
    let copyLog = { ...loginDeets };
    copyLog.email = event.target.value;
    setLoginDeets(copyLog);
    event.target.setCustomValidity("");
  }
  function handlePassChange(event) {
    let copyLog = { ...loginDeets };
    copyLog.password = event.target.value;
    setLoginDeets(copyLog);
    event.target.setCustomValidity("");
  }

  function isEmailValid() {
    const emailRegex = /\S+@\S+\.\S+/; // Basic email regex
    if (emailRegex.test(loginDeets.email)) {
      return true;
    } else {
      return false;
    }
  }

  function isPassValid() {
    console.log(loginDeets.password);
    if (loginDeets.password.length < 6) {
      return false;
    } else {
      return true;
    }
  }

  function submitForm(event) {
    event.preventDefault(); // Prevent default form submission behavior

    if (!isEmailValid()) {
      let copyErr = { ...setErr };
      copyErr.email = true;
      setErr(copyErr);
      return;
    } else {
      let copyErr = { ...setErr };
      copyErr.email = false;
      setErr(copyErr);
    }

    if (!isPassValid()) {
      let copyErr = { ...setErr };
      copyErr.password = true;
      setErr(copyErr);
      return;
    } else {
      let copyErr = { ...setErr };
      copyErr.password = false;
      setErr(copyErr);
    }

    // If all checks pass, proceed
    //     console.log("Form submitted successfully:", loginDeets);

    console.log(loginDeets);
    setLoginDeets({
      email: "",
      password: "",
    });
  }
  return (
    <div className="login-container">
      <Input
        type="email"
        id="email"
        name="email"
        placeholder="Email"
        value={loginDeets.email}
        onChange={handleEmailChange}
        required={true}
      />
      {err.email === true && (
        <Error error="This email is invalid, check again." />
      )}
      <Input
        type="password"
        id="password"
        name="password"
        placeholder="Password"
        value={loginDeets.password}
        onChange={handlePassChange}
        required={true}
      />
      {err.password === true && (
        <Error error="This password has less than 6 letters. " />
      )}
      <Forgot />

      <div className="submitbutton-container">
        <button onClick={(event) => submitForm(event)}> {mode} </button>
      </div>
    </div>
  );
};
