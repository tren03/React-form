import "./Profile.css";
import { useContext } from "react";
import React from "react";
import { GlobalContext } from "../../context/GlobalContext";

export const Profile = () => {
  const { setLogFlag } = useContext(GlobalContext); // Accessing context value

  const userData = localStorage.getItem("user");
  const userObj = JSON.parse(userData);
  console.log("succesful login, redirect to profile page");
  return (
    <div className="profile-main-container">
      <div className="profile-greeting-conatainer">
        <p>Hello {userObj.email}, Welcome to Your Profile Page</p>
      </div>
      <div>
        <div className="submitbutton-container">
          <button
            onClick={() => {
              setLogFlag({
                loginSuccess: false,
                forgotPass: false,
              });
            }}
          >
            Logout
          </button>
        </div>
      </div>
    </div>
  );
};
