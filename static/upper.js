// console.log("upper.js 가 로드되었습니다.")
function helloworld() {
  console.log("helloworld");
}

function display_icon(icons, num) {
  // if counter

  let icons_list = icons.split("&amp;");
  console.log(icons_list);
  id_num = "icons" + num.toString();
  // console.log(id_num)
  let div_icons = document.getElementById(id_num);
  // console.log(div_icons)

  if (is_in(icons_list, ["angel","angry","angry_devil","broken-heart","cool","cry","dead","devil","flat","happy","hearts","joycry","kiss","laugh","love","meh","neutral","puke","puke_rainbow","relax","rolling-eyes","sad","sad_cry","shut","sigh","sleep","smile","smile_heart","stunned","suprised","suspicious","sweat","thinking","why","wink","yummy"])) {
    div_icons.insertAdjacentHTML("beforeend", `<span>오늘의 감정:</span>`);
    for (i = 0; i < icons_list.length; i++) {
      if (icons_list[i] == "happy") {
        div_icons.insertAdjacentHTML(
          "beforeend",
          `<span><img src="/static/images/icons/emotion/happy.png" class="icon" alt="" /></span>`
        );
        continue;
      } else if (icons_list[i] == "hearts") {
        div_icons.insertAdjacentHTML(
          "beforeend",
          `<span><img src="/static/images/icons/emotion/hearts.png" class="icon" alt="" /></span>`
        );
        continue;
      } else if (icons_list[i] == "meh") {
        div_icons.insertAdjacentHTML(
          "beforeend",
          `<img src="/static/images/icons/emotion/rolling-eyes.png" class="icon" alt="" />`
        );
        continue;
      }
    }
  }

  if (is_in(icons_list, ["sunny", "cloud", "rain"])) {
    div_icons.insertAdjacentHTML("beforeend", `<span>  오늘의 날씨:</span>`);

    for (i = 0; i < icons_list.length; i++) {
      if (icons_list[i] == "sunny") {
        div_icons.insertAdjacentHTML(
          "beforeend",
          `<img src="/static/images/icons/weather/sun.png" class="icon" alt="" />`
        );
      } else if (icons_list[i] == "cloud") {
        div_icons.insertAdjacentHTML(
          "beforeend",
          `<img src="/static/images/icons/weather/cloudy.png" class="icon" alt="" />`
        );
      } else if (icons_list[i] == "rain") {
        div_icons.insertAdjacentHTML(
          "beforeend",
          `<img src="/static/images/icons/weather/storm.png" class="icon" alt="" /> `
        );
      }

      if (icons_list[i] == "-1") {
        div_icons.insertAdjacentHTML("beforeend", " ");
      } else {
      }
    }
  }

  if(is_in(icons_list,["school","weight"])){
    div_icons.insertAdjacentHTML("beforeend", `<span>오늘 있었던 일:</span>`);
    for (i = 0; i < icons_list.length; i++) {
      if (icons_list[i] == "school") {
        div_icons.insertAdjacentHTML(
          "beforeend",
          `<span><img src="/static/images/icons/things/school.png" class="icon" alt="" /></span>`
        );
      } else if (icons_list[i] == "hearts") {
        div_icons.insertAdjacentHTML(
          "beforeend",
          `<span><img src="/static/images/icons/things/weight.png" class="icon" alt="" /></span>`
        );
      }
    }
  }
}

function is_in(list_1, list_2) {
  for (i = 0; i < list_2.length; i++) {
    console.log(list_2[i]);
    if (list_1.includes(list_2[i])) {
      return true;
    }
  }
  return false;
}
