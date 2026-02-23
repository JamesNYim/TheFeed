import React from "react";
import { useAuth } from "../auth/AuthContext";

export default function Home() {
  const { user, logout } = useAuth();

  return (
    <div style={{ maxWidth: 600, margin: "40px auto" }}>
      <h2>Home</h2>
      <p>You are logged in as: <b>{user?.username}</b></p>
      <button onClick={logout}>Logout</button>
    </div>
  );
}
