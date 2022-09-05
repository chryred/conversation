import React from "react";
import { Routes, Route } from "react-router-dom";
import AppLayout from "components/layout/AppLayout";
import About from "./About";
import Home from "./Home";
import AccountsRoutes from "./accounts";

function Root() {
  return (
    <AppLayout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/accounts/*" element={<AccountsRoutes />} />
      </Routes>
    </AppLayout>
  );
}

export default Root;
