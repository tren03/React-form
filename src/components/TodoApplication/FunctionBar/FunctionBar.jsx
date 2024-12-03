import { useContext } from "react";
import { TaskContext } from "../../../context/TaskContext";
import { SelectInput } from "../SelectInput/SelectInput";
import { TaskButton } from "../TaskButton/TaskButton";
import "./FunctionBar.css";
export const FunctionBar = () => {
  const { setShowModal, setTasks, globalTasks } = useContext(TaskContext);
  function handleCategoryChange(e) {
    const categoryToFilter = e.target.value;
    console.log(categoryToFilter);
    if (categoryToFilter === "All Tasks") {
      setTasks(globalTasks);
      return;
    }
    let filtTasks = globalTasks.filter((item) => {
      if (item.taskCategory === categoryToFilter) {
        return true;
      }
      return false;
    });
    setTasks(filtTasks);
  }
  return (
    <div className="function-bar-container">
      <TaskButton
        buttonText="Add"
        handleClick={() => {
          setShowModal(true);
          console.log("clicked");
        }}
      />
      <SelectInput handleChange={handleCategoryChange} />
    </div>
  );
};
