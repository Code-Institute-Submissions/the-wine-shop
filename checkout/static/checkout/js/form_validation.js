// Form field validation at checkout
// Highlight compulsory fields red that aren't filled in

$(document).ready(function () {

    $( "#submit-button" ).click(function() {
        var a = $("#id_forename").val();
        var b = $("#id_surname").val();
        var c = $("#id_email").val();
        var d = $("#id_address1").val();
        var e = $("#id_town").val();
        var f = $("#id_country").val();
        var g = $("#id_postcode").val();
        var h = $("#id_phone").val();

        if (a === "") {
            $("#id_forename").css('border', '1px solid red');
        }
        if (b === "") {
            $("#id_surname").css('border', '1px solid red');
        }
        if (c === "") {
            $("#id_email").css('border', '1px solid red');
        }
        if (d === "") {
            $("#id_address1").css('border', '1px solid red');
        }
        if (e === "") {
            $("#id_town").css('border', '1px solid red');
        }
        if (f === "") {
            $("#id_country").css('border', '1px solid red');
        }
        if (g === "") {
            $("#id_postcode").css('border', '1px solid red');
        }
        if (h === "") {
            $("#id_phone").css('border', '1px solid red');
        }
    });
});