import React, { useEffect } from "react";
import { useNavigate } from "react-router";
import { TaskContextProvider } from "../../../context/TaskContext";
import { Modal } from "../Modal/Modal";
import { NavBar } from "../NavBar/NavBar";
import { TodoContainer } from "../TodoContainer/TodoContainer";
import "./Todo.css";

// We need to get the data from the python api endpoint

export const Todo = () => {
  const navigate = useNavigate();
  // useEffect(() => {
  //   const isLoggedIn = localStorage.getItem("isLoggedIn");
  //
  //   if (isLoggedIn !== "true") {
  //     // If user is not logged in, redirect to login page
  //     console.log("User is not logged in, redirecting to login page.");
  //     navigate("/");
  //   }
  // });

  return (
    <TaskContextProvider>
      <div className="todo-outer-container">
        <NavBar />
        <Modal />
        <TodoContainer />
      </div>
    </TaskContextProvider>
  );
};
