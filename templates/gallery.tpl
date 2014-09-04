<!DOCTYPE>
<html>
<head>
    <title>Gallery</title>
</head>
<body>
	<h1>Pictures</h1>
    <ul id="navigation">
    {% for item in navigation %}
    	<img src="{{ item }}.img" alt="{{item}}" height="100" width="100">
    {% endfor %}
    </ul>
</body>
</html>