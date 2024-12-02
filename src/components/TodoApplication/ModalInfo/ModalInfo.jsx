import { useContext, useState } from "react";
import { TaskContext } from "../../../context/TaskContext";
import { ModalField } from "../ModalField/ModalField";
import { TaskButton } from "../TaskButton/TaskButton";
import "./ModalInfo.css";

// in case we call model info for updating,this information should be pre filled
export const ModalInfo = ({ title = "", description = "", category = "" }) => {
  const { tasks, setTasks, setShowModal } = useContext(TaskContext);
  const [err, setErr] = useState({
    title: false,
    desc: false,
    category: false,
  });

  const [localModalDeets, setLocalModalDeets] = useState({
    title: title,
    description: description,
    category: category,
  });

  console.log("from modal :", tasks);
  console.log(setTasks);
  function handleAddTask() {
    // check if all fields have values

    let flag = false;
    let copyErr = { ...err };
    for (let field in localModalDeets) {
      if (localModalDeets[field] === "") {
        copyErr[field] = true;
        flag = true;
      } else {
        copyErr[field] = false;
      }
    }
    setErr(copyErr);

    if (flag === true) {
      console.log("fields not filled, do not update state");
    } else {
      console.log("yes you can update");
      // create object and update tasks
      let copyTasks = [...tasks];
      console.log("copytask : ", copyTasks);
      copyTasks.push({
        taskTitle: localModalDeets.title,
        taskDescription: localModalDeets.description,
        taskCategory: localModalDeets.category,
      });
      setTasks(copyTasks);
      setShowModal(false);
    }
  }

  return (
    <div className="modal-info-container">
      <ModalField
        type="text"
        name="title"
        id="title"
        placeholder="Title of the task"
        value={localModalDeets.title}
        localModalDeets={localModalDeets}
        setlocalModalDeets={setLocalModalDeets}
        hasError={err.title ? true : false}
      />
      <ModalField
        type="text"
        name="desc"
        id="description"
        placeholder="Description of the task"
        value={localModalDeets.description}
        localModalDeets={localModalDeets}
        setlocalModalDeets={setLocalModalDeets}
        hasError={err.description ? true : false}
      />
      <ModalField
        type="text"
        name="category"
        id="category"
        placeholder="Category of the task"
        value={localModalDeets.category}
        localModalDeets={localModalDeets}
        setlocalModalDeets={setLocalModalDeets}
        hasError={err.category ? true : false}
      />
      <TaskButton
        buttonText="Create/Update"
        handleClick={() => handleAddTask()}
      />
    </div>
  );
};
