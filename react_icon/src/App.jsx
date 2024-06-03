import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import { FaCarBattery } from "react-icons/fa6";
function App() {
  return (
    <>
      <div>
        <FaCarBattery size={"18px"} color="rgb(223, 252, 3)"></FaCarBattery>
        <FaCarBattery size={"36px"} color="rgb(223, 252, 3)"></FaCarBattery>
        <FaCarBattery size={"72px"} color="rgb(223, 252, 3)"></FaCarBattery>
      </div>
    </>
  );
}

export default App;
