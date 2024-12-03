import { useContext } from "react";
import { TaskContext } from "../../../context/TaskContext";
import { Task } from "../Task/Task";
import "./TaskContainer.css";

export const TaskContainer = () => {
  const { tasks, setTasks } = useContext(TaskContext);

  return (
    <div className="task-container">
      {tasks.map((element, _) => (
        <Task
          key={element.taskId}
          id={element.taskId}
          title={element.taskTitle}
          description={element.taskDescription}
          category={element.taskCategory} // Use the correct property
        />
      ))}
    </div>
  );
};
