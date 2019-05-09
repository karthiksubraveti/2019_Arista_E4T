// captureAndUpdateImage is called by capture function
// This sends a Get request to the server and gets the
// path of the image as response
function captureAndUpdateImage(imgObj) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
     if ( this.readyState == 4 && this.status == 200 ) {
        try {
            resp = JSON.parse(this.response)
            resp2 = JSON.parse(resp)
            
            // ******* CHANGE 6 *******
            // add alert(resp2) in the next line

        
        } catch(err) {
            alert(err)
        }
        renderImage(imgObj, resp2)
     }
  }
  URL = window.location.href + "capture"

  xhttp.open("GET", URL, true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send();
}

// renderImage sets the src of the image object to the path returned
// by the server.
function renderImage(imgObj, resp) {
      var path = window.location.href + resp.basedir + "/" + resp.fname
      imgObj.src=path 
}

// capture checks which button triggered the event,
// based on the owner, it will select which image object
// to display the image into.
function capture() {
     var imageName = ""
     var imgObj
     if (this.id == "user1") {
        imgObj = document.getElementById("uimg1")
     } else {
        imgObj = document.getElementById("uimg2")
     }

     // ***** CHANGE 7 *******
     // add alert("Capture called")
     captureAndUpdateImage(imgObj)
}
