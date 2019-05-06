function captureAndUpdateImage(imgObj) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
     if ( this.readyState == 4 && this.status == 200 ) {
        try {
            resp = JSON.parse(this.response)
            resp2 = JSON.parse(resp)
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

function renderImage(imgObj, resp) {
      var path = window.location.href + resp.basedir + "/" + resp.fname
      imgObj.src=path 
}

function capture() {
     var imageName = ""
     var imgObj
     if (this.id == "user1") {
        imgObj = document.getElementById("uimg1")
     } else {
        imgObj = document.getElementById("uimg2")
     }
     captureAndUpdateImage(imgObj)
}
