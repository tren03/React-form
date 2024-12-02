import React from "react";
import { FunctionBar } from "../FunctionBar/FunctionBar";
import { TaskButton } from "../TaskButton/TaskButton";
import "./TodoContainer.css";

// We need to switch out the login component for the sign in component
export const TodoContainer = () => {
  return (
    <div className="todo-container">
      <FunctionBar />
    </div>
  );
};
