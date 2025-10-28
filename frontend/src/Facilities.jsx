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
      <ul>
        {facilities.map((facility) => (
          <li key={facility.id}>
            {" "}
            <h3>{facility.name}</h3>
            <p>{facility.address}</p>
            <ul>
              {facility.services.map((service) => (
                <li key={service.id}>
                  {service.name} – ${service.price}
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </>
  );
}

export default Facilities;
