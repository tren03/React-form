import React, { useContext } from "react";
import { TaskContext } from "../../../context/TaskContext";
import "./TaskButton.css";

export const TaskButton = ({ buttonText }) => {
  const { showModal, setShowModal } = useContext(TaskContext);
  return (
    <div className="task-button-container">
      <button onClick={() => setShowModal(true)}>{buttonText}</button>
    </div>
  );
};
