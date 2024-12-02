import "./Profile.css";
import { useState, useEffect } from "react";
import React from "react";
import { useNavigate } from "react-router";

export const Profile = () => {
  const [userEmail, setUserEmail] = useState("");

  // If the same thing was done without use effect, i was gettin infinite render error as setUserEmail was being called multiple times
  useEffect(() => {
    try {
      const userData = localStorage.getItem("user");
      const userObj = JSON.parse(userData);
      if (userObj) {
        setUserEmail(userObj.email);
      }
    } catch (err) {
      console.log("err getting local storage");
    }
  }, []);

  let navigate = useNavigate("/");

  return (
    <div className="profile-main-container">
      <div className="profile-greeting-conatainer">
        <p>Hello {userEmail}, Welcome to Your Profile Page</p>
      </div>
      <div>
        <div className="submitbutton-container">
          <button onClick={() => navigate("/")}>Logout</button>
        </div>
        <div className="submitbutton-container">
          <button onClick={() => navigate("/todo")}>
            Go to Todo Application
          </button>
        </div>
      </div>
    </div>
  );
};
