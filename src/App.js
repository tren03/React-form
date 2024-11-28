import { useState } from "react";
import "./App.css";
import { Form } from "./components/FormComponent/Form";

function App() {
  const [mode, setMode] = useState("Login");
  const [loginDeets, setLoginDeets] = useState({
    email: "",
    password: "",
  });
  const [signinDeets, setSigninDeets] = useState({
    email: "",
    password: "",
    confirm_password: "",
  });

  return (
    <div className="main-container">
      <Form
        mode={mode}
        setMode={setMode}
        loginDeets={loginDeets}
        setLoginDeets={setLoginDeets}
        signinDeets={signinDeets}
        setSigninDeets={setSigninDeets}
      />
    </div>
  );
}

export default App;
