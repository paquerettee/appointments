import { createContext, useContext, useState } from "react";
import config from "./config";
import axios from "axios";

const AppointmentsContext = createContext();
export const useAppointments = () => useContext(AppointmentsContext);

export const AppointmentsProvider = ({ children }) => {
  const [appointments, setAppointments] = useState([]);

  // const addNewAppointment = (facility) => {
  //   console.log("appointmentProvider, addNewAppointment");
  //   setAppointments((prev) => [...prev, { facility, date: new Date() }]);
  // };

  const addNewAppointment = async ({ facilityId, clientId, professionalId, serviceId, date }) => {
    const appointment = {
      facility: facilityId,
      client: clientId,
      professional: professionalId,
      service: serviceId,
      date,
      status: "scheduled",
    };

    console.log("provider, addNewAppointment: ", appointment);

    try {
      const response = await axios.post(config.BACKEND_URL + "appointments/", appointment, {
        headers: {
          "Content-Type": "application/json",
        },
      });

      const savedAppointment = response.data;
      setAppointments((prev) => [...prev, savedAppointment]);
    } catch (error) {
      console.error("Failed to save appointment:", error);
    }
  };

  return (
    <AppointmentsContext.Provider value={{ appointments, addNewAppointment }}>
      {children}
    </AppointmentsContext.Provider>
  );
};
