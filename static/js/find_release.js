if (typeof FileReader == 'undefined') {
    document.getElementById("xmTanDiv").InnerHTML = "<h1>当前浏览器不支持FileReader接口</h1>";
   document.getElementById("xdaTanFileImg").setAttribute("disabled", "disabled");
        }
//选择图片，马上预览
 function xmTanUploadImg(obj) {
  var file = obj.files[0];               
  console.log(obj);console.log(file);
  console.log("file.size = " + file.size);
  var reader = new FileReader();
  reader.onload = function (e) {
      
  var img = document.getElementById("avarimgs");
      img.src = e.target.result;
   //或者 img.src = this.result;  //e.target == this
  }
      reader.readAsDataURL(file)
  }
   function title_check()
  {	
  	var title = document.getElementById("title_input").value;
	if(title.match(/^\s*$/))
		{document.getElementById("title_tip").style.visibility="visible";}
	else{document.getElementById("title_tip").style.visibility="hidden";}
	  
	}
	  function find_time_check()
  {	
  	var find_time = document.getElementById("find_time_input").value;
	if(find_time.match(/^\s*$/))
		{document.getElementById("find_time_tip").style.visibility="visible";}
	else{document.getElementById("find_time_tip").style.visibility="hidden";}
	  
	}
	  function find_place_check()
  {	
  	var find_place = document.getElementById("find_place_input").value;
	if(find_place.match(/^\s*$/))
		{document.getElementById("find_place_tip").style.visibility="visible";}
	else{document.getElementById("find_place_tip").style.visibility="hidden";}
	  
	}
	  function contact_check()
  {	
  	var contact = document.getElementById("contact_input").value;
	if(contact.match(/^\s*$/))
		{document.getElementById("contact_tip").style.visibility="visible";}
	else{document.getElementById("contact_tip").style.visibility="hidden";}
	  
	}
		  function describe_check()
  {	
  	var describe = document.getElementById("describe_input").value;
	if(describe.match(/^\s*$/))
		{document.getElementById("describe_tip").style.visibility="visible";}
	else{document.getElementById("describe_tip").style.visibility="hidden";}
	}// JavaScript Document