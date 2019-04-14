   function title_check()
  {	
  	var title = document.getElementById("title_input").value;
	if(title.match(/^\s*$/))
		{document.getElementById("title_tip").style.visibility="visible";}
	else{document.getElementById("title_tip").style.visibility="hidden";}
	  
	}
	  function depart_time_check()
  {	
  	var depart_time = document.getElementById("depart_time_input").value;
	if(depart_time.match(/^\s*$/))
		{document.getElementById("depart_time_tip").style.visibility="visible";}
	else{document.getElementById("depart_time_tip").style.visibility="hidden";}
	  
	}
	  function depart_place_check()
  {	
  	var depart_place = document.getElementById("depart_place_input").value;
	if(depart_place.match(/^\s*$/))
		{document.getElementById("depart_place_tip").style.visibility="visible";}
	else{document.getElementById("depart_place_tip").style.visibility="hidden";}
	  
	}
	  function people_check()
  {	
  	var people = document.getElementById("people_input").value;
	if(people.match(/^\s*$/))
		{document.getElementById("people_tip").style.visibility="visible";}
	else{document.getElementById("people_tip").style.visibility="hidden";}
	  
	}

		  function describe_check()
  {	
  	var describe = document.getElementById("describe_input").value;
	if(describe.match(/^\s*$/))
		{document.getElementById("describe_tip").style.visibility="visible";}
	else{document.getElementById("describe_tip").style.visibility="hidden";}
	}
		  function contact_check()
  {	
  	var contact = document.getElementById("contact_input").value;
	if(contact.match(/^\s*$/))
		{document.getElementById("contact_tip").style.visibility="visible";}
	else{document.getElementById("contact_tip").style.visibility="hidden";}
	  
	}// JavaScript Document