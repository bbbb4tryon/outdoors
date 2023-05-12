import { useState } from "react";
import Signup from "./signup";
import HomeGrid from "./homepage";

export default function Index() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [loggedIn, setLoggedIn] = useState(false);
  const [user, setUser] = useState(null);

  const createUser = async () => {
    try {
      const response = await fetch("/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password }),
      });
      const data = await response.json();
      if (response.status === 200) {
        setLoggedIn(true);
        setUser(data);
      } else {
        setErrorMessage(data.error);
      }
    } catch (error) {
      console.error(error);
      setErrorMessage("Something went wrong: index.js");
    }
  };
// #reroute to signup page
  const login = async () => {
    try {
      const response = await fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, password }),
      });
      const data = await response.json();
      if (response.status === 200) {
        setLoggedIn(true);
        setUser(data);
      } else {
        setErrorMessage("Invalid login");
      }
    } catch (error) {
      console.error(error);
      setErrorMessage("Something went wrong:login index"  );
    }
  };

  const checkLogin = async () => {
    try {
      const response = await fetch("/checklogin");
      const data = await response.json();
      if (response.status === 200) {
        setLoggedIn(true);
        setUser(data);
      }
    } catch (error) {
      console.error(error);
    }
  };

  const logout = async () => {
    try {
      await fetch("/logout", { method: "DELETE" });
      setLoggedIn(false);
      setUser(null);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
 
      
      {/* <Signup /> */}
      <HomeGrid />
    </div>
  );
}
     