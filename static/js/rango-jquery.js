$(document).ready(function(){
    // JQuery code to be added in here.
    $("#about-btn").click( function(event){
        alert("You clicked the button using JQuery!");
        str = $("#test").html()
        str = str + "haha!"
        $("#test").html(str)
    });
    $("#about-btn").addClass("btn btn-primary");
    
    $("p").hover( function(){
       $(this).css('color','red');
    },
    function(){
       $(this).css('color','blue');  
    });
});
