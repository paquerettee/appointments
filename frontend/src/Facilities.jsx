import { useState, useEffect } from "react";
import config from "./config";
import axios from "axios";
import Appointments from "./Appointments";
import { useAppointments } from "./AppointmentsContext";
import AppointmentModal from "./AppointmentModal";

function Facilities() {
  const [facilities, setFacilities] = useState([]);

  useEffect(() => {
    axios.get(config.BACKEND_URL + "facilities/").then((response) => {
      console.log(response.data);
      setFacilities(response.data);
    });
  }, []);

  return (
    <>
      <ul className="flex flex-col space-y-4 pt-4 border-t border-gray-300">
        {facilities.map((facility) => (
          <li className="flex-grow border-b border-gray-300" key={facility.id}>
            <Facility facility={facility} />
          </li>
        ))}
      </ul>
    </>
  );
}

function Facility({ facility }) {
  const { addNewAppointment } = useAppointments();
  const [isModalOpen, setIsModalOpen] = useState(false);

  // const makeAppointment = () => {
  //   console.log("Making an appointment: ", facility);
  //   // use react context??
  //   Appointments.addNewAppointment();
  // };

  const makeAppointment = () => {
    // console.log("Making an appointment: ", facility);
    const appointment = {
      facilityId: 10,
      clientId: 21,
      professionalId: 13,
      serviceId: 14,
      date: "2025-11-01T14:30:00",
    };
    console.log("Making an appointment: ", appointment);
    addNewAppointment(appointment);
  };

  return (
    <>
      <div className="flex w-full gap-3 pb-4 ">
        <div className="w-64 shrink-0">
          <div className="w-64 h-40 overflow-hidden rounded-lg">
            <img
              src={facility.main_img}
              className="w-full h-full object-cover"
              style={{ objectPosition: "center 20%" }}
              alt="Preview"
            />
          </div>
        </div>
        <div className="flex-grow">
          <h3 className="text-2xl pb-3">{facility.name}</h3>
          <p>{facility.address}</p>
          <ul className="flex flex-col gap-2 items-start">
            {facility.services.map((service) => (
              <li key={service.id} className="flex w-full items-end">
                <div className="flex-grow truncate">{service.name} </div>
                <div className="mx-4 shrink-0">${service.price}</div>
                <button
                  className="px-3 py-1 bg-blue-500 text-white rounded"
                  onClick={() => setIsModalOpen(true)}
                >
                  Umów
                </button>
              </li>
            ))}
          </ul>
        </div>
      </div>
      <AppointmentModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} />
    </>
  );
}

export default Facilities;
