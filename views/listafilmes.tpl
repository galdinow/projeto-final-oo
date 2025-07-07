<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Todos os Filmes</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Agbalumo&display=swap" rel="stylesheet">
    
    <style>
        body {
            background-color: #1B2B30;
            color: #ffffff;
        }
        .movie-card img {
            width: 100%;
            height: 350px;
            object-fit: cover;
            border-radius: 10px;
            transition: transform 0.3s;
        }
        .movie-card img:hover {
            transform: scale(1.05);
        }
        h2 {
        font-family: 'Agbalumo', cursive;
        }
        

    </style>
</head>
<body>

<div class="container mt-5 pb-5">
    <h2 class="mb-4">Catálogo de Filmes</h2>
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-5 g-4">
        % for filme in filmes:
            <div class="col movie-card">
                <a href="/movie/{{filme['id']}}">
                    <img src="{{filme['img_url']}}" alt="{{filme['title']}}">
                </a>
            </div>
        % end
    </div>
</div>

</body>
</html>
