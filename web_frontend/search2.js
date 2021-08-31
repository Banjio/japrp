$(document).ready(function(){
$("#search-button").click(function(){
    $("#search-result").fadeToggle();
});
});

function removeAllSearchResults() {
    $(document).ready(function(){
        $("#search-result").children().remove();
    //for (child in resultNode){
        //console.log(child);
        //resultNode[child].remove();
    //}
});
}

//removeAllSearchResults();