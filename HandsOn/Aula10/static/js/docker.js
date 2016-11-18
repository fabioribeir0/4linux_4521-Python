$("document").ready(function(){
    $(".btn-success").each(function(){
        $(this).click(function(){
            bid = $(this).attr("id");
            $.ajax({
                url:"/start/"+bid,
                type: "GET"
            })
            .done(function(data){
                alert(data.message);
                window.location.href="/";
            })
            .fail(function(data){
                alert("Falhou");
                console.log(data)
            })
        });
    });

    $(".btn-danger").each(function(){
        $(this).click(function(){
            bid = $(this).attr("id");
            $.ajax({
                url:"/stop/"+bid,
                type: "GET"
            })
            .done(function(data){
                alert(data.message);
                window.location.href="/";
            })
            .fail(function(data){
                alert("Falhou");
                console.log(data)
            })
        });
    });

});
