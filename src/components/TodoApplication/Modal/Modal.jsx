import { useContext } from "react";
import { TaskContext } from "../../../context/TaskContext";
import "./Modal.css";
export const Modal = () => {
  const { showModal, setShowModal } = useContext(TaskContext);
  return (
    <div className="modal-container">{showModal ? <h1> hwllo </h1> : null}</div>
  );
};
