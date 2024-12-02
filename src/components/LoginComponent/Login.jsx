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
import { useNavigate } from "react-router";
export const Login = () => {
  const { logFlag, setLogFlag, mode, loginDeets, setLoginDeets } =
    useContext(GlobalContext);
  const [err, setErr] = useState({
    email: false,
    password: false,
    wrongpassword: false,
  });

  let navigate = useNavigate();

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
        autoComplete="current-password"
        value={loginDeets.password}
        onChange={(event) => handlePassChange(event, loginDeets, setLoginDeets)}
        hasError={err.password ? true : false}
      />
      {err.password === true && (
        <Error error="Enter a password greater than 6 characters " />
      )}
      {err.wrongpassword === true && (
        <Error error="The email or password entered is wrong" />
      )}

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
              navigate,
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
