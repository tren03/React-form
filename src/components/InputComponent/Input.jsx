import React from "react";
import "./Input.css";

export const Input = ({
  type = "text",
  id,
  name,
  placeholder = "",
  value,
  onChange,
  required = false,
}) => {
  return (
    <>
      <input
        type={type}
        id={id}
        name={name}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        required={required}
      />
    </>
  );
};
