import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import styles from "../styles/Home.module.css";

export default function Signup() {
  const [loggedIn, setloggedIn] = useState(false);
  const [user, setUser] = useState();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [showEmailValidation, setShowEmailValidation] = useState(false);
  const [showPasswordValidation, setShowPasswordValidation] = useState(false);
  const [showAlert, setShowAlert] = useState(false);
  const router = useRouter();

  // useEffect(() => {
  //   if (showAlert) {
  //     alert("OK");
  //     setUsername("");
  //     setPassword("");
  //     setEmail("");
  //     setShowAlert(false);
  //     router.push("/user-landing-page");
  //   }
  // }, [showAlert]);

  function handleSubmit(e) {
    console.log("handleSubmit in signup.js");
    e.preventDefault();
    const userinfo = {
      name: username,
      password: password,
      email: email,
    };
    console.log("userinfo: name, password, email is below");
    console.log(userinfo.name, userinfo.password, userinfo.email);

    fetch("http://127.0.0.1:5555/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userinfo),
    })
      .then((r) => r.json())
      .then((user) => {
        console.log(user);
        // TODO: setUser instead of setloggedIn?
        setloggedIn(true);
      })
      .then(() => router.push("/user-landing-page"));
  }
  //   .catch((err) => {
  //     console.log('error caught .catch');
  //     alert("Failed to create account. Please try again later.");
  // });

  function handlePasswordFocus() {
    if (password.length < 2 || !/\d/.test(password)) {
      setShowPasswordValidation(true);
    } else {
      setShowPasswordValidation(false);
    }
  }
  function handleEmail() {
    if (!email.includes('@')) {
      setShowEmailValidation(true);
    } else {
      setShowEmailValidation(false);
    }
  }
  
  return (
    <div className="signup">
      <h1>New User Sign Up</h1>
      <form onSubmit={handleSubmit}>
        <p>Username</p>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <p>Password</p>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          onFocus={handlePasswordFocus}
        />
        {showPasswordValidation && (
          <p style={{ color: "red" }}>
            At least 2 characters long and containing a number.
          </p>
        )}
        <p>Email</p>
        <input
          type="text"
          name='email'
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          onFocus={handleEmail}
        />
        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
}
