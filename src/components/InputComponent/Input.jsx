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
  hasError = false,
  autoComplete = "",
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
        autoComplete={autoComplete}
        className={hasError ? "input-error" : ""}
      />
    </>
  );
};
