function sendCaptureRequest(id) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = renderImage(xhttp, id)
  URL = "http://localhost:1337/uimage/" + id
  xhttp.open("POST", URL, true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send();
}

function renderImage( xhttp, id )
      if (this.readyState == 4 && this.status == 200) {
         filename = "images/" + id + ".jpg"
         url = url_for("static", filename=filename")
         alert(url)
         document.getElementById(id).src=url
      }
}

function capture(id) {
     alert("Capture")
     document.getElementById("log").innerHTML = "Clicked pic for " + id;
     sendCaptureRequest(id) 
}
