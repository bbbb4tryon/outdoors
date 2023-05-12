//path: client/pages/user-landing-page.js
import React, { useState, useEffect } from "react";
import styles from "../styles/Home.module.css";
import algorithm from "./api/algorithm.js";


export default function UserLandingPage({ temperature, humidity, windSpeed }) {
  const recommendations = algorithm(temperature, humidity, windSpeed);

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Here are your clothing recommendations:</h1>
      <ul className={styles.list}>
        {recommendations.map((item, index) => (
          <li key={index} className={styles.item}>
            {item}
          </li>
        ))}
      </ul>
    </div>
  );
}