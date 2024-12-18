import backendAddr from "../backendAddr";

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

function submitForm(
  event,
  loginDeets,
  setLoginDeets,
  err,
  setErr,
  setLogFlag,
  navigate,
) {
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
    //need to validate login and get jwt
    sendLoginDeets(loginDeets);

    setLoginDeets({
      email: "",
      password: "",
    });
  }
}

async function sendLoginDeets(loginDeets) {
  const modified_deets = {
    email: loginDeets.email,
    password: loginDeets.password,
  };

  const response = await fetch(`${backendAddr}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(modified_deets), // Send the task data in JSON format
  });
  console.log(response);
}

export {
  handleEmailChange,
  handlePassChange,
  isEmailValid,
  isPassValid,
  submitForm,
};
