$(document).ready(function(){
        
     $("#entrada-form").submit(function(e){
        e.preventDefault();

        $.ajax({
            url: $(this).attr('action'), 
            type: $(this).attr('method'),
            data: $(this).serialize(),
            //success: function (response) {
            success: function (json) {
                console.log(json)
                // on successfull creating object
                // 1. clear the form.
                $("#entrada-form").trigger('reset');
                // 2. focus to nickname input 
                $("#codigo").focus();

                // display the newly friend to table.
                //var instance = JSON.parse(json);
                //var instance = JSON.parse(response['instance']);
                //var fields = instance[0]["fields"];
                $("#my_entrada tbody").prepend(
                    `<tr>
                    <td>${json["codigob"] || ""}</td>
                    <td>${json["nombre"] || ""}</td>
                    <td>${json["descripcion"] || ""}</td>
                    <td>${json["cantidad"] || ""}</td>
                    
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


