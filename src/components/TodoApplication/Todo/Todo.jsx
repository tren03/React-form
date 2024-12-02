import React from "react";
import { TaskContextProvider } from "../../../context/TaskContext";
import { NavBar } from "../NavBar/NavBar";
import { TodoContainer } from "../TodoContainer/TodoContainer";
import "./Todo.css";

// We need to switch out the login component for the sign in component
export const Todo = () => {
  return (
    <TaskContextProvider>
      <div className="todo-outer-container">
        <NavBar />
        <TodoContainer />
      </div>
    </TaskContextProvider>
  );
};
