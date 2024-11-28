import "./SignUp.css";
import { useState } from "react";
import { Error } from "../ErrorComponent/Error";
import { Input } from "../InputComponent/Input";
export const SignUp = ({ mode, signinDeets, setSigninDeets }) => {
  const [err, setErr] = useState({
    first_name: false,
    last_name: false,
    user_name: false,
    phone: false,
    email: false,
    password: false,
    confirm_password: false,
  });
  const [flag, setFlag] = useState(false);

  function isEmpty(val) {
    console.log("reached");
    if (signinDeets[val] === "") {
      return true;
    }
    return false;
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
    // console.log("all should be true", err);
    let valToCheck = ["first_name", "last_name", "user_name", "phone"];

    if (!isEmailValid()) {
      let copyErr = { ...err };
      copyErr.email = true;
      setErr(copyErr);
      return;
    } else {
      let copyErr = { ...err };
      copyErr.email = false;
      setErr(copyErr);
    }

    if (!isPassValid()) {
      let copyErr = { ...err };
      copyErr.password = true;
      setErr(copyErr);
    } else {
      let copyErr = { ...err };
      copyErr.password = false;
      setErr(copyErr);
    }
    if (!isConfirmPassValid()) {
      let copyErr = { ...err };
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
      first_name: "",
      last_name: "",
      user_name: "",
      email: "",
      password: "",
      phone: "",
      confirm_password: "",
    });
  }
  function handleChange(event) {
    let field = event.target.id;
    let value = event.target.value;
    let copyLog = { ...signinDeets };
    copyLog[field] = value;
    setSigninDeets(copyLog);
    event.target.setCustomValidity("");
  }

  return (
    <div className="signin-container">
      <div className="name-container">
        <Input
          type="text"
          id="first_name"
          name="first_name"
          placeholder="First Name"
          value={signinDeets.first_name}
          onChange={(event) => {
            handleChange(event);
          }}
          required={true}
        />
        {err.first_name === true && <Error error="First Name is empty" />}
        <Input
          type="text"
          id="last_name"
          name="last_name"
          placeholder="Last Name"
          value={signinDeets.last_name}
          onChange={(event) => {
            handleChange(event);
          }}
          required={true}
        />
      </div>
      {err.last_name === true && <Error error="Last Name is empty" />}
      <div className="phone-container">
        <Input
          type="text"
          id="user_name"
          name="user_name"
          placeholder="Username"
          value={signinDeets.user_name}
          onChange={(event) => {
            handleChange(event);
          }}
          required={true}
        />
        {err.user_name === true && <Error error="Username is empty" />}
        <Input
          type="tel"
          id="phone"
          name="phone"
          placeholder="Phone Number"
          value={signinDeets.phone}
          onChange={(event) => {
            handleChange(event);
          }}
          required={true}
        />
        {err.phone === true && <Error error="Phone Number is empty" />}
      </div>
      <Input
        type="email"
        id="email"
        name="email"
        placeholder="Email"
        value={signinDeets.email}
        onChange={(event) => {
          handleChange(event);
        }}
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
        onChange={(event) => {
          handleChange(event);
        }}
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
        onChange={(event) => {
          handleChange(event);
        }}
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
