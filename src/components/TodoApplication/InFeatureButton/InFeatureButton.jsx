import { useContext } from "react";
import { TaskContext } from "../../../context/TaskContext";
import "./InFeatureButton.css";
export const InFeatureButton = ({ action, image, id }) => {
  const { tasks, setTasks, setShowModal } = useContext(TaskContext);

  async function delete_task(taskId) {
    try {
      const response = await fetch(
        `http://localhost:8000/delete_task?id=${taskId}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        },
      );

      if (!response.ok) {
        throw new Error("Error deleting task");
      }

      // Parse the response JSON to get the updated tasks list
      const updatedTasks = await response.json();

      // Update the tasks list with the updated data
      setTasks(updatedTasks);
    } catch (err) {
      console.log("Error while deleting task:", err);
    }
  }

  function update_task(taskId) {
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
