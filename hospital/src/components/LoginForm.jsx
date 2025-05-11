import React from 'react'

function loginForm() {
  return (
    <div>
        <label htmlFor="">Username</label>
        <input type="text"/>
        <label htmlFor="">Password</label>
        <input type="password"/>

        <button>Iniciar Sesion</button>
    </div>
  )
}

export default loginForm