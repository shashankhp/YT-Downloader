<!DOCTYPE html>


<head>
    <link href="../static/main.css" rel="stylesheet" type="text/CSS">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <link rel="preconnect" href="https://fonts.gstatic.com">
 	<link href="https://fonts.googleapis.com/css2?family=Cabin:wght@500&display=swap" rel="stylesheet">
</head>



<body>
{% with messages = get_flashed_messages() %}
	{% if messages %}
		{% for msg in messages %}
			<p id= "mess">{{msg}}</p>
		{% endfor %}
	{% endif %}
{% endwith %}

  <form action="#" method="post">
    <p id="title"><label> Enter the YouTube Link </label></p>
    <p id="link" ><input type="text" name="link"></p>
    <p id="sub" > <input type="submit" value="Submit"></p>
  </form>
</body> 
