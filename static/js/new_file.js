function getCookie(name) {
	var cookieValue = null;
	if(document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for(var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if(cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

$('document').ready(function() {

	var E = window.wangEditor;
	var editor1 = new E('#div1', '#div2'); // 只传一个参数生成菜单编辑器合体的编辑器
	//			var text1 = $('#text1');

	//			editor1.customConfig.onchange = function(html) {
	//				// 监控变化，同步更新到 textarea
	//				text1.val(html);
	//			}
	editor1.customConfig.onchangeTimeout = 10; //内容变化触发的的延时，默认200ms

	//默认的菜单按钮
	editor1.customConfig.menus = [
		'head', // 标题
		'bold', // 粗体
		'fontSize', // 字号
		'fontName', // 字体
		'italic', // 斜体
		'underline', // 下划线
		'strikeThrough', // 删除线
		'foreColor', // 文字颜色
		'backColor', // 背景颜色
		'link', // 插入链接
		'list', // 列表
		'justify', // 对齐方式
		'quote', // 引用
		'emoticon', // 表情
		'image', // 插入图片
		'table', // 表格
		'video', // 插入视频
		'code', // 插入代码
		'undo', // 撤销
		'redo' // 重复
	];
	//粘贴时保留样式
	editor1.customConfig.pasteFilterStyle = false
	//表情
	editor1.customConfig.emotions = [{
			// tab 的标题
			title: '默认',
			// type -> 'emoji' / 'image'
			type: 'image',
			// content -> 数组
			content: [{
					alt: '[坏笑]',
					src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/50/pcmoren_huaixiao_org.png'
				},
				{
					alt: '[舔屏]',
					src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/40/pcmoren_tian_org.png'
				}
			]
		},
		{
			// tab 的标题
			title: 'emoji',
			// type -> 'emoji' / 'image'
			type: 'emoji',
			// content -> 数组
			content: ['👿', '😃', '😄', '😁', '😆']
		}
	]
	//上传图片tab 二选一不可同时使用
	editor1.customConfig.uploadImgShowBase64 = true // 使用 base64 保存图片
	// editor.customConfig.uploadImgServer = '/upload'  // 上传图片到服务器

	editor1.create();
	//      editor1.txt.html('<p>追加的内容</p>')//较慢的内容赋值方法
	$('#div2>div>p').remove(); //生成编辑器后最后一行为br回车 直接追加有空行
	editor1.txt.append('<p>追加的内容</p>');
	editor1.txt.append('<p>追加的内容</p>'); //追加的内容
	//		editor1.$textElem.attr('contenteditable', true) //编辑器可用
	// 初始化 textarea 的值
	//			text1.val(editor1.txt.html());

	$('#btn1').click(function() {
		alert(editor1.txt.html());
	});
	$('#btn2').click(function() {
		alert(editor1.txt.text());
	});
	
	
	$('#json').click(function() {
		alert('111');
		url='foo';
		$.get(url, function(callback) {
			alert(callback);
		});
	});
	$('#post').click(function() {
		var csrftoken = getCookie('csrftoken');
		var username = 'yu';
		var password = 'aaaaaa';
		url='/Demo/post';
		$.ajax({
			cache: false,
			type: "POST",
			url: url,
			dataType: 'json',
			async: true,
			data: {
				username: username, //用户名
				password: password //密码
			},
			success: function(data) {
				
			},
			beforeSend: function(xhr, settings) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		});
	});
	
	$('#subumit').click(function(){
		var title=$('#title').val();
		if(title==''||title==null){
			alert('当前文章无标题');
			return;
		}
		if(editor1.txt.text()==''||editor1.txt.text()==null){
			alert('当前文章无内容');
			return;
		}
		var csrftoken = getCookie('csrftoken');
		var content=editor1.txt.html();
		data={
			content:content,
			title:title
		}
		url='/Demo/savenews';
		$.ajax({
			cache:false,
			type:'POST',
			url:url,
			dataType:'json',
			async:true,
			data:data,
			success:function(res){
				flag=res['result'];
				alert(flag);
			},
			beforeSend:function(xhr,settings){
				xhr.setRequestHeader("X-CSRFToken",csrftoken);
			}
		});
	});
});