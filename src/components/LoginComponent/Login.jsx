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
    if (loginDeets.password.length >= 6) {
      return true;
    } else {
      return false;
    }
  }

  function submitForm(event) {
    event.preventDefault(); // Prevent default form submission behavior

    //flag - false means there is no error
    let flag = false;
    let copyErr = { ...err };

    if (!isEmailValid()) {
      copyErr.email = true;
      flag = true;
    } else {
      copyErr.email = false;
    }

    if (!isPassValid()) {
      copyErr.password = true;
      flag = true;
    } else {
      copyErr.password = false;
    }

    setErr(copyErr);

    if (flag === true) {
      return;
    } else {
      console.log(loginDeets);
      setLoginDeets({
        email: "",
        password: "",
      });
    }
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
        hasError={err.email ? true : false}
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
        hasError={err.password ? true : false}
      />
      {err.password === true && <Error error="Please Enter the password " />}
      <Forgot />

      <div className="submitbutton-container">
        <button onClick={(event) => submitForm(event)}> {mode} </button>
      </div>
    </div>
  );
};
