import React, { useState } from 'react'
import PostUsers from '../services/UsersServices'

function UserCrud() {
    const [nombreUser, setNombreUser] = React.useState("")
    const [PrimerNombreUser, setPrimerNombreUser] = React.useState("")
    const [apellidoUser, setApellidoUser] = React.useState("")
    const [correoUser, setCorreoUser] = React.useState("")
    const [contrasenaUser, setContrasenaUser] = React.useState("")

    function nombre (evento) {
      setNombreUser(evento.target.value)
    }
    function PrimerNombre (evento) {
      setPrimerNombreUser(evento.target.value)
    }
    function apellido (evento) {
      setApellidoUser(evento.target.value)
    }
    function correo (evento) {
      setCorreoUser(evento.target.value)
    }
    function contrasena (evento) {
      setContrasenaUser(evento.target.value)
    }
    async function cargarUsers () {
      const obj = { 
        username: nombreUser,
        first_name: PrimerNombreUser,
        last_name: apellidoUser,
        email: correoUser,
        password: contrasenaUser
      }
      

      const respuestaServer = await PostUsers(obj)

      console.log(respuestaServer)
    }
  return (
    <div>
        <label htmlFor="">Nombre</label>
        <input value={nombreUser} onChange={nombre} type="text"/>
        <br />
        <br />
        <label htmlFor="">Primer Nombre</label>
        <input value={PrimerNombreUser} onChange={PrimerNombre} type="text"/>
        <br />
        <br />
        <label htmlFor="">Apellido</label>
        <input value={apellidoUser} onChange={apellido} type="text"/>
        <br />
        <br />
        <label htmlFor="">Correo</label>
        <input value={correoUser} onChange={correo} type="email"/>
        <br />
        <br />
        <label htmlFor="">Contraseña</label>
        <input value={contrasenaUser} onChange={contrasena} type="password"/>
        <br />
        <br />
        <button onClick={cargarUsers}>Crear Usuario</button>
    </div>
  )
}

export default UserCrud