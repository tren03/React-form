import { Input } from "../../InputComponent/Input";
import { SelectInput } from "../SelectInput/SelectInput";
import { TaskButton } from "../TaskButton/TaskButton";
import "./FunctionBar.css";
export const FunctionBar = () => {
  return (
    <div className="function-bar-container">
      <TaskButton buttonText="Add" />
      <SelectInput />
    </div>
  );
};
