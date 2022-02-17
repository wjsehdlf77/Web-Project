console.log("lower.js 가 로드되었습니다.");
function helloworld() {
  console.log("helloworld");
}

function display_like() {
  console.log('function display_like 실행')
  let posts = document.getElementsByClassName("sub_body_form");
  for (i = 1; i < posts.length + 1; i++) {
    // console.log(i)
    id_str = "like_" + i.toString();
    let checkbox_label = document.getElementById(id_str);
    let checkbox = checkbox_label.getElementsByTagName("input")[0];
    let checkbox_in = checkbox_label.getElementsByTagName("span")[0];
    checkbox.addEventListener("change", function (e) {


      if (checkbox.checked) {
        checkbox_in.innerHTML = `<img src="/static/images/cloud_full.png" class="like_icon" alt="" />`;

        let csrf_token = $("[name=csrfmiddlewaretoken]").val();
        let post_id = checkbox_label.getElementsByTagName("postid")[0];
        post_id = parseInt(post_id.textContent);
        $.ajax({
          type: "post",
          url: "like/",
          dataType: "json",
          data: {
            post: post_id,
            csrfmiddlewaretoken: csrf_token,
          },
          headers: { "X-CSRFToken": "{{ csrf_token }}" },
          success: function (response) {
            console.log(response);
            alert("success??!!");
          },
          error: function () {
            // console.log("error");
          },
          complete: function () {
            // console.log('complete')
          },
        });
        

      } else {
        checkbox_in.innerHTML = `<img src="/static/images/cloud_empty.png" class="like_icon" alt="" />`;

        let csrf_token = $("[name=csrfmiddlewaretoken]").val();
        let post_id = checkbox_label.getElementsByTagName("postid")[0];
        post_id = parseInt(post_id.textContent);
        $.ajax({
          type: "post",
          url: "unlike/",
          dataType: "json",
          data: {
            post: post_id,
            csrfmiddlewaretoken: csrf_token,
          },
          headers: { "X-CSRFToken": "{{ csrf_token }}" },
          success: function (response) {
            console.log(response);
            alert("success??!!");
          },
          error: function () {
            // console.log("error");
          },
          complete: function () {
            // console.log('complete')
          },
        });
      }
      

      // console.log(e)
      let pe = this.parentElement.parentElement
      // console.log(pe)
      let div_count=pe.getElementsByClassName('feed_txt')
      let count_id= div_count[0].getAttribute('id')
      console.log(count_id)
      let content = div_count.item(0)
      // console.log(content)
      // console.log(typeof(content))
      content = content.textContent

      c_txt=content.substr(3,content.length)
      c_txt=c_txt.substr(0,c_txt.length-1)
      // console.log(c_txt)
      c_txt=(parseInt(c_txt)+1).toString()
      let temp_html = '<b>좋아요 '+c_txt+'개</b>'
      // div_count.innerHTML=temp_html
      // div_count.innerText=temp_html
      console.log(div_count)
      like_c=$("#"+count_id)
      like_c.empty()
      like_c.append(temp_html)



      // window.div_count.reload()
      // $('.feed_txt').load(location.href+' .feed_txt');
      // div_count.load(location.href+' .feed_txt')
      // div_count.     
      // $('.feed_txt').load($('.feed_txt').value)
      // div_count.load(location.href+' .feed_txt')
      // $('.feed_txt').load(location.href+' .feed_txt[0]');
      // $('.feed_txt').load(location.href);//엄청난 오류...
      // $('#'+count_id).load(location.href+' #'+count_id);
      // console.log(typeof(div_count))
      // console.log(typeof($('.feed_txt')))
      // console.log($('.feed_txt'))
      // console.log(div_count)
      console.log($("#"+count_id))
      // location.reload()
    });
    // checkbox_label.addEventListener("click", function () {
    //   like_count = "like_count" + i.toString();
    //   // window.location.reload()
    //   location.reload()
    //   // $("#" + like_count).load(window.location.href + "#" + like_count);
    // });
  }
}

display_like();

