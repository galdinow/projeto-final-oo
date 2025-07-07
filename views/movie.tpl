
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{filme["title"]}}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic" rel="stylesheet" type="text/css" />
    <link href="https://fonts.googleapis.com/css2?family=Agbalumo&display=swap" rel="stylesheet">

    <style>
        body {
            background-color: #1B2B30;
            color: #ffffff;
            font-family: 'Merriweather', sans-serif;
        }
        .filme-img {
            max-width: 100%;
            border-radius: 10px;
        }
        .estrela-btn {
            font-size: 1.5rem;
            margin: 0 2px;
        }
        body, .form-label, .form-control {
        font-family: "Merriweather", sans-serif;
        }
        h1 {
        font-family: 'Agbalumo', cursive;
        }
    </style>
</head>
<body>

<div class="container mt-5">
    <div class="row">
        
        <div class="col-md-4">
            <img src="{{filme['img_url']}}" alt="Capa do Filme" class="filme-img">

            <!-- Média das avaliações -->
            <div class="mt-3">
    {% if filme['media_avaliacoes'] is not None %}
        <h5>Média de avaliações:</h5>
        <p class="fs-4">
            {{ filme['media_avaliacoes'] }} ★ ({{ filme['num_avaliacoes'] }} avaliações)
        </p>
    {% else %}
        <p class="text-muted">Este filme ainda não foi avaliado.</p>
    {% endif %}
</div>
        </div>

        
        <div class="col-md-8">
            <h1>{{filme['title']}}</h1>
            <p>{{filme['description']}}</p>

            <form action="/avaliar-filme" method="POST" class="mt-4">
    <input type="hidden" name="filme_id" value="{{filme['id']}}">

    <p>Avalie este filme:</p>
    
    % for i in range(1, 6):
    <button type="submit" name="nota" value="{{i}}" class="btn btn-warning estrela-btn">
        {{'★' * i}}
    </button>
% end

    </form>
        </div>
    </div>
</div>

</body>
</html>
