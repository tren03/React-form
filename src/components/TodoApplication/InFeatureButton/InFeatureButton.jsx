import "./InFeatureButton.css";
export const InFeatureButton = ({ action, image }) => {
  return (
    <div className="in-feature-button-container">
      <button>
        <img src={image} alt={action} /> {/* Display the icon/image */}
      </button>
    </div>
  );
};
