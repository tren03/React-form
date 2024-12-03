import React, { useContext, useEffect } from "react";
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
    fetch("http://localhost:8000/get_tasks")
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
