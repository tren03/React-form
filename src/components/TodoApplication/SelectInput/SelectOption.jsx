import { useContext } from "react";
import { TaskContext } from "../../../context/TaskContext";
import "./SelectOption.css";

export const SelectOption = ({ value }) => {
  const { globalTasks, setTasks } = useContext(TaskContext);

  return (
    <>
      <option value={value}>{value}</option>
    </>
  );
};
