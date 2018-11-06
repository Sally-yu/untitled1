
			function check() {
				var pas = $('#passwd').val();
				var pas1 = $('#passwd1').val();
				if(pas != pas1) {
					alert('密码不相同');
					return false;
				} 
				else {
					return true;
				}
			}
