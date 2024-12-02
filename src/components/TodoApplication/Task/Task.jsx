import React from "react";
import { TaskButton } from "../TaskButton/TaskButton";
import "./Task.css";

// We need to switch out the login component for the sign in component
export const Task = () => {
  return (
    <div className="task-container">
      <TaskButton buttonText="Add" />
      <TaskButton buttonText="Add" />
    </div>
  );
};
