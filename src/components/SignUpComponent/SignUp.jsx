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

  // if field is empty, returns true
  function isEmpty(val) {
    if (signinDeets[val] === "") {
      return true;
    }
    return false;
  }

  // if email is valid, returns true
  function isEmailValid() {
    const emailRegex = /\S+@\S+\.\S+/; // Basic email regex
    if (emailRegex.test(signinDeets.email)) {
      return true;
    } else {
      return false;
    }
  }

  // is pass is valid, returns true
  function isPassValid() {
    const passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@_])[A-Za-z\d@_]+$/;
    if (
      signinDeets.password.length >= 6 &&
      passRegex.test(signinDeets.password)
    ) {
      return true;
    } else {
      return false;
    }
  }

  function formatPhoneNumber(phoneNumberString) {
    var cleaned = ("" + phoneNumberString).replace(/\D/g, "");
    var match = cleaned.match(/^(1|)?(\d{3})(\d{3})(\d{4})$/);
    if (match) {
      var intlCode = match[1] ? "+1 " : "";
      return [intlCode, "(", match[2], ") ", match[3], "-", match[4]].join("");
    }
    return null;
  }
  // formatPhoneNumber("+12345678900"); // => "+1 (234) 567-8900"
  // formatPhoneNumber("2345678900"); // => "(234) 567-8900"

  // if confirm pass is valid, returns true
  function isConfirmPassValid() {
    if (signinDeets.password === signinDeets.confirm_password) {
      return true;
    } else {
      return false;
    }
  }

  function submitForm(event) {
    event.preventDefault(); // Prevent default form submission behavior
    let valToCheck = ["first_name", "last_name", "user_name", "phone"];

    let copyErr = { ...err };

    let flag = false;

    valToCheck.forEach((item) => {
      if (isEmpty(item)) {
        copyErr[item] = true;
        flag = true;
      } else {
        copyErr[item] = false;
      }
    });

    // if email is not valid, set err field to true
    if (!isEmailValid()) {
      copyErr.email = true;
      flag = true;
    } else {
      copyErr.email = false;
    }

    // if pass is not valid, set err field to true
    if (!isPassValid()) {
      copyErr.password = true;
      flag = true;
    } else {
      copyErr.password = false;
    }

    // if confirmpass is not valid, set err field to true
    if (!isConfirmPassValid()) {
      copyErr.confirm_password = true;
      flag = true;
    } else {
      copyErr.confirm_password = false;
    }

    // set error object
    setErr(copyErr);
    console.log(flag);

    if (flag === true) {
      return;
    } else {
      console.log("reached");
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
  }

  function handleChange(event) {
    let field = event.target.id;
    let value = event.target.value;
    let copyLog = { ...signinDeets };
    copyLog[field] = value;
    setSigninDeets(copyLog);
    if (field === "phone") {
      console.log("hi phone");
    }
    event.target.setCustomValidity("");
  }

  return (
    <div className="signin-container">
      <div className="firstname-lastname-container">
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
          hasError={err.first_name ? true : false}
        />
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
          hasError={err.last_name ? true : false}
        />
      </div>
      <div className="username-phone-container">
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
          hasError={err.user_name ? true : false}
        />
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
          hasError={err.phone ? true : false}
        />
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
        value={signinDeets.password}
        onChange={(event) => {
          handleChange(event);
        }}
        hasError={err.password ? true : false}
        required={true}
      />
      {err.password === true && (
        <Error error="Password must have uppercase, lowercase, number, and @ or _." />
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
        hasError={err.confirm_password ? true : false}
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
