function handleEmailChange(event, loginDeets, setLoginDeets) {
  let copyLog = { ...loginDeets };
  copyLog.email = event.target.value;
  setLoginDeets(copyLog);
  event.target.setCustomValidity("");
}

function handlePassChange(event, loginDeets, setLoginDeets) {
  let copyLog = { ...loginDeets };
  copyLog.password = event.target.value;
  setLoginDeets(copyLog);
  event.target.setCustomValidity("");
}

function isEmailValid(email) {
  const emailRegex = /\S+@\S+\.\S+/; // Basic email regex
  if (emailRegex.test(email)) {
    return true;
  } else {
    return false;
  }
}

function isPassValid(password) {
  if (password.length >= 6) {
    return true;
  } else {
    return false;
  }
}

function submitForm(event, loginDeets, setLoginDeets, err, setErr, setLogFlag) {
  event.preventDefault(); // Prevent default form submission behavior

  //flag - false means there is no error
  let flag = false;
  let copyErr = { ...err };

  if (!isEmailValid(loginDeets.email)) {
    copyErr.email = true;
    flag = true;
  } else {
    copyErr.email = false;
  }

  if (!isPassValid(loginDeets.password)) {
    copyErr.password = true;
    copyErr.wrongpassword = false;
    flag = true;
  } else {
    copyErr.password = false;
  }

  setErr(copyErr);

  if (flag === true) {
    return;
  } else {
    // all details pass check, need to check for correct login via local storage
    console.log(loginDeets);

    // handle error if localstorage disabled
    try {
      const userData = localStorage.getItem("user");
      if (userData === null) {
        console.log("wrong username password");
      } else {
        //user object exists, we need to check that now
        const userObj = JSON.parse(userData);
        if (
          userObj.email === loginDeets.email &&
          userObj.password === loginDeets.password
        ) {
          console.log("succesful login, redirect to profile page");
          setLogFlag({
            loginSuccess: true,
            forgotPass: false,
          });
        } else {
          console.log("wrong password");
          copyErr.wrongpassword = true;
          setErr(copyErr);
          return;
        }
      }
    } catch (err) {
      console.log("err getting object from localStorage");
    }

    setLoginDeets({
      email: "",
      password: "",
    });
  }
}

export {
  handleEmailChange,
  handlePassChange,
  isEmailValid,
  isPassValid,
  submitForm,
};
