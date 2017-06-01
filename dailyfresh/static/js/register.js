$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;


	$('#user_name').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_user_name(){
		var len = $('#user_name').val().length;
		if(len<5||len>20)
		{
			$('#user_name').next().html('请输入5-20个字符的用户名')
			$('#user_name').next().show();
			error_name = true;
		}
		else
		{
			// 利用ajax查询数据库是否存在该用户名
			$.get('/user/register_exist/', {'user_name':$('#user_name').val()}, function (data) {
				if (data.count == 1){
					$('#user_name').next().html('用户名已存在');
					$('#user_name').next().show();
					error_name = true;
					// alert(error_name);
				}else{
					$('#user_name').next().hide();
					error_name = false;
				}

            })

		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致')
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
			error_check_password = true;
		}

	}


	$('#reg_form').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
		{

			//在js中使用ajax提交会报403错误,无法通过csrf验证,需要在模板中添加一段js代码
			var user_name  = $('#user_name').val();
			var pwd = $('#pwd').val();
			var cpwd = $('#cpwd').val();
			var email = $('#email').val();

			var data_send = {'user_name':user_name,'pwd':pwd,'cpwd':cpwd,'email':email};
			$.post('/user/register_handle/',data_send,function (redirect_info) {
				// 通过ajax传递数据执行的这条url重定向的结果并没有返回给浏览器,而是通过function()来接收
				//　这里并没有接收
				alert("注册成功！");
				//location.href=redirect_info.redirect;
				window.location.href=redirect_info.redirect;

			});

			// 阻止默认form表单提交
			return false;
		}
		else
		{
			return false;
		}

	});




})