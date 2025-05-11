import React from 'react'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Administrador from '../pages/Administrador';
import PacientesCrudPage from '../pages/PacientesCrudPage';
import UserCrudPage from '../pages/UserCrudPage';
import Login from '../pages/Login';
import Register from '../pages/Register';
import DoctoresCrudPage from '../pages/DoctoresCrudPage';

function Routing() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login/>} />
        <Route path="/register" element={<Register/>} />
        <Route path="/admin" element={<Administrador/>} />
        <Route path="/pacientes" element={<PacientesCrudPage/>} />
        <Route path="/doctores" element={<DoctoresCrudPage/>} />
        <Route path="/user" element={<UserCrudPage/>} />
      </Routes>
    </Router>
  )
}

export default Routing