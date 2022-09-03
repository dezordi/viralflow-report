from pkg_resources import resource_filename

CSS = resource_filename(__name__, 'css/style.css')

HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<link href="css/style.css" rel="stylesheet">
<title>ViralFlow</title>
</head>
<body>
<main>
    <div class="container"> 
        <h1>ViralFlow HTML results</h1>
"""

FOOTER = """    </div>
</main>
</body>
</html>
"""