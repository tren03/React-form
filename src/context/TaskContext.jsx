import { useState, createContext } from "react";

export const TaskContext = createContext();

export const TaskContextProvider = ({ children }) => {
  const [tasks, setTasks] = useState([
    {
      taskDescription: "sample task 1",
    },
    {
      taskDescription: "sample task 2",
    },
    {
      taskDescription: "sample task 3",
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
