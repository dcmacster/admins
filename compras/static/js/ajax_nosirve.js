$(document).ready(function(){
        
     $("#entrada-form").submit(function(e){
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'), 
            type: $(this).attr('method'),
            data: $(this).serialize(),
            //success: function (response) {
            success: function (response) {
                //console.log(json)
                // on successfull creating object
                // 1. clear the form.
                $("#entrada-form").trigger('reset');
                // 2. focus to nickname input 
                $("#codigo").focus();

                // display the newly friend to table.
                //var instance = JSON.parse(json);
               
               var instance = JSON.parse(response.instance);
               
               // var fields = instance[0]["fields"];
                $("#my_registro").remove();
                /*$("#my_entrada tbody").prepend(
                    `<tr>
                    <td>${fields["codigob"] || ""}</td>
                    <td>${fields["nombre"] || ""}</td>
                    <td>${fields["descripcion"] || ""}</td>
                    <td>${fields["cantidad"] || ""}</td>
                    
                    </tr>`
                )*/


                var codigob = instance.codigob;
                var nombre = instance.nombre;
                var descripcion = instance.descripcion;
                var cantidad = instance.cantidad;
                $("#my_entrada tbody").prepend(
                    `<tr>
                    <td>${codigob || ""}</td>
                    <td>${nombre || ""}</td>
                    <td>${descripcion || ""}</td>
                    <td>${cantidad || ""}</td>
                    
                    </tr>`
                )

            }
           /* error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }*/
        })

    })

})


