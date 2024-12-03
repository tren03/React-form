import { useContext, useEffect, useState } from "react";
import { TaskContext } from "../../../context/TaskContext";
import { ModalField } from "../ModalField/ModalField";
import { SelectInput } from "../SelectInput/SelectInput";
import { TaskButton } from "../TaskButton/TaskButton";
import "./ModalInfo.css";

// in case we call model info for updating,this information should be pre filled
export const ModalInfo = ({ title = "", description = "", category = "" }) => {
  const { tasks, setGlobalTasks, setTasks, setShowModal } =
    useContext(TaskContext);

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

  async function add_new_task(newTask) {
    try {
      const response = await fetch("http://localhost:8000/add_task", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newTask), // Send the task data in JSON format
      });

      if (!response.ok) {
        throw new Error("Error adding task");
      }

      // Parse the response JSON
      const updatedTasks = await response.json();

      // Update the tasks list with the updated data
      setTasks(updatedTasks);
      setGlobalTasks(updatedTasks);

      // Close the modal after adding the task
      setShowModal(false);
    } catch (err) {
      console.log("Error while adding task:", err);
    }
  }

  // check if all fields have values
  function handleAddTask() {
    let flag = false;
    let copyErr = { ...err };
    for (let field in localModalDeets) {
      if (localModalDeets[field] === "" && field === "category") {
        localModalDeets[field] = "Low Priority";
      }
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
      console.log("local deets are here,", localModalDeets);

      // do api req

      //id added by db itself
      let newTask = {
        taskTitle: localModalDeets.title,
        taskDescription: localModalDeets.description,
        taskCategory: localModalDeets.category,
      };

      add_new_task(newTask);
      // copyTasks.push({
      //   taskTitle: localModalDeets.title,
      //   taskDescription: localModalDeets.description,
      //   taskCategory: localModalDeets.category,
      // });
      // setTasks(copyTasks);
      setShowModal(false);
    }
  }

  function getLocalModalDeetsCategory(e) {
    setLocalModalDeets({
      ...localModalDeets,
      category: e.target.value, // Update the category value from the select
    });
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
      <div className="modal-info-select-container">
        <label> Category </label>
        <SelectInput
          className="modal-info-select"
          handleChange={getLocalModalDeetsCategory}
          optionList={["Low Priority", "Medium Priority", "High Priority"]}
        />
      </div>
      <TaskButton
        buttonText="Create/Update"
        handleClick={() => handleAddTask()}
      />
    </div>
  );
};
// <ModalField
//   type="text"
//   name="category"
//   id="category"
//   placeholder="Category of the task"
//   value={localModalDeets.category}
//   localModalDeets={localModalDeets}
//   setlocalModalDeets={setLocalModalDeets}
//   hasError={err.category ? true : false}
// />
