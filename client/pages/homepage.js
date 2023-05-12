import { useState } from "react";
import { useRouter } from "next/router";
import styles from "../styles/Home.module.css";

export default function HomePage() {
  const router = useRouter();

    const handleUserLandingPageClick = () => {
      router.push("/user-landing-page");
    };

  const handleDestinationClick = () => {
    router.push("/destination");
  };

  // const handleBaseLayer = () => {
  //   router.push("/baselayer");
  // };

  const handleRecommendationsClick = () => {
    router.push("/recommendations");
  };

  const handleUserLogClick = () => {
    router.push("/userlog");
  };

  return (
    <div>
      <h1 className={styles.title}>Enter the Outdoors!</h1>

      <p className={styles.description}>
        Get started by clicking an option below
        {/* <code>pages/index.js</code> */}
      </p>

      <div className={styles.grid}>
              <div className={styles.card} onClick={handleUserLandingPageClick}>
          <h3>Go to personal homepage &rarr;</h3>
          <p>Find your profile and data there.</p>
        </div>

        <div className={styles.card} onClick={handleDestinationClick}>
          <h3>Destination &rarr;</h3>
          <p>Find the weather at your destination.</p>
        </div>

        {/* <div className={styles.card} onClick={handleBaseLayer}>
          <h3>Baselayer &rarr;</h3>
          <p>Learn what to wear when you start!</p>
        </div> */}

        <div className={styles.card} onClick={handleRecommendationsClick}>
          <h3>Recommendations &rarr;</h3>
          <p>What should you be wearing at the end of your adventure?</p>
        </div>

        <div className={styles.card} onClick={handleUserLogClick}>
          <h3>UserLog &rarr;</h3>
          <p>In here, enter your data to track your progress!</p>
        </div>
      </div>

      <div
        style={{
          display: "flex",
          justifyContent: "center",
          marginTop: "2rem",
        }}
      >
        <button
          variant="primary"
          type="submit"
          className="mb-3"
          style={{
            padding: "0.5rem 1rem",
            backgroundColor: "#0d6efd",
            fontFamily:
              "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Fira Sans,Droid Sans,Helvetica Neue,sans-serif",
            color: "white",
            fontWeight: "bold",
            borderRadius: "0.25rem",
            marginRight: "1rem",
          }} onClick={() => router.push("/logout")}>
          Get outta here
        </button>

        <button className={styles.link} onClick={() => router.push("/signup")}>
          Never been here before?
        </button>
      </div>
    </div>
  );
}
