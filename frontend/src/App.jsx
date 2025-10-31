import "./App.css";
import Facilities from "./Facilities";
import Appointments from "./Appointments";
import { AppointmentsProvider } from "./AppointmentsContext";
import Footer from "./Footer";

function App() {
  return (
    <div className="mx-auto w-full">
      <AppointmentsProvider>
        <h1 className="py-4 text-4xl text-center">Facilities</h1>
        <Facilities />
        {/* <h1>My Appointment Dashboard</h1>
      <Appointments /> */}
        <Footer></Footer>
      </AppointmentsProvider>
    </div>
  );
}

export default App;
