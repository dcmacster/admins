
    function loadProd() {

        var str;
        str = document.getElementById("codigo").value
        console.log(str)
        if (str.length == 0) {
            document.getElementById("my_registro").innerHTML = "";
            return;
        } else {
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    var myObj = JSON.parse(this.responseText);
                    document.getElementById("my_registro").innerHTML = "<tr><td>" + myObj.codigob + "</td><td>" + myObj.nombre + "</td> <td>" + myObj.descripcion + "</td><td>" + myObj.cantidad + "</td></tr>";
                }
            };
            xmlhttp.open("GET", "{% url 'buscar' %}?codigo=" + str, true);
            xmlhttp.send();
        }
    } 
