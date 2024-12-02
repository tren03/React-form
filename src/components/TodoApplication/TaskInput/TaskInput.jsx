import React from "react";
import { Input } from "../../InputComponent/Input";
import { TaskButton } from "../TaskButton/TaskButton";
import "./TaskInput.css";

// We need to switch out the login component for the sign in component
export const TaskInput = () => {
  return (
    <div className="taskinput-container">
      <Input
        type="text"
        id="task-deets"
        name="task-deets"
        placeholder="Task Description"
        // value={signinDeets.first_name}
        // onChange={(event) => {
        //   handleChange(event, signinDeets, setSigninDeets);
        // }}
        // hasError={err.first_name ? true : false}
      />
      <TaskButton buttonText="Add" />
    </div>
  );
};
