import "./App.css";
import Facilities from "./Facilities";
import Appointments from "./Appointments";
import Footer from "./Footer";

function App() {
  return (
    <div>
      <h1>Facilities</h1>
      <Facilities />
      {/* <h1>My Appointment Dashboard</h1>
      <Appointments /> */}
      <Footer></Footer>
    </div>
  );
}

export default App;
