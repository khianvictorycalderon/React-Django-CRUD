// All components in this file, this is just a test project btw

import { forwardRef, useRef, type HTMLInputTypeAttribute } from "react";

interface InputProps {
  type?: HTMLInputTypeAttribute;
  label?: string;
  id: string;
  placeholder?: string;
  className?: string;
}

const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ type = "text", label, id, placeholder, className = "", ...props }, ref) => {
    return (
      <div className="relative w-full">
        <input
          type={type}
          id={id}
          ref={ref}
          placeholder={placeholder || label}
          {...props}
          className={`peer w-full p-4 pt-6 rounded-md bg-white ring-1 ring-gray-300 focus:ring-2 focus:ring-blue-500 outline-none transition duration-200 placeholder-transparent ${className}`}
        />
        {label && (
          <label
            htmlFor={id}
            className="absolute left-4 top-2 text-gray-400 text-sm transition-all duration-200 pointer-events-none
                       peer-placeholder-shown:top-4 peer-placeholder-shown:text-gray-400 peer-placeholder-shown:text-base
                       peer-focus:left-2 peer-focus:top-1.5 peer-focus:text-blue-500 peer-focus:text-sm"
          >
            {label}
          </label>
        )}
      </div>
    );
  }
);

export default function App() {

  const first_name = useRef<HTMLInputElement>(null);
  const last_name = useRef<HTMLInputElement>(null);
  const age = useRef<HTMLInputElement>(null);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 py-32">
      
      <div>
        <h2 className="text-4xl font-semibold">React + Django CRUD</h2>
        <hr className="my-4" />

        <h2 className="font-semibold text-2xl text-center">Add Item</h2>
        
          <form className="flex flex-col gap-2 mt-4">

            <Input 
              type="text"
              label="First Name"
              id="first-name-add-input"
            />

            <Input 
              type="text"
              label="Last Name"
              id="last-name-add-input"
            />

            <Input 
              type="number"
              label="Age"
              id="last-name-add-input"
            />

          </form>

        </div>

    </div>
  );
}