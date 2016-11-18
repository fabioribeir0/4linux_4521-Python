$("document").ready(function(){
    $(".btn-success").each(function(){
        $(this).click(function(){
            bid = $(this).attr("id");
            alert("ID: "+bid);
        });
    });

    $(".btn-danger").each(function(){
        $(this).click(function(){
            bid = $(this).attr("id");
            alert("ID: "+bid);
        });
    });
});
