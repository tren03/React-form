import "./SignUp.css";
import { useContext, useState } from "react";
import { Error } from "../ErrorComponent/Error";
import { Input } from "../InputComponent/Input";
import { submitForm, handleChange } from "../../utils/SignUpUtils.js";
import { GlobalContext } from "../../context/GlobalContext";

export const SignUp = () => {
  const [err, setErr] = useState({
    first_name: false,
    last_name: false,
    user_name: false,
    phone: false,
    email: false,
    password: false,
    confirm_password: false,
  });

  const { mode, setMode, signinDeets, setSigninDeets } =
    useContext(GlobalContext);
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
            handleChange(event, signinDeets, setSigninDeets);
          }}
          hasError={err.first_name ? true : false}
        />
        <Input
          type="text"
          id="last_name"
          name="last_name"
          placeholder="Last Name"
          value={signinDeets.last_name}
          onChange={(event) => {
            handleChange(event, signinDeets, setSigninDeets);
          }}
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
            handleChange(event, signinDeets, setSigninDeets);
          }}
          hasError={err.user_name ? true : false}
        />
        <Input
          type="tel"
          id="phone"
          name="phone"
          placeholder="Phone Number"
          value={signinDeets.phone}
          onChange={(event) => {
            handleChange(event, signinDeets, setSigninDeets);
          }}
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
          handleChange(event, signinDeets, setSigninDeets);
        }}
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
          handleChange(event, signinDeets, setSigninDeets);
        }}
        hasError={err.password ? true : false}
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
          handleChange(event, signinDeets, setSigninDeets);
        }}
        hasError={err.confirm_password ? true : false}
      />
      {err.confirm_password === true && (
        <Error error="The passwords do not match" />
      )}
      <div className="submitbutton-container">
        <button
          onClick={(event) =>
            submitForm(event, signinDeets, setSigninDeets, err, setErr, setMode)
          }
        >
          {mode}
        </button>
      </div>
    </div>
  );
};
