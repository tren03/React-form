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

async function submitForm(
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
    let stat = await sendLoginDeets(loginDeets);
    // setLoginDeets({
    //   email: "",
    //   password: "",
    // });
    console.log(stat);
    if (stat === 200) {
      console.log("reaacheddd");
      navigate("/todo");
    }
  }
}

async function sendLoginDeets(loginDeets) {
  const formData = new URLSearchParams();
  formData.append("username", loginDeets.email); // Assuming loginDeets.email is used as the username
  formData.append("password", loginDeets.password);

  const response = await fetch(`${backendAddr}/v1/auth/token`, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/x-www-form-urlencoded", // This matches the curl Content-Type
    },
    body: formData, // The form data is automatically encoded as application/x-www-form-urlencoded
  });

  if (response.status == 200) {
    alert("Authenticated");
    return 200;
  }

  if (response.status == 404) {
    alert("User doesnt exist");
  }

  if (response.status == 400) {
    alert("Invalid credentials");
  }
}
export {
  handleEmailChange,
  handlePassChange,
  isEmailValid,
  isPassValid,
  submitForm,
};
