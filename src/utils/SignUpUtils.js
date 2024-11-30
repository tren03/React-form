function handleChange(event, signinDeets, setSigninDeets) {
  let field = event.target.id;
  let value = event.target.value;
  let copyLog = { ...signinDeets };
  copyLog[field] = value;
  setSigninDeets(copyLog);
  event.target.setCustomValidity("");
}
// if field is empty, returns true
function isEmpty(val, signinDeets) {
  if (signinDeets[val] === "") {
    return true;
  }
  return false;
}

function isPhoneValid(signinDeets) {
  const regex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
  if (
    regex.test(signinDeets.phone) &&
    !isEmpty(signinDeets.phone, signinDeets)
  ) {
    return true;
  } else {
    return false;
  }
}

// console.log(validatePhoneNumber("123-456-7890")); // true
// console.log(validatePhoneNumber("123.456.7890")); // true
// console.log(validatePhoneNumber("(123) 456-7890")); // true
// console.log(validatePhoneNumber("1234567890")); // true
// console.log(validatePhoneNumber("12345")); // false

// if email is valid, returns true
function isEmailValid(email) {
  const emailRegex = /\S+@\S+\.\S+/; // Basic email regex
  if (emailRegex.test(email)) {
    return true;
  } else {
    return false;
  }
}

// is pass is valid, returns true
function isPassValid(password) {
  const passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@_])[A-Za-z\d@_]+$/;
  if (password.length >= 6 && passRegex.test(password)) {
    return true;
  } else {
    return false;
  }
}

// if confirm pass is valid, returns true
function isConfirmPassValid(password, confirm_password) {
  if (password === confirm_password) {
    return true;
  } else {
    return false;
  }
}
function submitForm(event, signinDeets, setSigninDeets, err, setErr, setMode) {
  event.preventDefault(); // Prevent default form submission behavior
  let valToCheck = ["first_name", "last_name", "user_name"];

  let copyErr = { ...err };

  let flag = false;

  valToCheck.forEach((item) => {
    if (isEmpty(item, signinDeets)) {
      copyErr[item] = true;
      flag = true;
    } else {
      copyErr[item] = false;
    }
  });

  // if email is not valid, set err field to true
  if (!isEmailValid(signinDeets.email)) {
    copyErr.email = true;
    flag = true;
  } else {
    copyErr.email = false;
  }

  // if pass is not valid, set err field to true
  if (!isPassValid(signinDeets.password)) {
    copyErr.password = true;
    flag = true;
  } else {
    copyErr.password = false;
  }

  // if confirmpass is not valid, set err field to true
  if (!isConfirmPassValid(signinDeets.password, signinDeets.confirm_password)) {
    copyErr.confirm_password = true;
    flag = true;
  } else {
    copyErr.confirm_password = false;
  }

  // if confirmpass is not valid, set err field to true
  if (!isPhoneValid(signinDeets)) {
    copyErr.phone = true;
    flag = true;
  } else {
    copyErr.phone = false;
  }

  // set error object
  setErr(copyErr);
  console.log(flag);

  if (flag === true) {
    return;
  } else {
    //sign up success
    console.log("reached");

    // need to handle error here
    localStorage.setItem("user", JSON.stringify(signinDeets));

    console.log(signinDeets);
    setSigninDeets({
      first_name: "",
      last_name: "",
      user_name: "",
      email: "",
      password: "",
      phone: "",
      confirm_password: "",
    });
    //redirect to login page after succesfull signin
    setMode("Login");
  }
}

export {
  isEmpty,
  isPhoneValid,
  isEmailValid,
  isConfirmPassValid,
  isPassValid,
  submitForm,
  handleChange,
};
