<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>login</title>
</head>
<body>
<h1>Usuario novo?</h1>

<form action="/cadastro-usuario" method="post">
    <div>
    <label for="username">Username</label>
    <input type="text" id="username" placeholder="Username" required>
    </div>

    <div>
    <label for="email">Email</label>
    <input type="email" id="email" placeholder="firstname@gmail.com" required>
    </div>

    <div>
    <label for="password">Password</label>
    <input type="password" id="password" placeholder="123456789" required>
    </div>

    <div>
        <input type="submit">
    </div>
</form>
</body>
</html>