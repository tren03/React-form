import { useContext } from "react";
import { TaskContext } from "../../../context/TaskContext";
import { SelectInput } from "../SelectInput/SelectInput";
import { TaskButton } from "../TaskButton/TaskButton";
import "./FunctionBar.css";
export const FunctionBar = () => {
  const { setShowModal } = useContext(TaskContext);
  return (
    <div className="function-bar-container">
      <TaskButton
        buttonText="Add"
        handleClick={() => {
          setShowModal(true);
          console.log("clicked");
        }}
      />
      <SelectInput />
    </div>
  );
};
