import { Route, Routes } from "react-router-dom";
import Glavna from "./Komponente/Glavna"
import Logovani from "./Komponente/Logovani"
import Login from "./Komponente/Login"
import Register from "./Komponente/Register"


function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Glavna />} />
        <Route path="/logovani" element={<Logovani />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />        
      </Routes>
    </div>
  );
}

export default App;