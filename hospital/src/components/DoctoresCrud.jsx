import React, { useState } from 'react'
import PostDoctores from '../services/DoctoresServices'

function DoctoresCrud() {
    const [nombreDoctor, setNombreDoctor] = React.useState("")
    const [apellidoDoctor, setApellidoDoctor] = React.useState("")
    const [anosExperiencia, setAnosExperiencia] = React.useState(0)

    function nombre (evento) {
      setNombreDoctor(evento.target.value)
    }
    function apellido (evento) {
      setApellidoDoctor(evento.target.value)
    }
    function anos (evento) {
      setAnosExperiencia(Number(evento.target.value))
    }
    async function cargarDoctores () {
        //console.log(nombreDoctor, apellidoDoctor, anosExperiencia)
      const obj = { 
        nombre: nombreDoctor,
        apellido: apellidoDoctor,
        anos_experiencia: anosExperiencia
      }
      //console.log(obj)

      const respuestaServer = await PostDoctores(obj)

      console.log(respuestaServer)
    }
  return (
    <div>
        <label htmlFor="">Nombre</label>
        <input value={nombreDoctor} onChange={nombre} type="text"/>
        <br />
        <br />
        <label htmlFor="">Apellido</label>
        <input value={apellidoDoctor} onChange={apellido} type="text"/>
        <br />
        <br />
        <label htmlFor="">Años de experiencia</label>
        <input value={anosExperiencia} onChange={anos} type="number"/>
        <br />
        <br />
        <button onClick={cargarDoctores}>Crear Doctor</button>
    </div>
  )
}

export default DoctoresCrud