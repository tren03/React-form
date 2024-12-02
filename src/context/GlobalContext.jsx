import { useState, createContext } from "react";

export const GlobalContext = createContext();

export const GlobalContextProvider = ({ children }) => {
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

  // const [logFlag, setLogFlag] = useState({
  //   loginSuccess: false,
  //   forgotPass: false,
  // });

  return (
    <GlobalContext.Provider
      value={{
        mode,
        setMode,
        loginDeets,
        setLoginDeets,
        signinDeets,
        setSigninDeets,
        // logFlag,
        // setLogFlag,
      }}
    >
      {children}
    </GlobalContext.Provider>
  );
};
