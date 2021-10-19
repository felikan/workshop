$(document).ready(function() {
    $.get("../resources/code_snippets/example.html", function(data){
        $('#example').html(data);
    });
});