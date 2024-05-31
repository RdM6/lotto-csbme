import React, { } from "react";
import './App.css';

import {BrowserRouter, Routes, Route, Link} from "react-router-dom";

import MainPage from "./pages/MainPage";
import LoginPage from "./pages/LoginPage"
import RegisterPage from "./pages/RegisterPage"
import GamePage from "./pages/GamePage"

function App() {
  return (
    <div className="vh-100 gradient-custom">
    <div className="container">
      <h1 className="page-header text-center">Lotto</h1>

      <BrowserRouter>
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/game" element={<GamePage />} />
        </Routes>
      </BrowserRouter>
    </div>
    </div>
  );
}

export default App;
