// console.log("upload.js 가 로드되었습니다.")
function helloworld(){
  console.log("helloworld")
}

function display_icon(icons,counter){

  let icons_list= icons.split("&amp;");
  console.log(icons_list);
  id_num = 'icons'+counter.toString()
  console.log(id_num)
  let div_icons = document.getElementById(id_num);
  // let div_icons=$("#"+id_num)//에러
  console.log(div_icons)

    

    for (i = 0; i < icons_list.length; i++) {
      if (icons_list[i] == "happy") {
        div_icons.insertAdjacentHTML("beforeend","<span><i class='fas fa-regular fa-face-smile-beam'></i>happy</span>");
      } else if (icons_list[i] == "hearts") {
        div_icons.insertAdjacentHTML("beforeend","<span><i class='fas fa-regular fa-face-smile-hearts'></i> hearts</span>");
      } else if (icons_list[i] == "meh") {
        div_icons.insertAdjacentHTML("beforeend","<i class='fas fa-regular fa-face-meh'></i>meh ");
      } else if (icons_list[i] == "sunny") {
        div_icons.insertAdjacentHTML("beforeend","<i class='fas fa-sun'></i>sunny ");
      } else if (icons_list[i] == "cloud") {
        div_icons.insertAdjacentHTML("beforeend","<i class='fas fa-solid fa-clouds'></i>cloud ");
      } else if (icons_list[i] == "rain") {
        div_icons.insertAdjacentHTML("beforeend","<i class='fas fa-cloud-showers-heavy'></i> rain ");
      } else if (icons_list[i] == "-1") {
        div_icons.insertAdjacentHTML("beforeend"," ");
      } else {
      }
    }  

}