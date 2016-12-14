$(document).ready(function(){
  $("#reset_npwd_input").blur(function(){
    if(document.getElementById("reset_npwd_input").value.length < 6){
      document.getElementById("reset_npwd_hint").style.visibility="visible";
    }else{
      document.getElementById("reset_npwd_hint").style.visibility="hidden";
    }
  });

  $("#reset_rpwd_input").blur(function(){
    if(document.getElementById("reset_rpwd_input").value == document.getElementById("reset_npwd_input").value){
      document.getElementById("reset_rpwd_hint").style.visibility="hidden";
    }else{
      document.getElementById("reset_rpwd_hint").style.visibility="visible";
    }
  });
});


