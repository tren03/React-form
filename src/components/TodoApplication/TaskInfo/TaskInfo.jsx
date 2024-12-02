import "./TaskInfo.css";
export const TaskInfo = ({ title, description, category }) => {
  return (
    <div className="task-info-container">
      <h3>
        {" "}
        {title} : {category}{" "}
      </h3>
      <p> {description} </p>
    </div>
  );
};
