/**
 * Created by hp on 2018/3/20.
 */
// //顶部导航条随滚动条滚动
    window.onscroll=function () {
        //获得滚动条的左侧的值，设为负值
        var sl=-Math.max(document.body.scrollLeft,document.documentElement.scrollLeft);
        //设定导航条的左侧的left的值
        document.getElementById('navtop').style.left=sl+'px';
    };
$(function () {
    //当模态框隐藏的时候，加载微信移除事件
    cancel_wx();

    //验证码事件
    $('#imgCode').click(function () {
        ChangeCode();
    });

    //导航条中注册登录的js
    $('#nav-regist,#reg-a').click(function () {
        //清除加载的二维码图片和提示
        $('#wx-load').remove();
        $('#wxtip').remove();
        register();
    });
    $('#nav-login,#login-a').click(function () {
        //清除加载的二维码图片和提示
        $('#wx-load').remove();
        $('#wxtip').remove();
        login();
    });
    //注册的全局变量
    error_name = false;
    error_password = false;
    error_check_password = false;
    error_email = false;
    error_check = true;//协议默认是勾选的
    //登录的全局变量
    login_uname=false;
    login_upwd=false;

 /*以上定义为局部变量产生undefined错误，无法跳转，改为全局变量后修正*/
    //注册form
    $('#r_uname').blur(function () {
        check_user_name();

        console.log(1)
    });

    $('#rpwd').blur(function () {
        check_pwd();
        console.log(2)
    });

    $('#cpwd').blur(function () {
        check_cpwd();
        console.log(3)
    });

    $('#remail').blur(function () {
        check_email();
        console.log(4)
    });

    $('#allow').click(function () {
        check_agreement();
        console.log(5)
    });
    //提交注册按钮操作
    $('#reg-sub').click(function() {

        //隐藏提示标签清空错误提示
        $('.form-tip').addClass('hidden').children().html('');

        console.log(6);
        check_user_name();
        check_pwd();
        check_cpwd();
        check_email();
        check_agreement();

        if(error_name && error_password && error_check_password && error_email && error_check ) {
            console.log(7);
            $.ajax({
                url:"/user/registerhandle/",
                type: "POST",
                data: $('#reg-form').serialize(),//获取id='reg-from''的form表单的全部数据
                headers:{'X-CSRFtoken':$.cookie('csrftoken')},
                dataType:'JSON',
                traditional:true,
                success: function(data){
                    success_call(data);
                },
                error:function(data){
                    var v='网络故障';
                    $('.form-tip').removeClass('hidden').children().html(v)
                }
            });
        } else {
            console.log(8);
            // $(this).addAttr('disabled','disabled');
            return false;
        }

    });
    //登录form
    $('#username').blur(function () {
        login_name();
    });
    $('#upwd').blur(function () {
        login_pwd();
    });
    //登录按钮操作
    $('#login-sub').click(function () {
        login_name();
        login_pwd();
        if(login_uname && login_upwd){
            $.ajax({
                url:'/user/login/',
                type:'POST',
                data:$('#login-form').serialize(),
                headers:{'X-CSRFtoken':$.cookie('csrftoken')},
                dataType:'JSON',
                traditional:true,
                success: function(data){
                    success_call(data);
                },
                error:function(data){
                    var v='网络故障';
                    $('.form-tip').removeClass('hidden').children().html(v)
                }
            });
        }else {
            console.log(13);
            return false;
        }
    });
    //登录框回车事件
    $('#login-form').submit(function () {
        $('#login-sub').click();
        return false//必须阻断，不然会刷新页面
    });
    //验证码看不清
    $('#check_code').click(function () {
        ChangeCode()
    });
    //微信扫码登录
    $('#wxlogin').click(function () {
        //加载微信二维码函数
        login_wx();
        polling();

        //当扫码图片获取成功，才加载轮询函数，避免同时加载时出现，图片明明已获取成功，但轮询函数认为没有获取到的问题。
        //setTimeout() 方法用于在指定的毫秒数后调用函数或计算表达式。5毫秒后，执行轮询，保证初始图片不为0
        // setTimeout(polling(),console.log('看看二维码图片'+$('#wx-load').length),1000);
        // if(v){
        //     //加载长轮询函数
        //     polling();
        // }

        console.log(5)
    });
    //退出
    $('#nav-li').delegate('#nav-cancel','click',function () {
        $.cookie('*',null);
    })

});
//检查用户名格式
function check_user_name() {
    //用户名必须以字母开头，后面是由字母和数字组成，长度在5位到16位之间。
    var re=/^[a-zA-Z][a-zA-Z0-9]{4,15}$/;
    var uname=$('#r_uname').val().trim();
    if (re.test(uname)){

        $.get("/user/register_exist/?uname="+$('#r_uname').val(),function (data) {
            if(data.count>=1){
                console.log('1.5');
                $('#r_uname').next().html('用户已存在，请换个用户名注册').show();
                error_name = false;
            }else{
                $('#r_uname').next().html('').hide();
                error_name = true;
            }
        });
    }else{
         $('#r_uname').next().html('用户名必须以字母开头，后面是由字母和数字组成，长度在5位到16位之间。').show();
            error_name = false;
    }
}
//密码格式检查
function check_pwd() {
    var len = $('#rpwd').val().length;
    if (len < 6 || len > 20) {
        $('#rpwd').next().html('密码最少6位，最长20位').show();
        error_password = false;
    }
    else {
        $('#rpwd').next().hide();
        error_password = true;
    }
}
//密码确认
function check_cpwd(){
    var pass = $('#rpwd').val();
    var cpass = $('#cpwd').val();
    if (pass != cpass) {
        $('#cpwd').next().html('两次输入的密码不一致').show();
        error_check_password = false;
    }else {
        $('#cpwd').next().hide();
        error_check_password = true;
    }
}
//检查email格式
function check_email() {
    var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
    if (re.test($('#remail').val())) {
        $('#remail').next().hide();
        error_email = true;
    } else {
        $('#remail').next().html('你输入的邮箱格式不正确').show();

        error_check_password = false;
    }
}
//同意协议
function check_agreement() {
    if ($('#allow').is(':checked')) {
            error_check = true;
            $('.error_tip2').hide();
        } else {
            error_check = false;
            $('.error_tip2').html('请勾选').show();

        }
}
//验证码更新
function ChangeCode() {
    var code = document.getElementById('imgCode');
    code.src += '?';
}

//注册界面函数
function register() {
    $('#login-btn').removeClass('active');
    $('#regist-btn').addClass('active');
    $('#login-form').addClass('hide');
    $('#reg-form').removeClass('hide');
}
//登录界面函数
function login(){
    $('#login-btn').addClass('active');
    $('#regist-btn').removeClass('active');
    $('#login-form').removeClass('hide');
    $('#reg-form').addClass('hide');
    var uname=$.cookie('uname');
    $('#username').val(uname);
}
//检查登录框用户名
function login_name() {
    var v=$('#username').val().trim().length;
    if(v===0){
        $('.user-error').html('请填写用户名').show();
        login_uname=false;
    }else {
        $('.user-error').html('').hide();
        login_uname=true;
    }
}
//检查登录框密码
function login_pwd() {
    var v=$('#upwd').val().trim().length;
    if(v===0){
        $('.pwd-error').html('请填写密码').show();
        login_upwd=false;
    }else {
        $('.pwd-error').html('').hide();
        login_upwd=true;
    }
}
//注册和登录提交时ajax-success回调函数
function success_call(data) {

    var p="/user/";
    //根据后台返回的状态码是false还是true来操作
    if(data.status){
        //获取后台发过来的id
        var ids=data.ids;
        //获取后台发过来的用户名
        var uname=data.unames;
        console.log('uname:'+uname);

        // request.setRequestHeader('uname',uname);
        console.log('11');

        //替换登录标签为

        var v1='<a id="nav-uname" ids="' +ids+
            '" href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">' +uname+
            '<span class="caret"></span> </a> ' +
            '<ul class="dropdown-menu"> ' +
            '<li><a href="'+p+'">用户中心</a></li> ' +
            '<li role="separator" class="divider"></li>' +
            '<li><a href="#">其他</a></li>' +
            '<li role="separator" class="divider"></li>' +
            '<li><a href="/user/logout" id="nav-cancel" >退出</a></li>' +
            '</ul>';
            //给父级标签增加下拉菜单属性
        $('#nav-login').parent().addClass('dropdown');
        $('#nav-login').replaceWith(v1);

        //替换注册标签为

        var v2='<a href="'+p+'">用户中心</a>';
        $('#nav-regist').replaceWith(v2);
        //去除模态框
        $('#login-1').modal('hide');
        //为了防止用填过的值再注册的事件发生，重置下面这些值，因为当前这些值都为true。
        error_name = false;
        error_password = false;
        error_check_password = false;
        error_email = false;
        error_check = true;//协议默认是勾选的
        //为了防止登录过后验证值改变，将其改为初始状态
        login_uname=false;
        login_upwd=false;

        // location.reload() //刷新该网页，这个很费流量哦
    }else{
        console.log('12');
        var v=data.error;
        $('.form-tip').removeClass('hidden').children().html(v)
    }
}
//微信扫码登录的函数
function login_wx() {

    //清空模态框登录和注册标签的active
    $('#login-btn,#regist-btn').removeClass('active');
    //隐藏模态框登录和注册form
    $('#login-form,#reg-form').addClass('hide');
    //清除上次加载的二维码图片和提示
    $('#wx-load').remove();
    $('#wxtip').remove();
    //弹出扫码框，加载二维码
    $.ajax({
            url:'/user/login_wx/',
            type:'GET',
            dataType:'json',
            success:function (data) {
                //定义二维码图片
                var tag='<img id="wx-load" width="270px" height="270px" style="position:relative;left:50%;margin-left:-135px" ' +
                    'src="https://login.weixin.qq.com/qrcode/'+data.code+'">';
                //加入到
                $('.modal-body').append(tag);
                //在模态框footer中加入提示
                var wxtip='<div id="wxtip" style="float: right;display: inline-block" class="clearfix" ><span>扫码表示您已同意</span><a  href="#">瓷画网用户使用协议</a></div>';
                $('.modal-footer').append(wxtip)
            }
        });


}
//当模态框隐藏的时候，要清除微信，不然，老在加载
function cancel_wx() {
    //当模态框完全对用户隐藏时触发。
    $('#login-1').on('hidden.bs.modal', function () {
        //执行一些动作...
        //清除加载的二维码图片和提示
        $('#wx-load').remove();
        $('#wxtip').remove();

    })
}
//长轮询函数：根据状态码，用递归方式实现长轮询pending
function polling() {
    console.log(6+'轮询');
    //ajax方式实现长轮询,不发送数据,访问轮询函数
    $.ajax({
        url:'/user/polling_wx/',
        type:'GET',
        dataType:'json',
        success:function (data) {
            console.log('收到数据');
            if(data.status==408){
                console.log(1+'等待手机扫描');
                //等待手机扫描二维码,轮询
                console.log(data.status);
                //如果二维码图片不存在就退出，避免点击后，还在轮询，浪费带宽
                console.log('二维码图片'+$('#wx-load').length);
                if ($('#wx-load').length===1 ){
                    console.log(7+'');
                    polling()//递归
                }else{
                    console.log(8+'退出，结束轮询');
                    return
                }

            }else if(data.status==201){
                //已经扫描二维码，获取头像，等待手机确认，轮询
                console.log(2+'已扫描，获取头像');
                //获取头像
                if ($('#wx-load').length===1){
                    console.log(9);
                    $('#wx-load').attr('src',data.src);
                    $('#wx-load').attr('width','100px');
                    $('#wx-load').attr('height','100px');
                    $('#wx-load').css('margin-left','-50px');
                    polling()//递归
                }else{
                    console.log(10+'退出，结束轮询');
                    return
                }

            }else if(data.status){
                //手机已经确认，这时状态码应该为data.status=True，获得用户名和密码，实现页面更新
                console.log(3+'手机已确认，结束轮询');
                //如果是第一次，会传过来用户名和密码，显示密码和用户名
                if(data.username){
                    var username=data.username;
                    var upwd=data.upwd;
                    alert('恭喜您通过验证，请记住您的账号为'+username+' 密码为'+upwd+' , 不方便扫码登录时，可以使用账号和密码登录');
                }

                success_call(data);

                //结束轮询
                return
                // window.location.href='/'
            }else{
                //异常 结束
                console.log(4+'异常结束轮询');
                return false


            }
        }

    })
}