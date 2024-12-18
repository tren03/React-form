import React, { useContext, useEffect } from "react";
import backendAddr from "../../../backendAddr";
import { TaskContext } from "../../../context/TaskContext";
import { FunctionBar } from "../FunctionBar/FunctionBar";
import { TaskButton } from "../TaskButton/TaskButton";
import { TaskContainer } from "../TaskContainer/TaskContainer";
import { TodoHeading } from "../TodoHeading/TodoHeading";
import "./TodoContainer.css";

// We need to switch out the login component for the sign in component
export const TodoContainer = () => {
  const { globalTasks, tasks, setGlobalTasks, setTasks } =
    useContext(TaskContext);
  // getting data from db and setting task state
  useEffect(() => {
    console.log(backendAddr);
    fetch(`${backendAddr}/crud/get_tasks`)
      .then((response) => response.json())
      .then((data) => {
        setTasks(data);
        setGlobalTasks(data);
        // console.log(data);
      })
      .catch((error) => {
        console.error("Error fetching tasks:", error);
      });
  }, []);

  return (
    <div className="todo-container">
      <TodoHeading />
      <FunctionBar />
      <TaskContainer />
    </div>
  );
};
