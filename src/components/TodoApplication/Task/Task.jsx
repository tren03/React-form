import React from "react";
import { InFeatureButton } from "../InFeatureButton/InFeatureButton";
import { TaskInfo } from "../TaskInfo/TaskInfo";
import "./Task.css";

// We need to switch out the login component for the sign in component
export const Task = ({ id, title, description, category }) => {
  return (
    <div className="task-shell">
      <TaskInfo title={title} category={category} description={description} />
      <div className="feature-buttons">
        <InFeatureButton action="update" image="/editicon.svg" id={id} />
        <InFeatureButton action="delete" image="/deleteIcon.svg" id={id} />
      </div>
    </div>
  );
};
