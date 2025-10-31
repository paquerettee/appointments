import { useEffect, useState } from "react";
import config from "./config";
import axios from "axios";

function Appointments() {
  const [appointments, setAppointments] = useState([]);
  const [loading, setLoading] = useState(true);

  // const addNewAppointment = () => {
  //   console.log("Add new appointment");
  // };

  useEffect(() => {
    axios
      .get(config.BACKEND_URL + "appointments/")
      .then((response) => {
        console.log(response.data);
        setAppointments(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching appointments:", error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading appointments...</p>;

  return (
    <div>
      <h2>Appointments</h2>
      <ul>
        {appointments.map((app) => (
          <li key={app.id}>
            <strong>{app.status}</strong> — {new Date(app.date).toLocaleString()}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Appointments;
