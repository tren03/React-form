import { useContext } from "react";
import backendAddr from "../../../backendAddr";
import { TaskContext } from "../../../context/TaskContext";
import "./InFeatureButton.css";
export const InFeatureButton = ({ action, image, id }) => {
  const { tasks, setTasks, setShowModal, setUpdateFlag } =
    useContext(TaskContext);

  async function delete_task(taskId) {
    try {
      const response = await fetch(`${backendAddr}/v1/crud/delete_task?`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
        body: JSON.stringify(taskId), // Send task ID as a JSON string
      });

      if (!response.ok) {
        throw new Error("Error deleting task");
      }

      // Parse the response JSON to get the updated tasks list
      const updatedTasks = await response.json();
      let list = updatedTasks.task_list;
      let taskList = list.map((task) => {
        let t = {
          taskId: task.task_id,
          taskTitle: task.task_title,
          taskDescription: task.task_description,
          taskCategory: task.task_category,
        };
        return t;
      });

      // Update the tasks list with the updated data
      setTasks(taskList);
    } catch (err) {
      console.log("Error while deleting task:", err);
    }
  }

  function update_task(taskId) {
    setUpdateFlag({
      isUpdate: true,
      taskId: taskId,
    });
    setShowModal(true);
    console.log(taskId);
  }

  let handleActionClick;
  if (action === "update") {
    handleActionClick = update_task;
  }
  if (action === "delete") {
    handleActionClick = delete_task;
  }
  return (
    <div className="in-feature-button-container">
      <button onClick={() => handleActionClick(id)}>
        <img src={image} alt={action} /> {/* Display the icon/image */}
      </button>
    </div>
  );
};
