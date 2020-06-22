import bobo, os

@bobo.query('/')
def hello():
    return "Hello world from Bobo!!!!"

"""@bobo.query('/form')
def form():
    return """

@bobo.query('/form')
def html():
    return """
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>FORMULARIO</title>
    <style type="text/css">
            html{
        font-size: larger;
        letter-spacing: 1px;
        background-color: lightcoral;
        }
        body{
        background-color: lightcoral;
        }
        center{
            background-color: lightcoral;
        }
        h1{
        color: darkslategray;
        }
        p{
            font-family: 'Dosis', sans-serif;
            border: sandybrown;
        }
        number{
            font-family: 'Dosis', sans-serif;
            font-style: oblique;
        }
    </style>
    <!-- CSS only -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  <link href="https://fonts.googleapis.com/css2?family=Dosis&display=swap" rel="stylesheet">

  <!-- JS, Popper.js, and jQuery -->
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </head>
  <body>
<center>
  <div class="formulario">
  <h1>FORMULARIO</h1>
  <link rel="stylesheet" href="estilos.css">
  <form>
      <p>Matricula: <input placeholder="Escriba su matricula" type="text" name="matricula" size="40"></p>
      <p>Nombre: <input placeholder="Escribe tu nombre(s)" type="text" name="nombre" size="40"></p>
      <p>Primer apellido: <input placeholder="Escribe tu primer apellido" type="text" name="primer_apellido" size="40"></p>
      <p>Segundo apellido: <input placeholder="Escribe tu segundo apellido" type="text" name="segundo_apellido" size="40"></p>
      <p>Edad: <input placeholder="Escribe tu edad" type="number" name="edad" size="40"></p>
      <p>Fecha de nacimiento: <input type="date" name="nacimiento" min="1900"></p>
      <p>Sexo:
        <input type="radio" name="hm" value="h"> Hombre
        <input type="radio" name="hm" value="m"> Mujer
      </p>
      <p>Estado:
        <select name="estado">
          <option value="0">Selecciona</option>
          <option value="1">Aguascalientes</option>
          <option value="2">Baja California</option>
          <option value="3">Baja California Sur</option>
          <option value="4">Campeche</option>
          <option value="5">Chiapas</option>
          <option value="6">Chihuahua</option>
          <option value="7">Coahuila de Zaragoza</option>
          <option value="8">Colima</option>
          <option value="9">Durango</option>
          <option value="10">Estado de México</option>
          <option value="11">Guanajuato</option>
          <option value="12">Guerrero</option>
          <option value="13">Hidalgo</option>
          <option value="14">Jalisco</option>
          <option value="15">Michoacán de Ocampo</option>
          <option value="16">Morelos</option>
          <option value="17">Nayarit</option>
          <option value="18">Nuevo León</option>
          <option value="19">Oaxaca</option>
          <option value="20">Puebla</option>
          <option value="21">Querétaro</option>
          <option value="22">Quintana Roo</option>
          <option value="23">San Luis Potosí</option>
          <option value="24">Sinaloa</option>
          <option value="25">Sonora</option>
          <option value="26">Tabasco</option>
          <option value="27">Tamaulipas</option>
          <option value="28">Tlaxcala</option>
          <option value="29">Veracruz de Ignacio de la Llave</option>
          <option value="30">Yucatán</option>
          <option value="31">Zacatecas</option>
        </select>
      </p>
      <p>
        <input type="reset" value="Borrar">
        <input type="submit" value="Guardar">
      </p>
    </form>
  </center>
  </body>
</html>

    """ 
