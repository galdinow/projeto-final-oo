% rebase("base.tpl", title="Login")

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Cadastro de Usuário</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Agbalumo&display=swap" rel="stylesheet">
    <style>
        body, .form-label, .form-control, .btn {
            font-family: "Merriweather", sans-serif;
        }
        h2 {
            font-family: 'Agbalumo', cursive;
        }
        body {
            background-color: #1B2B30;
            color: #ffffff;
        }
        .custom-btn {
            background-color: #337988;
            color: white;
            border: none;
        }
        .custom-btn:hover {
            background-color: #194f5b;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <h2 class="mb-4">Cadastrar Novo Usuário</h2>
        <form action="/login" method="post">
            <div class="mb-3">
                <label for="username" class="form-label">Usuário</label>
                <input type="text" id="username" name="username" class="form-control" placeholder="Seu nome de usuário" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" id="email" name="email" class="form-control" placeholder="seunome@email.com" required>
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Senha</label>
                <input type="password" id="password" name="password" class="form-control" placeholder="********" required>
            </div>
            <button type="submit" class="btn custom-btn">Cadastrar</button>
        </form>
        <p class="mt-3">Já possui uma conta? <a href="/logon" class="text-info">Entrar</a></p>
    </div>
</body>
</html>
