import { useState, createContext } from "react";

export const TaskContext = createContext();

export const TaskContextProvider = ({ children }) => {
  // These are used to fileter through and display
  const [globalTasks, setGlobalTasks] = useState([]);

  // These tasks are rendered
  const [tasks, setTasks] = useState([]);

  const [categories, setCategories] = useState([
    "Low Priority",
    "Medium Priority",
    "High Priority",
    "All Tasks",
  ]);

  const [showModal, setShowModal] = useState(false);

  const [updateFlag, setUpdateFlag] = useState({
    isUpdate: false,
    taskId: null,
  });

  return (
    <TaskContext.Provider
      value={{
        globalTasks,
        setGlobalTasks,
        tasks,
        setTasks,
        showModal,
        setShowModal,
        categories,
        setCategories,
        updateFlag,
        setUpdateFlag,
      }}
    >
      {children}
    </TaskContext.Provider>
  );
};
