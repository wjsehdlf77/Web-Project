
function read_f(e) {

  var img=$('#preview_pic')
  if(window.FileReader) {
    var file  = e.target.files[0];
    var reader = new FileReader();
    if (file && file.type.match('image.*')) {
      reader.readAsDataURL(file);
      console.log(reader)
    } else {
      img.css('display', 'none');
      img.attr('src', '');
    }
    reader.onloadend = function (e) {
      img.attr('src', reader.result);
      img.css('display', 'block');
    }
  }
}

  // document.getElementById('datePicker').valueAsDate = new Date();
  document.getElementById("id_photo").addEventListener('change', read_f, false);
