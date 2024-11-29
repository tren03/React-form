import "./Profile.css";
import React from "react";

export const Profile = ({ setLogFlag }) => {
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
              setLogFlag(false);
            }}
          >
            Logout
          </button>
        </div>
      </div>
    </div>
  );
};
