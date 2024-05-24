document.getElementById('add-cyclist-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const tipo = document.getElementById('tipo').value;
    const nombre = document.getElementById('nombre').value;
    const edad = document.getElementById('edad').value;
    const nacionalidad = document.getElementById('nacionalidad').value;
    const atributoEspecifico = document.getElementById('atributo-especifico').value;

    const table = document.getElementById('cyclist-table').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    newRow.insertCell(0).innerText = tipo;
    newRow.insertCell(1).innerText = nombre;
    newRow.insertCell(2).innerText = edad;
    newRow.insertCell(3).innerText = nacionalidad;
    newRow.insertCell(4).innerText = atributoEspecifico;

    document.getElementById('add-cyclist-form').reset();
});
