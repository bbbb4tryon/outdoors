// PATH: client/pages/index.js

// import Head from "next/head";
import Image from "next/image";
import { Inter } from "next/font/google";
import styles from "../styles/Home.module.css";

import { useState } from "react";

const inter = Inter({ subsets: ["latin"] });

const Index = () => {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch("/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      const responseData = await response.json();
      console.log(responseData);
      // Redirect to the user home page after successful login
      // For example: router.push("/userhome");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
      {/* <Head>
        <title>My App - Login</title>
        <link rel="icon" href="/favicon.ico" />
      </Head> */}

      <main className={styles.main}>
        <h1 className={styles.title}>Login</h1>
        <form className={styles.form} onSubmit={handleFormSubmit}>
          <label className={styles.label}>
            Username:
            <input
              className={styles.input}
              type="text"
              name="username"
              value={formData.username}
              onChange={handleInputChange}
              required
            />
          </label>
          <label className={styles.label}>
            Password:
            <input
              className={styles.input}
              type="password"
              name="password"
              value={formData.password}
              onChange={handleInputChange}
              required
            />
          </label>
          <button className={styles.button} type="submit">
            Submit
          </button>
        </form>
      </main>
    </>
  );
};

export default Index;
// we use the useState hook to initialize the formData object with username and password properties. We also add an onChange event handler to the input fields to update the formData state when the user types in the input fields.

// We modify the handleSubmit function to use the /api/login endpoint instead of /submit, which is more descriptive of its purpose. We also add a console.log statement to log the response data to the console.

// Finally, we add a handleFormSubmit function to handle the form submission event. This function sends a POST request to the /api/login endpoint with the formData object in the request body. On successful login, you can use Next.js router to redirect the user to the desired page.