<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{filme.title}}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #1B2B30;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }
        .filme-img {
            max-width: 100%;
            border-radius: 10px;
        }
        .estrela-btn {
            font-size: 1.5rem;
            margin: 0 2px;
        }
    </style>
</head>
<body>

<div class="container mt-5">
    <div class="row">
        <!-- 1/3: Imagem -->
        <div class="col-md-4">
            <img src="{{filme.img_url}}" alt="Capa do Filme" class="filme-img">

            <!-- Média das avaliações -->
            <div class="mt-3">
                {% if filme.avaliacoes and len(filme.avaliacoes) > 0 %}
                    <h5>Média de avaliações:</h5>
                    <p class="fs-4">
                        {{ "%.1f"|format(sum(filme.avaliacoes) / len(filme.avaliacoes)) }} ★ ({{ len(filme.avaliacoes) }} avaliações)
                    </p>
                {% else %}
                    <p class="text-muted">Este filme ainda não foi avaliado.</p>
                {% end %}
            </div>
        </div>

        <!-- 2/3: Título, descrição e avaliação -->
        <div class="col-md-8">
            <h1>{{filme.title}}</h1>
            <p>{{filme.description}}</p>

            <form action="/avaliar-filme" method="POST" class="mt-4">
                <input type="hidden" name="filme_id" value="{{filme.id}}">

                <p>Avalie este filme:</p>
                {% for i in range(1, 6) %}
                    <button type="submit" name="nota" value="{{i}}" class="btn btn-warning estrela-btn">
                        {{'★' * i}}
                    </button>
                {% end %}
            </form>
        </div>
    </div>
</div>

</body>
</html>
