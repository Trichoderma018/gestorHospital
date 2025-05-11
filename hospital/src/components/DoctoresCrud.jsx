import React from 'react'

function DoctoresCrud() {
    const [nombreDoctor, setNombreDoctor] = React.useState("")
    const [apellidoDoctor, setApellidoDoctor] = React.useState("")
    const [anosExperiencia, setAnosExperiencia] = React.useState(0)

    function nombre (evento) {
        
    }
    function apellido (evento) {
        
    }
    function anos (evento) {
        
    }
    function cargarDoctores (evento) {
        
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
        <button value={cargarDoctores}>Crear Doctor</button>
    </div>
  )
}

export default DoctoresCrud