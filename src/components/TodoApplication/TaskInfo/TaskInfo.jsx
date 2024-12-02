import "./TaskInfo.css";
export const TaskInfo = ({ title, description }) => {
  return (
    <div className="task-info-container">
      <h3> {title} </h3>
      <p> {description} </p>
    </div>
  );
};
