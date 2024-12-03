import React from "react";
import { useNavigate } from "react-router";
import { TaskButton } from "../TaskButton/TaskButton";
import "./NavBar.css";

export const NavBar = () => {
  const navigate = useNavigate();
  const userData = localStorage.getItem("user");
  const userObj = userData ? JSON.parse(userData) : null;
  function logout() {
    try {
      const isLoggedIn = localStorage.setItem("isLoggedIn", "false");
      console.log("User is not logged in, redirecting to login page.");
      navigate("/");
    } catch (err) {
      console.log("err,logging you out : ", err);
      navigate("/");
    }
  }

  // Extract the first letter of the user's first name (or username)
  const userInitial =
    userObj && userObj.first_name ? "Welcome, " + userObj.first_name : "U"; // Default to "U" if the name doesn't exist
  return (
    <div className="navbar-container">
      <div className="user-initial">{userInitial}</div>
      <TaskButton handleClick={logout} buttonText="Logout" />
    </div>
  );
};
