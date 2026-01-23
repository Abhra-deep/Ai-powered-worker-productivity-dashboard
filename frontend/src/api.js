import { useEffect, useState } from "react";
import { api } from "./api";

function App() {
  const [workers, setWorkers] = useState({});
  const [factory, setFactory] = useState({});

  useEffect(() => {
    api.get("/metrics/workers").then(res => setWorkers(res.data));
    api.get("/metrics/factory").then(res => setFactory(res.data));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Factory Dashboard</h1>

      <h2>Factory Metrics</h2>
      <pre>{JSON.stringify(factory, null, 2)}</pre>

      <h2>Workers</h2>
      {Object.entries(workers).map(([id, m]) => (
        <div key={id}>
          <b>{id}</b> – Utilization: {m.utilization.toFixed(2)}%
        </div>
      ))}
    </div>
  );
}

export default App;
