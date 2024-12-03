import { useContext } from "react";
import "./App.css";
import { Form } from "./components/FormComponent/Form";
import { Profile } from "./components/ProfileComponent/Profile";
import { GlobalContext } from "./context/GlobalContext";
import { BrowserRouter, Routes, Route } from "react-router";
import { Forgot } from "./components/ForgotComponent/Forgot";
import { Todo } from "./components/TodoApplication/Todo/Todo";

function App() {
  return (
    <BrowserRouter>
      <div className="main-container">
        <Routes>
          <Route path="/" element={<Form />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/forgotpass" element={<Forgot />} />
          <Route path="/todo" element={<Todo />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
