import { useState, createContext } from "react";

export const TaskContext = createContext();

export const TaskContextProvider = ({ children }) => {
  const [tasks, setTasks] = useState([
    {
      taskId: "1",
      taskTitle: "Task1",
      taskDescription: "sample task 1",
      taskCategory: "High Priority",
    },
    {
      taskId: "2",
      taskTitle: "Task2",
      taskDescription: "sample task 2",
      taskCategory: "Medium Priority",
    },
    {
      taskId: "3",
      taskTitle: "Task3",
      taskDescription: "sample task 3",
      taskCategory: "Low Priority",
    },
  ]);

  const [showModal, setShowModal] = useState(false);

  return (
    <TaskContext.Provider
      value={{
        tasks,
        setTasks,
        showModal,
        setShowModal,
      }}
    >
      {children}
    </TaskContext.Provider>
  );
};
