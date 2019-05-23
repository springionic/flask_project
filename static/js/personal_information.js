window.onload = function(){
    if(window.location.search){
        turn();
    }
}
function turn() {
    var cls = document.getElementById("wrapp").className;
    if (/photo_front/.test(cls)) {
        cls = cls.replace(/photo_front/, 'photo_back');
    }
    else {
        cls = cls.replace(/photo_back/, 'photo_front');
    }
    return wrapp.className = cls;
}// JavaScript Document
/**
 * 重命名昵称的函数
 */
function rename() {
    user_id = $('#user_id').text();
    new_name = prompt('请输入新昵称：');
    if (new_name) {
        $.ajax({
            url: '/rename',
            type: 'POST',
            data: {user_id: user_id, new_name: new_name},
            dataType: 'json',
            success: function (data) {
                if (data.status == 1) {
                    alert('用户昵称修改成功！')
                    location.reload();
                }
                if (data.status == 0) {
                    alert('修改失败，请稍后再试！')
                }
            }
        })
    }
}

// 删除拼车记录的函数
function del_carpool(carpool_id) {
    var option = confirm("确定删除此记录吗？")
    if (option == true) {
        $.ajax({
            url: '/del_carpool',
            type: 'POST',
            data: {carpool_id: carpool_id},
            dataType: 'json',
            success: function (data) {
                if (data.status == 1) {
                    alert('删除成功!')
                    location.href='/user_information?a=1';
                }
                else {
                    alert('删除失败，请稍后在试！')
                }
            }
        })
    }
}

// 删除约吧记录的函数
function del_play(play_id) {
    var option = confirm("确定删除此记录吗？")
    if (option == true) {
        $.ajax({
            url: '/del_play',
            type: 'POST',
            data: {play_id: play_id},
            dataType: 'json',
            success: function (data) {
                if (data.status == 1) {
                    alert('删除成功!')
                    location.href='/user_information?a=1';
                }
                else {
                    alert('删除失败，请稍后在试！')
                }
            }
        })
    }
}

// 删除寻物启事记录
function del_search(search_id) {
    var option = confirm("确定删除此记录吗？")
    if (option == true) {
        $.ajax({
            url: '/del_search',
            type: 'POST',
            data: {search_id: search_id},
            dataType: 'json',
            success: function (data) {
                if (data.status == 1) {
                    alert('删除成功!')
                    location.href='/user_information?a=1';
                }
                else {
                    alert('删除失败，请稍后在试！')
                }
            }
        })
    }
}

// 删除失物招领函数
function del_lost(lost_id) {
    var option = confirm("确定删除此记录吗？")
    if (option == true) {
        $.ajax({
            url: '/del_lost',
            type: 'POST',
            data: {lost_id: lost_id},
            dataType: 'json',
            success: function (data) {
                if (data.status == 1) {
                    alert('删除成功!')
                    location.href='/user_information?a=1';
                }
                else {
                    alert('删除失败，请稍后在试！')
                }
            }
        })
    }
}


