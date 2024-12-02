import { Input } from "../../InputComponent/Input";
import "./ModalField.css";
export const ModalField = ({
  type,
  id,
  name,
  placeholder,
  value,
  hasError,
  localModalDeets,
  setlocalModalDeets,
}) => {
  function handleChange(event, localModalDeets, setlocalModalDeets) {
    let field = event.target.id;
    let value = event.target.value;
    let copyLog = { ...localModalDeets };
    copyLog[field] = value;
    setlocalModalDeets(copyLog);
    event.target.setCustomValidity("");
  }
  return (
    <div className="modal-field-container">
      <label htmlFor={id}>{placeholder}</label>
      <Input
        type={type}
        id={id}
        name={name}
        placeholder={placeholder}
        value={value}
        onChange={(event) =>
          handleChange(event, localModalDeets, setlocalModalDeets)
        }
        hasError={hasError ? true : false}
      />
    </div>
  );
};
