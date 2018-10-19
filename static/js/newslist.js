//CSRFToken 
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

function LocalTime(utc){
	var time=new Date(utc);
	return time.toLocaleString();
}

$('document').ready(function() {
	$('#load-data').click(function(){
	var url = 'newslist/2018';//相对与项目根路径
	$.get(
		url,
		function(res) {
			alert(res);
			var table=JSON.parse(res);
			$.each(table, function(index,row) {
				var title=row['fields']['title'];
				var pubTime=LocalTime(row['fields']['pubTime']);
				var modifyTime=LocalTime(row['fields']['modifyTime']);
				$('#news_table').append(
					"<tr><th>"+title+"</th><th>"+pubTime+"</th><th>"+modifyTime+"</th></tr>"
				);
			});
		}
	);
	});
});