import React from "react";
import { Routes, Route } from "react-router-dom";
import Login from "./Login";
import Profile from "./Profile";

function AccountsRoutes() {
  return (
    <>
      <Routes>
        <Route path="/profile" element={<Profile />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </>
  );
}

export default AccountsRoutes;