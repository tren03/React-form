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

    fetch(`${backendAddr}/v1/crud/get_all_tasks`, {
      method: "GET", // Specify GET method
      headers: {
        Accept: "application/json", // Specify that you expect a JSON response
      },
      credentials: "include", // This ensures that cookies are sent with the request, including HttpOnly cookies
    })
      .then((response) => response.json())
      .then((data) => {
        let list = data.task_list;
        let taskList = list.map((task) => {
          let t = {
            taskId: task.task_id,
            taskTitle: task.task_title,
            taskDescription: task.task_description,
            taskCategory: task.task_category,
          };
          return t;
        });

        setTasks(taskList);
        setGlobalTasks(taskList);
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
