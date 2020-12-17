$(document).ready(function(){
    let placeToDrop = '';
    let element = '';
    const fake = $("#fake");
    $("tr[draggable='true']").on("dragstart", function(e){
//        e.preventDefault();
        element = $(this); //        element.hide();
        $(fake).outerHeight($(this).outerHeight());
    })

    $("tr").on("drop, dragover", function(){
        placeToDrop = $(this);
    })

    $("#table").on("dragover", function(e){
        e.preventDefault();
        $(placeToDrop).after($(fake));
        $(fake).show();
    })

    $("#table").on("dragleave", function(e){
        e.preventDefault();
        $(fake).hide();
    });

    $("#table").on("drop", function(e){
        e.preventDefault();
        $(placeToDrop).after($(element));
        $(fake).hide();
        newOrder();
    })

// Double Click
    $("tr[draggable='true']").dblclick(function() {
        var row = $(this);
        var parent = $(this).parent().children();
        var first = parent.eq(0).find("td:first").html();
        var last = parent.eq( parent.length-1 );

//        console.log( parent );
//        console.log( parent.length );
//        console.log( parent.eq( parent.length-2 ).find("td:first").html() );
//        console.log( row.find("td:first").html() );
//        console.log( first );
//        console.log( row.find("td:first").html() == first );

        $(this).fadeOut("slow");
        setTimeout( function(){
            $('#table tr:first').before( row );
            $('#table tr:first').fadeIn("slow");
            setTimeout( function(){ newOrder(); }, 200);
        }, 500);
    });

})


function newOrder() {
  var temp = [];
  $("tr").each(function() {
    $this = $(this);
    var id = $this.find("td:first").html();
    if (typeof id !== 'undefined') {
      temp.push(id);
    }
  });
  $.post("/jobs/m_order/", {
    'data': JSON.stringify(temp), 'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value })
      .done(function(msg) {
//        console.log( msg );
      })
      .fail(function(xhr, status, error) {
//        console.log( xhr );
//        console.log( status );
//        console.log( error );
      });

}
