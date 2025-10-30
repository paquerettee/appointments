import { useState, useEffect } from "react";
import config from "./config";
import axios from "axios";

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
      <ul className="flex flex-col space-y-4">
        {facilities.map((facility) => (
          <li className="flex-grow" key={facility.id}>
            <Facility facility={facility} />
          </li>
        ))}
      </ul>
    </>
  );
}

function Facility({ facility }) {
  return (
    <div className="flex w-full gap-3 pb-4 border-b border-gray-300">
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
              <button className="px-3 py-1 bg-blue-500 text-white rounded">Umów</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Facilities;
