// console.log("upper.js 가 로드되었습니다.")

const emotion_list= ["angel","angry","angry_devil","broken-heart","cool","cry","dead","devil","flat","happy","hearts","joycry","kiss","laugh","love","neutral","puke","puke_rainbow","relax","rolling-eyes","sad","sad_cry","shut","sigh","sleep","smile","smile_heart","stunned","surprised","suspicious","sweat","thinking","why","wink","yummy"]

const weather_list=["cloudy", "cold","leaf","moon","rain","rainbow","snow","snow_cloudy","storm","sun","wind"]

const things_list = ["camera","chat","civil-rights","covid-19","dental","game-over","grandma","hard-work","hold-hand","level-up","medicine","peace","school","sing","washer","weight","whatsapp","zehovah"]


function helloworld() {
  console.log("helloworld");
}

function display_icon(icons, num) {

  let icons_list = icons.split("&amp;");
  console.log(icons_list);
  id_num = "icons" + num.toString();
  let div_icons = document.getElementById(id_num);

  if (is_in(icons_list, emotion_list)) {
    div_icons.insertAdjacentHTML("beforeend", `<span>오늘의 감정:</span>`);
    here:
    for (i = 0; i < icons_list.length; i++) {
      for(j=0;j<emotion_list.length;j++){
        if(icons_list[i]==emotion_list[j]){
          let temp_html=`<span title="`+emotion_list[j]+`"><img src="/static/images/icons/emotion/`+emotion_list[j]+`.png" class="icon" alt="" /></span>`
          div_icons.insertAdjacentHTML("beforeend",temp_html)
          continue here;
        }
      }
    } 
    div_icons.insertAdjacentHTML("beforeend",`<br>`)
  }

  if (is_in(icons_list, weather_list)) {
    div_icons.insertAdjacentHTML("beforeend", `<span>  오늘의 날씨:</span>`);
    top:
    for (i = 0; i < icons_list.length; i++) {
      for(j=0;j<weather_list.length;j++){
        if(icons_list[i]==weather_list[j]){
          let temp_html=`<span title="`+weather_list[j]+`"><img src="/static/images/icons/weather/`+weather_list[j]+`.png" class="icon" alt="" /></span>`
          div_icons.insertAdjacentHTML("beforeend",temp_html)
          continue top;
        }
      }
    }
    div_icons.insertAdjacentHTML("beforeend",`<br>`)
  }
  if(is_in(icons_list,things_list)){
    div_icons.insertAdjacentHTML("beforeend", `<span>오늘 있었던 일:</span>`);
    things:
    for (i = 0; i < icons_list.length; i++) {
      for(j=0;j<things_list.length;j++){
        if(icons_list[i]==things_list[j]){
          let temp_html=`<span title="`+things_list[j]+`"><img src="/static/images/icons/things/`+things_list[j]+`.png" class="icon" alt="" /></span>`
          div_icons.insertAdjacentHTML("beforeend",temp_html)
          continue things;
        }
      }
    }
    div_icons.insertAdjacentHTML("beforeend",`<br/>`)
  }
}

function is_in(list_1, list_2) {
  for (i = 0; i < list_2.length; i++) {
    // console.log(list_2[i]);
    if (list_1.includes(list_2[i])) {
      return true;
    }
  }
  return false;
}
