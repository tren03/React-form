import React from "react";
import { TaskContextProvider } from "../../../context/TaskContext";
import { Modal } from "../Modal/Modal";
import { NavBar } from "../NavBar/NavBar";
import { TodoContainer } from "../TodoContainer/TodoContainer";
import "./Todo.css";

// We need to get the data from the python api endpoint

export const Todo = () => {
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
