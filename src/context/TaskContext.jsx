import { useState, createContext } from "react";

export const TaskContext = createContext();

export const TaskContextProvider = ({ children }) => {
  const [tasks, setTasks] = useState([]);

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
