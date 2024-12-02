import React from "react";
import { TaskContextProvider } from "../../../context/TaskContext";
import { TaskContainer } from "../TaskContainer/TaskContainer";
import { TaskInput } from "../TaskInput/TaskInput";
import "./TodoContainer.css";

// We need to switch out the login component for the sign in component
export const TodoContainer = () => {
  return (
    <TaskContextProvider>
      <div className="todo-outer-container">
        <div className="todo-container">
          <TaskInput />
          <TaskContainer />
        </div>
      </div>
    </TaskContextProvider>
  );
};
