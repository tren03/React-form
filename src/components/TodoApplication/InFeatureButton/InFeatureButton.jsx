import "./InFeatureButton.css";
export const InFeatureButton = ({ action, image, id }) => {
  return (
    <div className="in-feature-button-container">
      <button onClick={() => console.log(id)}>
        <img src={image} alt={action} /> {/* Display the icon/image */}
      </button>
    </div>
  );
};
