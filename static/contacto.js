document.addEventListener('DOMContentLoaded', function () {
    isValid = true;
    const formulario = document.getElementById('formulario');
    formulario.addEventListener('submit', function (e) {
        e.preventDefault()
        isValid = true;
        validarNombre();
        validarEmail();
        validarConsulta();
        validarTerminos();


        if (isValid) {
            exito();
        }
    })

    // validar nombre

    let nombreIngresado = document.getElementById('nombre');
    nombreIngresado.addEventListener('blur', validarNombre);
    nombreIngresado.addEventListener('input', validarNombre);

    function validarNombre() {
        let nombre = nombreIngresado.value.trim();
        let error = document.getElementById('nombre-error');
        let regex = /^[a-zA-ZÁÉÍÓÚÑáéíóúñ\s]+$/;

        if (nombre === '') {
            error.textContent = 'Debe completar este campo';
            error.style.color = 'red';
            error.style.display = 'block'
            isValid = false;
        } else if (!regex.test(nombre) || nombre.length < 2) {
            error.textContent = 'Debe ingresar un nombre valido';
            error.style.color = 'red';
            error.style.display = 'block'
            isValid = false;
        } else {
            error.textContent = '';

        }
    }

    // validar email

    let emailIngresado = document.getElementById('email');
    emailIngresado.addEventListener('blur', validarEmail);

    function validarEmail() {
        let email = emailIngresado.value.trim();
        let error = document.getElementById('email-error');
        let regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

        if (email === '') {
            error.textContent = 'este campo es obligatorio';
            error.style.display = 'block';
            error.style.color = 'red';
            isValid = false;
        } else if (email.length < 5 || !regex.test(email)) {
            error.textContent = 'Debe ingresar un email valido';
            error.style.display = 'block';
            error.style.color - 'red';
            isValid = false;
        } else {
            error.textContent = ''
        }
    }

    //validar consulta

    let consultaIngresada = document.getElementById('consulta');
    consultaIngresada.addEventListener('blur', validarConsulta);
    consultaIngresada.addEventListener('input', validarConsulta);

    function validarConsulta() {
        let consulta = consultaIngresada.value.trim();
        let error = document.getElementById('consulta-error');
        let caracteres = document.getElementById('caracteres');
        let caracteresRestantes = 100 - consulta.length;


        caracteres.textContent = `Caracteres usados: ${consulta.length} - Caracteres restantes: ${caracteresRestantes}`
        caracteres.style.color = 'blue';
        if (consulta === '') {
            error.textContent = 'debe completar este campo';
            error.style.color = 'red';
            error.style.display = 'block';
            isValid = false;
        } else if (consulta.length > 100) {
            error.textContent = 'Alcanzaste el limite maximo de 10 caracteres';
            error.style.color = 'red';
            error.style.display = 'block';
            isValid = false;
        }
    }

    // validar los terminos

    let terminos = document.getElementById('terminos');
    terminos.addEventListener('blur', validarTerminos);
    terminos.addEventListener('change', validarTerminos);

    function validarTerminos() {
        let error = document.getElementById('terminos-error');

        if (!terminos.checked) {
            error.textContent = 'Debe aceptar para poder continuar';
            error.style.color = 'red';
            error.style.display = 'block'
            isValid = false;
        } else {
            error.textContent = '';
        }
    }
})

    