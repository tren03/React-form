import { useContext } from "react";
import { TaskContext } from "../../../context/TaskContext";
import "./SelectInput.css";
import { SelectOption } from "./SelectOption";
export const SelectInput = ({ optionList, handleChange }) => {
  // the options are the categories, from globalTasks, get all uniqe categories and display them
  const { categories } = useContext(TaskContext);
  if (!optionList) {
    optionList = categories;
  }

  return (
    <div className="select-container">
      <select className="select-button" onChange={handleChange}>
        {optionList.map((item, index) => {
          return <SelectOption key={index} value={item} />;
        })}
      </select>
    </div>
  );
};
