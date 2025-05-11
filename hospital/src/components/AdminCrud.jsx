import React from 'react'
import { Link } from 'react-router-dom'
import '../styles/sidebar.css'
/*
    Esta es la interfaz en la que se va a visualizar 
    todos los crud cuando el usuario se loguee como admin
*/
function AdminCrud() {
  return (
    <div>
        <div className='sidebar'>
            <h2>Menu de Mantenimientos</h2>
            <ul>
                <li>
                    <Link to="/pacientes">Mantenimiento Pacientes</Link>
                </li>
                <li>
                    <Link to="/user">Mantenimiento Usuarios</Link>
                </li>
                <li>
                    <Link to="/doctores">Mantenimiento Doctores</Link>
                </li>
            </ul>
        </div>
    </div>
  )
}

export default AdminCrud