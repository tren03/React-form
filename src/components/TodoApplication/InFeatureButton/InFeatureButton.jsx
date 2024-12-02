import "./InFeatureButton.css";
export const InFeatureButton = ({ action }) => {
  return (
    <div className="in-feature-button-container">
      <button> {action}</button>
    </div>
  );
};
