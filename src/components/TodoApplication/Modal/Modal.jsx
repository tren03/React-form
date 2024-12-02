import { useContext } from "react";
import { TaskContext } from "../../../context/TaskContext";
import { ModalInfo } from "../ModalInfo/ModalInfo";
import "./Modal.css";
export const Modal = () => {
  const { showModal, setShowModal } = useContext(TaskContext);

  if (showModal) {
    return (
      <div
        className="modal-background"
        onClick={() => {
          setShowModal(false);
        }}
      >
        <div onClick={(e) => e.stopPropagation()} className="modal-container">
          <ModalInfo />
        </div>
      </div>
    );
  }
  // return (
  //   <div className="modal-container">{showModal ? <h1> hwllo </h1> : null}</div>
  // );
};
