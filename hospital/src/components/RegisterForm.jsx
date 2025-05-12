import React from 'react'

function RegisterForm() {
  return (
    <div>
        <label htmlFor="">Username</label>
        <input type="text"/>
        <label htmlFor="">Nombre</label>
        <input type="text"/>
        <label htmlFor="">Apellido</label>
        <input type="text"/>
        <label htmlFor="">Email</label>
        <input type="email"/>
        <label htmlFor="">Password</label>
        <input type="password"/>

        <button>Registrarse</button>
    </div>
  )
}

export default RegisterForm