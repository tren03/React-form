import React from "react";
import { FunctionBar } from "../FunctionBar/FunctionBar";
import { TaskButton } from "../TaskButton/TaskButton";
import { TaskContainer } from "../TaskContainer/TaskContainer";
import { TodoHeading } from "../TodoHeading/TodoHeading";
import "./TodoContainer.css";

// We need to switch out the login component for the sign in component
export const TodoContainer = () => {
  return (
    <div className="todo-container">
      <TodoHeading />
      <FunctionBar />
      <TaskContainer />
    </div>
  );
};
