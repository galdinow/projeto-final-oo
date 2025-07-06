<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Cadastrar Filme</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic" rel="stylesheet" type="text/css" />
    <link href="https://fonts.googleapis.com/css2?family=Agbalumo&display=swap" rel="stylesheet">

    <style>
        body, .form-label, .form-control, .btn {
        font-family: "Merriweather", sans-serif;
        }
        h2 {
        font-family: 'Agbalumo', cursive;
        }
        body {
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
<body class="" style="background-color: #1B2B30;">
    <div class="container mt-5">
        <h2 class="mb-4">Cadastrar Novo Filme</h2>
        <form action="/cadastrofilme" method="POST">
            <div class="mb-3">
                <label class="form-label">Título</label>
                <input type="text" name="title" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Descrição</label>
                <textarea name="description" class="form-control" rows="3" required></textarea>
            </div>
            <div class="mb-3">
                <label class="form-label">Diretor</label>
                <input type="text" name="director" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">URL da Imagem</label>
                <input type="text" name="img_url" class="form-control" placeholder="/static/img/exemplo.jpg" required>
            </div>
            <button type="submit" class="btn custom-btn">Cadastrar</button>
        </form>
    </div>
</body>
</html>
