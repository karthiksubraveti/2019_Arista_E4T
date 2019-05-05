function captureAndUpdateImage(imgObj, imageName) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
     if ( this.readyState == 4 && this.status == 200 ) {
        var resp = JSON.parse(this.response)
        renderImage(imgObj, resp);
     }
  }
  URL = window.location.href + "capture/" + imageName

  xhttp.open("GET", URL, true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send();
}

function renderImage(imgObj, resp) {
      var url = window.location.href + resp["url"]
      imgObj.src=url
}

function capture() {
     var imageName = ""
     var imgObj
     if (this.id == "user1") {
        imgObj = document.getElementById("uimg1")
        imageName = "user1"
     } else {
        imgObj = document.getElementById("uimg2")
        imageName = "user2"
     }
     captureAndUpdateImage(imgObj, imageName)
}
