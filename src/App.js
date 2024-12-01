import { useContext } from "react";
import "./App.css";
import { Form } from "./components/FormComponent/Form";
import { Profile } from "./components/ProfileComponent/Profile";
import { GlobalContext } from "./context/GlobalContext";

function App() {
  const { logFlag } = useContext(GlobalContext);

  return (
    <div className="main-container">
      {logFlag.loginSuccess ? <Profile /> : <Form />}
    </div>
  );
}

export default App;
