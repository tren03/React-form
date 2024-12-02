import React from "react";
import { InFeatureButton } from "../InFeatureButton/InFeatureButton";
import { TaskInfo } from "../TaskInfo/TaskInfo";
import "./Task.css";

// We need to switch out the login component for the sign in component
export const Task = ({ title, description, category }) => {
  return (
    <div className="task-shell">
      <TaskInfo title={title} category={category} description={description} />
      <div className="feature-buttons">
        <InFeatureButton action="update" image="/editicon.svg" />
        <InFeatureButton action="delete" image="/deleteIcon.svg" />{" "}
      </div>
    </div>
  );
};
