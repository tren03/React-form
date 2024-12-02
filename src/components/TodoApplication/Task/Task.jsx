import React from "react";
import { InFeatureButton } from "../InFeatureButton/InFeatureButton";
import { TaskButton } from "../TaskButton/TaskButton";
import { TaskInfo } from "../TaskInfo/TaskInfo";
import "./Task.css";

// We need to switch out the login component for the sign in component
export const Task = () => {
  return (
    <div className="task-shell">
      <TaskInfo title="sample" description="This is a very important task" />
      <InFeatureButton action="update" />
      <InFeatureButton action="delete" />
    </div>
  );
};
