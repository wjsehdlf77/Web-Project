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
      

      let pe = this.parentElement.parentElement
      let div_count=pe.getElementsByClassName('feed_txt')
      let count_id= div_count[0].getAttribute('id')
      // console.log(count_id)
      let content = div_count.item(0)
      content = content.textContent

      c_txt=content.substr(3,content.length)
      c_txt=c_txt.substr(0,c_txt.length-1)
      if (checkbox.checked){
        c_txt=(parseInt(c_txt)+1).toString()}
      else{
        c_txt=(parseInt(c_txt)-1).toString()}
      let temp_html = '<b>좋아요 '+c_txt+'개</b>'
      // console.log(div_count)
      like_c=$("#"+count_id)
      like_c.empty()
      like_c.append(temp_html)
      // console.log($("#"+count_id))
    });
  }
}

function add_search_bar(){


  $(this).append(`<form method="GET" action="{% url 'dailyphoto:search' %}">
  <div id="search" style="margin-left:100px;">
    <input name="search" type="date"  />
    <button class="btn btn-basic " style="margin-bottom:10px;"type="submit">검색</button>
  </div>
</form>`)

}

display_like();

$(document).ready(function(){
  $('#description').each(function(){
      //var content = $(this).children('.content');
      var content = $(this).find('.text');
      var content_txt = content.text();
      var content_html = content.html();
      var content_txt_short = content_txt.substring(0,20)+"...";
      var btn_more = $('<a href="javascript:void(0)" class="more">더보기</a>');

      $(this).append(btn_more);
      if(content_txt.length >= 20){
          content.html(content_txt_short)
          
      }else{
          btn_more.hide()
      }
      
      btn_more.click(toggle_content);
      function toggle_content(){
          if($(this).hasClass('short')){
              // 접기 상태
              $(this).html('더보기');
              content.html(content_txt_short)
              $(this).removeClass('short');
          }else{
              // 더보기 상태
              $(this).html('접기');
              content.html(content_html);
              $(this).addClass('short');

          }
      }
  });


  $('#search').addEventListener('click',function(){
  //   $(this).append(`<form method="GET" action="{% url 'dailyphoto:search' %}">
  //   <div id="search" style="margin-left:100px;">
  //     <input name="search" type="date"  />
  //     <button class="btn btn-basic " style="margin-bottom:10px;"type="submit">검색</button>
  //   </div>
  // </form>`)

  $(this).html(`<form method="GET" action="{% url 'dailyphoto:search' %}">
  <div id="search" style="margin-left:100px;">
    <input name="search" type="date"  />
    <button class="btn btn-basic " style="margin-bottom:10px;"type="submit">검색</button>
  </div>
</form>`)

    
    


  })
});

