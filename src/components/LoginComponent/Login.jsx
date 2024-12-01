import "./Login.css";
import { Input } from "../InputComponent/Input";
import { useContext, useState } from "react";
import { Error } from "../ErrorComponent/Error";
import { Forgot } from "../ForgotComponent/Forgot";
import {
  handleEmailChange,
  handlePassChange,
  submitForm,
} from "../../utils/LoginUtils";
import { GlobalContext } from "../../context/GlobalContext";
export const Login = () => {
  const { logFlag, setLogFlag, mode, loginDeets, setLoginDeets } =
    useContext(GlobalContext);
  const [err, setErr] = useState({
    email: false,
    password: false,
  });

  return (
    <div className="login-container">
      <Input
        type="email"
        id="email"
        name="email"
        placeholder="Email"
        value={loginDeets.email}
        onChange={(event) =>
          handleEmailChange(event, loginDeets, setLoginDeets)
        }
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
        onChange={(event) => handlePassChange(event, loginDeets, setLoginDeets)}
        hasError={err.password ? true : false}
      />
      {err.password === true && (
        <Error error="Enter a password greater than 6 characters " />
      )}
      {console.log(setLogFlag)}

      {/* i cannot figure out why this logflag is not getting passed to forgot component*/}
      <Forgot />
      <div className="submitbutton-container">
        <button
          onClick={(event) =>
            submitForm(
              event,
              loginDeets,
              setLoginDeets,
              err,
              setErr,
              setLogFlag,
            )
          }
        >
          {" "}
          {mode}{" "}
        </button>
      </div>
    </div>
  );
};
