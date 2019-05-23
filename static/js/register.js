var code; //在全局 定义验证码
var password_flag = false;

function addDisabled() {
    $("#btn").addClass("disabled");
}

function removeDisabled() {
    $("#btn").removeClass("disabled");
}

function createCode() {
    code = "";
    var codeLength = 4;
    var selectChar = new Array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');
    for (var i = 0; i < codeLength; i++) {
        var charIndex = Math.floor(Math.random() * 52);
        code += selectChar[charIndex];
    }
    document.getElementById("discode").style.fontFamily = "Fixedsys"; //设置字体
    document.getElementById("discode").style.letterSpacing = "10px"; //字体间距
    document.getElementById("discode").style.color = "#ff0000"; //字体颜色
    document.getElementById("discode").innerHTML = code; // 显示
    document.getElementById("page_code").value = code;
}

function Codechange() {
    code = "";
    var codeLength = 4;
    var selectChar = new Array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');
    for (var i = 0; i < codeLength; i++) {
        var charIndex = Math.floor(Math.random() * 52);
        code += selectChar[charIndex];
    }
    document.getElementById("discode").innerHTML = code;
    document.getElementById("page_code").value = code;
}

function studentid_panduan() {
    var reg = /^(10|[1-9]\d).*\d{6}$/;
    var password = document.getElementById("studentid").value;
    var password_length = password.length;
    if (password.match(/^\s*$/)) {
        document.getElementById("studentid_tip").innerHTML = "请输入学号";
        document.getElementById("studentid_tip").style.visibility = "visible";
        addDisabled();
    }
    else if (password_length != 8) {
        document.getElementById("studentid_tip").innerHTML = "学号只能为8位";
        document.getElementById("studentid_tip").style.visibility = "visible";
        addDisabled();
    }
    else {
        if (!reg.test(password)) {
            document.getElementById("studentid_tip").innerHTML = "学号格式不正确";
            document.getElementById("studentid_tip").style.visibility = "visible";
            addDisabled();
        }
        else {
            document.getElementById("studentid_tip").style.visibility = "hidden";
            $("#btn").removeClass("disabled");
        }
    }
}

function yanzhengma_zhengquepanduan() {
    var yanzhengma = document.getElementById("yanzhengma").value;
    if (yanzhengma.toLowerCase() != code.toLowerCase()) {
        addDisabled();
    } else {
        $("#btn").removeClass("disabled");
    }
}

function username_panduan() {
    var username = document.getElementById("username").value;
    var username_length = username.length;
    if (username.match(/^\s*$/)) {
        document.getElementById("username_tip").innerHTML = "昵称不能为空";
        document.getElementById("username_tip").style.visibility = "visible";
        addDisabled();
    }
    else if (username_length > 0 && username_length < 2) {
        document.getElementById("username_tip").innerHTML = "昵称不能少于2个文字或字符";
        document.getElementById("username_tip").style.visibility = "visible";
        addDisabled();
    }
    else {
        document.getElementById("username_tip").style.visibility = "hidden";
        $("#btn").removeClass("disabled");
    }
}

function yanzhengma_panduan() {
    var yanzhengma = document.getElementById("yanzhengma").value;
    if (yanzhengma.match(/^\s*$/)) {
        document.getElementById("yanzhengma_tip").innerHTML = "请输入验证码";
        document.getElementById("yanzhengma_tip").style.visibility = "visible";
        addDisabled();
    }
    else if (yanzhengma.length != 4) {
        document.getElementById("yanzhengma_tip").innerHTML = "验证码为4位";
        document.getElementById("yanzhengma_tip").style.visibility = "visible";
        addDisabled();
    }
    else {
        document.getElementById("yanzhengma_tip").style.visibility = "hidden";
        $("#btn").removeClass("disabled");
    }

}

function password_repanduan() {
    var password = document.getElementById("password").value;
    var repassword = document.getElementById("repassword").value;
    if (!password_flag) {
        document.getElementById("repassword_tip").innerHTML = "请先输入正确密码";
        document.getElementById("repassword_tip").style.visibility = "visible";
        addDisabled();
    }
    else {
        if (password != repassword) {
            document.getElementById("repassword_tip").innerHTML = "两次密码不一样";
            document.getElementById("repassword_tip").style.visibility = "visible";
            addDisabled();
        }
        else {
            document.getElementById("repassword_tip").style.visibility = "hidden";
            $("#btn").removeClass("disabled");
        }
    }
    /*if(repassword.match(/^\s*$/))
    {
        document.getElementById("repassword_tip").innerHTML="请输入确认密码";
        document.getElementById("repassword_tip").style.visibility="visible";
        addDisabled();
    }
    else
    {
        if(password!=repassword)
        {
            document.getElementById("repassword_tip").innerHTML="两次密码不一样";
            document.getElementById("repassword_tip").style.visibility="visible";
            addDisabled();
        }
        else
        {
            document.getElementById("repassword_tip").style.visibility="hidden";
            $("#btn").removeClass("disabled");
        }
    }*/

}

function password_panduan() {
    var reg = /^(?=.*[a-z])(?=.*[0-9]).{8,20}$/;
    var password = document.getElementById("password").value;
    var password_length = password.length;
    if (password_length == 0) {
        document.getElementById("password_tip").innerHTML = "请输入密码";
        document.getElementById("password_tip").style.visibility = "visible";
        addDisabled();
    }
    else if (password_length > 0 && password_length < 8) {
        document.getElementById("password_tip").innerHTML = "密码不能少于8位";
        document.getElementById("password_tip").style.visibility = "visible";
        addDisabled();
    }
    else {
        if (!reg.test(password)) {
            document.getElementById("password_tip").innerHTML = "密码必须是字母和数字结合";
            document.getElementById("password_tip").style.visibility = "visible";
            addDisabled();
        }
        else {
            document.getElementById("password_tip").style.visibility = "hidden";
            $("#btn").removeClass("disabled");
                        password_flag = true;
        }
    }
}

// JavaScript Document