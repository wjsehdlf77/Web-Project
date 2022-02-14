console.log("lower.js 가 로드되었습니다.")

function helloworld(){
  console.log("helloworld")
}


function display_like(){
  let posts=document.getElementsByClassName('sub_body_form')
  for (i = 1; i<posts.length+1;i++){

    id_str = 'like_' + i.toString()
    // console.log(id_str)
    let checkbox_label =  document.getElementById(id_str)
    // console.log(checkbox_label)
    let checkbox = checkbox_label.getElementsByTagName('input')[0];
    let checkbox_in = checkbox_label.getElementsByTagName('span')[0];
    // console.log(checkbox)
    checkbox.addEventListener('change', function(e) {
    // console.log(checkbox.checked, checkbox.value);
    // console.log(request) //request is not defined
    // console.log(user)
    if (checkbox.checked){
      checkbox_in.innerHTML=`<img src="/static/images/cloud_full.png" class="like_icon" alt="" />`
      $.ajax({
        type:'post',
        url:'/',
        dataType:'json',
        data:{
          'like':true
          // 'author':request.user,
          // 'post':request.post
        },
        success : function(data){
          alert('success??!!')
        },
        complete:function(data){
          // console.log('complete')
        }

      })
    }
    else{
      checkbox_in.innerHTML=`<img src="/static/images/cloud_empty.png" class="like_icon" alt="" />`
    }
  
    });
    checkbox_label.addEventListener('click',function(){
      // document.readyState
      like_count = 'like_count'+i.toString()
  
      // window.location.reload()
    $("#"+like_count).load(window.location.href + "#"+like_count);
  })
  

  }

}

display_like()