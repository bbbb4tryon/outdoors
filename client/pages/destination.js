import { useState, useEffect } from "react";
import styles from "../styles/Home.module.css";
import destStyles from "../styles/Dest.module.css";
import weather_conditions from "../public/weather_conditions.json";

export default function Destination() {
  const [location, setLocation] = useState("");
  const [feelsLike, setFeelsLike] = useState("");
  const [wind, setWind] = useState("");
  const [precipitation, setPrecipitation] = useState("");
  const [uvIndex, setUvIndex] = useState("");
  const [description, setDescription] = useState("");
  const [conditionCode, setConditionCode] = useState(0);
  // const [icon, setIcon] = useState("");

  // useEffect(() => {
    const fetchWeather = async () => {
      console.log("weather options fetchWeather");
      const lat = 53.1;
      const lon = -0.13;
      const url = `https://weatherapi-com.p.rapidapi.com/current.json?q=${lat}%2C${lon}`;
      const options = {
        method: "GET",
        headers: {
          "X-RapidAPI-Key":
          "7552fd5765msh9937588766fc23fp156f53jsn0132a88afefe",
          "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
        },
      };
      console.log(options);
      
      try {
        const response = await fetch(url, options);
        console.log("is the weather response below?");
        console.log(response);
        const data = await response.json();
        console.log("is the weather data below?");
        console.log(data);
        setLocation(data.location.name);
        console.log("is weather log and lat below:", location);
        console.log("weather location:", data.location.name);
        setFeelsLike(data.current.temp_f);
        console.log('is weather temp below:', feelsLike)
        console.log("weather temp:", data.current.temp_f);
        setDescription(data.current.condition.text);
        console.log('is weather description below:', description)
        console.log("weather description:", data.current.condition.text);
        setConditionCode(data.current.condition.code);
        console.log('is weather condition code below:', conditionCode)
        console.log("weather condition code:", data.current.condition.code);
        setWind(data.current.wind_mph);
        console.log('is weather wind below:', wind)
        console.log("weather wind:", data.current.wind_mph);
        setPrecipitation(data.current.precip_in);
        console.log('is weather precipitation below:', precipitation)
        console.log("weather precipitation:", data.current.precip_in);
        setUvIndex(data.current.uv);
        console.log('is weather uv index below:', uvIndex)
        console.log("weather uv index:", data.current.uv);
        
        // setIcon(data.current.condition.icon);
      } catch (error) {
        console.error("weather error");
      }
    };
    
  useEffect(() => {
    fetchWeather();
    console.log("weather options fetchWeather");
  }, []);

const condition = weather_conditions.find(
  (condition) => condition.code === conditionCode
);


  
  const handleWeatherCardClick = () => {
    fetchWeather(conditionCode)
  };

  return (
    <div>
      <h1 className={styles.title}>Enter the Outdoors!</h1>
      <p className={styles.description}>
        Click below to find the weather at your destination.
      </p>
      <div
        className={`${destStyles.card} ${destStyles.destCard}`}
        onClick={handleWeatherCardClick}
      >
        <h3>Temperature</h3>
        <p>What're you fareinhe-its?</p>
        <br></br>
        <h3>Location</h3>
        <p>What're you're digits're?</p>
        <br></br>
        <h3>Forecast</h3>
        <p>What're you expecting?</p>
        <br></br>
        <h3>Wind Chill</h3>
        <p>What're you speed?</p>
        <br></br>
        <h3>Precipitation</h3>
        <p>What're you percenting?</p>
        <br></br>
        <h3>UV Index</h3>
        <p>What're you burning?</p>
        <br></br>
      </div>
    </div>
  );
}