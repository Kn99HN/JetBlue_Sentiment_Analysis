$.post( "/postmethod", {
      canvas_data: JSON.stringify(outputData)
    }, function(err, req, resp){
      window.location.href = "/results/"+resp["responseJSON"]["uuid"];
    });



function setQuote(quote) {
    document.getElementById("quote").innerHTML = quote[0].toString();
    document.getElementById("source").innerHTML = Someone on quote[1].toString();
    document.getElementById("sentiment").innerHTML = "Our analysis shows that this quote is " + quote[2].toString();
    document.getElementById("quote").innerHTML = quote[0].toString();
}