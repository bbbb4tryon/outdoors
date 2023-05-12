import { useState,useEffect } from "react";
import axios from "axios";
import styles from "../styles/Home.module.css";

export default function UserLog() {
  console.log("UserLog function in client/pages/userlog.js");
  const [emotionalGauge, setEmotionalGauge] = useState("");
  const [relaxationGauge, setRelaxationGauge] = useState("");
  const [userLogs, setUserLogs] = useState([]);
  console.log("userLogs is below");
  console.log(userLogs);
  console.log("emotionalGauge, relaxationGauge is below");
  console.log(emotionalGauge, relaxationGauge);

  useEffect(() => {
    console.log("line 166666")
    fetch("/userlog")
      .then(r => r.json())
      .then((res) => {
        console.log("line 18", res);
        setUserLogs(res.user_logs);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);


const handleSubmit = async (e) => {
  console.log("handleSubmit in client/pages/userlog.js");
  console.log("e is below");
  console.log(e);
  e.preventDefault();
  // try {
  //   const res = await axios.post("/userlog", {
  //     emotional_gauge: emotionalGauge,
  //     relaxation_gauge: relaxationGauge,
  //   });
  //   console.log("res is below");
  //   console.log(res);
  //   console.log("res.data is below");
  //   console.log(res.data);
  //   setUserLogs([...userLogs, res.data]);
  //   setEmotionalGauge("happy");
  //   setRelaxationGauge("satisfied");
  // } catch (error) {
  //   console.error(error);
  // }
};
  // const UserLog = ({ userLogs, handleSubmit, emotionalGauge, setEmotionalGauge, relaxationGauge, setRelaxationGauge }) => {

    return (
      <div className={styles.container}>
        <h1 className={styles.title}>User Logs</h1>
        <form onSubmit={handleSubmit}>
          <label className={styles.label}>
            <span className={styles.gaugeLabel}>Emotional Gauge:</span>
            <select
              name="emotionalGauge"
              value={emotionalGauge}
              onChange={(e) => setEmotionalGauge(e.target.value)}
              className={styles.select}
            >
              <option value="overjoyed">Overjoyed</option>
              <option value="happy">Happy</option>
              <option value="level">Level</option>
              <option value="melancholy">Melancholy</option>
              <option value="depressed">Depressed</option>
            </select>
          </label>
          <label className={styles.label}>
            <span className={styles.gaugeLabel}>Relaxation Gauge:</span>
            <select
              name="relaxationGauge"
              value={relaxationGauge}
              onChange={(e) => setRelaxationGauge(e.target.value)}
              className={styles.select}
            >
              <option value="wholly relaxed">Wholly Relaxed</option>
              <option value="satisfied">Satisfied</option>
              <option value="meh">Meh</option>
              <option value="anxious">Anxious</option>
              <option value="agitated">Agitated</option>
            </select>
          </label>
          <button type="submit" className={styles.button}>Submit</button>
        </form>

        <table className={styles.table}>
          <thead>
            <tr>
              <th>ID</th>
              <th>Emotional Gauge</th>
              <th>Relaxation Gauge</th>
              <th>Created At</th>
            </tr>
          </thead>
          <tbody>
            {userLogs.map((log) => (
              <tr key={log.id}>
                <td>{log.id}</td>
                <td>{log.emotional_gauge}</td>
                <td>{log.relaxation_gauge}</td>
                <td>{new Date(log.created_at).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }

