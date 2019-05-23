// JavaScript Document
	var code; 
function createCode()
	{ 
	code = "";
	var codeLength =4;
	var selectChar = new Array(0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z');
	for(var i=0;i<codeLength;i++)
	{
		var charIndex =Math.floor(Math.random()*52);
		code +=selectChar[charIndex];
	}	
	document.getElementById("discode").style.fontFamily="Fixedsys"; //设置字体
	document.getElementById("discode").style.letterSpacing="10px"; //字体间距
	document.getElementById("discode").style.color="#ff0000"; //字体颜色
	document.getElementById("discode").innerHTML=code; // 显示
	document.getElementById("page_code").value = code;
	}
function Codechange()
{
		code = "";
	var codeLength =4;
	var selectChar = new Array(0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z');
	for(var i=0;i<codeLength;i++)
	{
		var charIndex =Math.floor(Math.random()*52);
		code +=selectChar[charIndex];
	}	
	document.getElementById("discode").innerHTML=code;
	document.getElementById("page_code").value = code;
	}
function yanzhengma_panduan()
	{
		var yanzhengma = document.getElementById("yanzhengma").value;
		if(yanzhengma.match(/^\s*$/))
		{
			document.getElementById("yanzhengma_tip").innerHTML="请输入验证码";
			document.getElementById("yanzhengma_tip").style.visibility="visible";
		}
		else if(yanzhengma.length!=4)
		{
			document.getElementById("yanzhengma_tip").innerHTML="验证码为4位";
			document.getElementById("yanzhengma_tip").style.visibility="visible";	
		}
		else
		{
			document.getElementById("yanzhengma_tip").style.visibility="hidden";
		}
		
	}	
function yanzhengma_zhengquepanduan()
	{
		var yanzhengma = document.getElementById("yanzhengma").value;
		if(yanzhengma.toLowerCase()!=code.toLowerCase())
		{
		alert("错误");	
		}
	}

function studentid_panduan()	
	{	var reg=/^(10|[1-9]\d).*\d{6}$/;
		var password = document.getElementById("studentid").value;
		var password_length=password.length;
		if(password.match(/^\s*$/))
		{	document.getElementById("studentid_tip").innerHTML="请输入学号";
			document.getElementById("studentid_tip").style.visibility="visible";	
		}
		else if(password_length!=8)
		{
			document.getElementById("studentid_tip").innerHTML="学号只能为8位";
			document.getElementById("studentid_tip").style.visibility="visible";		
		}
		else
		{
			if(!reg.test(password))
			{
			document.getElementById("studentid_tip").innerHTML="学号格式不正确";
			document.getElementById("studentid_tip").style.visibility="visible";		
			}
			else
			{
				document.getElementById("studentid_tip").style.visibility="hidden";
			}
		}
	}

function password_panduan()	
	{	var reg=/^(?=.*[a-z])(?=.*[0-9]).{8,20}$/;
		var password = document.getElementById("password").value;
		var password_length=password.length;
		if(password_length==0)
		{	document.getElementById("password_tip").innerHTML="请输入密码";
			document.getElementById("password_tip").style.visibility="visible";	
		}
		else if(password_length>0&&password_length<8)
		{
			document.getElementById("password_tip").innerHTML="密码不能少于8位";
			document.getElementById("password_tip").style.visibility="visible";		
		}
		else
		{
			if(!reg.test(password))
			{
			document.getElementById("password_tip").innerHTML="密码必须是字母和数字结合";
			document.getElementById("password_tip").style.visibility="visible";		
			}
			else
			{
				document.getElementById("password_tip").style.visibility="hidden";
			}
		}

}