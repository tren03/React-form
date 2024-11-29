import { useState } from "react";
import "./App.css";
import { Form } from "./components/FormComponent/Form";
import { Profile } from "./components/ProfileComponent/Profile";

function App() {
  const [mode, setMode] = useState("Login");
  const [loginDeets, setLoginDeets] = useState({
    email: "",
    password: "",
  });
  const [signinDeets, setSigninDeets] = useState({
    first_name: "",
    last_name: "",
    user_name: "",
    email: "",
    phone: "",
    password: "",
    confirm_password: "",
  });

  const [logFlag, setLogFlag] = useState(true);

  return (
    <div className="main-container">
      {logFlag ? (
        <Profile setLogFlag={setLogFlag} />
      ) : (
        <Form
          setLogFlag={setLogFlag}
          mode={mode}
          setMode={setMode}
          loginDeets={loginDeets}
          setLoginDeets={setLoginDeets}
          signinDeets={signinDeets}
          setSigninDeets={setSigninDeets}
        />
      )}
    </div>
  );
}

export default App;
