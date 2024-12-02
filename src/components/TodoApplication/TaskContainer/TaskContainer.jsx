import { useContext } from "react";
import { TaskContext } from "../../../context/TaskContext";
import { Task } from "../Task/Task";
import "./TaskContainer.css";

export const TaskContainer = () => {
  const { tasks, setTasks } = useContext(TaskContext);
  console.log(tasks);

  return (
    <div className="task-container">
      {tasks.map((element, index) => (
        <Task
          key={index}
          title={element.taskTitle}
          description={element.taskDescription}
          category={element.taskCategory} // Use the correct property
        />
      ))}
    </div>
  );
};
