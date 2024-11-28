import "./SignIn.css";
import { useState } from "react";
import { Error } from "../ErrorComponent/Error";
import { Input } from "../InputComponent/Input";
export const SignIn = ({ mode, signinDeets, setSigninDeets }) => {
  const [err, setErr] = useState({
    email: false,
    password: false,
    confirm_password: false,
  });
  function handleEmailChange(event) {
    let copyLog = { ...signinDeets };
    copyLog.email = event.target.value;
    setSigninDeets(copyLog);
    event.target.setCustomValidity("");
  }
  function handlePassChange(event) {
    let copyLog = { ...signinDeets };
    copyLog.password = event.target.value;
    setSigninDeets(copyLog);
    event.target.setCustomValidity("");
  }
  function handleConfirmPassChange(event) {
    let copyLog = { ...signinDeets };
    copyLog.confirm_password = event.target.value;
    setSigninDeets(copyLog);
    event.target.setCustomValidity("");
  }
  function isEmailValid() {
    const emailRegex = /\S+@\S+\.\S+/; // Basic email regex
    if (emailRegex.test(signinDeets.email)) {
      return true;
    } else {
      return false;
    }
  }

  function isPassValid() {
    if (signinDeets.password.length < 6) {
      return false;
    } else {
      return true;
    }
  }

  function isConfirmPassValid() {
    if (signinDeets.password === signinDeets.confirm_password) {
      return true;
    } else {
      return false;
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
    if (!isConfirmPassValid()) {
      let copyErr = { ...setErr };
      copyErr.confirm_password = true;
      setErr(copyErr);
      return;
    } else {
      let copyErr = { ...setErr };
      copyErr.confirm_password = false;
      setErr(copyErr);
    }

    console.log(signinDeets);
    setSigninDeets({
      email: "",
      password: "",
      confirm_password: "",
    });
  }

  return (
    <div className="signin-container">
      <Input
        type="email"
        id="email"
        name="email"
        placeholder="Email"
        value={signinDeets.email}
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
        value={signinDeets.password}
        onChange={handlePassChange}
        required={true}
      />
      {err.password === true && (
        <Error error="This password has less than 6 letters. " />
      )}
      <Input
        type="password"
        id="confirm_password"
        name="confirm_password"
        placeholder="Confirm Password"
        value={signinDeets.confirm_password}
        onChange={handleConfirmPassChange}
        required={true}
      />
      {err.confirm_password === true && (
        <Error error="The passwords do not match" />
      )}
      <div className="submitbutton-container">
        <button onClick={(event) => submitForm(event)}> {mode} </button>
      </div>
    </div>
  );
};
