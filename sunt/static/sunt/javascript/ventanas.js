document.getElementById("crearCuenta").onclick = function () {
  var enc = confirm("Desea responder una encuesta");
  if (enc == true) {
    location.href = "https://forms.gle/NBAWkTsXLnbQurJg7";
  } else {
    alert("Se ha registrado correctamente");
  }
};
