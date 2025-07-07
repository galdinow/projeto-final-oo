<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Trabalho Final OO</title>
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <!-- Bootstrap Icons-->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <!-- Google fonts-->
        <link href="https://fonts.googleapis.com/css?family=Merriweather+Sans:400,700" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic" rel="stylesheet" type="text/css" />
        <!-- SimpleLightbox plugin CSS-->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.css" rel="stylesheet" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="/static/css/styles.css" rel="stylesheet" />
        <link href="https://fonts.googleapis.com/css2?family=Agbalumo&display=swap" rel="stylesheet">

    </head>
    <body id="page-top" style="background-color: #1B2B30;">
        <!-- Navigation-->
        <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="#page-top">Trabalho OO</a>
                <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto my-2 my-lg-0">
                        <li class="nav-item"><a class="nav-link" href="/login">Entrar</a></li>
                        <li class="nav-item"><a class="nav-link" href="/cadastrofilme">Cadastrar um Filme</a></li>
                        <li class="nav-item"><a class="nav-link" href="/listafilmes">Filmes</a></li>
                        <li class="nav-item"><a class="nav-link" href="perfil.tpl">Perfil</a></li>
                       
                    </ul>
                </div>
            </div>
        </nav>
        <!-- Masthead-->
        <header class="masthead">
            <div class="container px-4 px-lg-5 h-100">
                <div class="row gx-4 gx-lg-5 h-100 align-items-center justify-content-center text-center">
                    <div class="col-lg-8 align-self-end">
                        <h1 class="text-white font-weight-bold">CineView</h1>
                        <hr class="divider" />
                    </div>
                    <div class="col-lg-8 align-self-baseline">
                        <p class="text-white-75 mb-5">Um espaço para amantes do cinema registrarem o que assistiram, recomendarem filmes e trocarem experiências.</p>
                        <a class="btn btn-primary btn-xl" href="/login">Cadastre-se!</a>
                    </div>
                </div>
            </div>
        </header>

        <div class="container mt-5">
  <div class="row justify-content-center g-4">
    
    <div class="col-md-4">
      <div class="card" style="width: 100%;">
        <img src="\static\img\howlc.jpg" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">O Castelo Animado</h5>
          <p class="card-text">Studio Ghibli</p>
          <a href="/movie/7142" class="btn btn-primary">Ver mais</a>
        </div>
      </div>
    </div>

    <div class="col-md-4">
      <div class="card" style="width: 100%;">
        <img src="/static/img/ponyo.jpg" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Ponyo</h5>
          <p class="card-text">Studio Ghibli</p>
          <a href="/movie/1344" class="btn btn-primary">Ver mais</a>
        </div>
      </div>
    </div>

    <div class="col-md-4">
      <div class="card" style="width: 100%;">
        <img src="/static/img/myntotoro.jpg" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Meu Amigo Totoro</h5>
          <p class="card-text">Studio Ghibli</p>
          <a href="/movie/6778" class="btn btn-primary">Ver mais</a>
        </div>
      </div>
    </div>

  </div>
</div>

        
        <section class="page-section" id="serviços">
            <div class="container px-4 px-lg-5">
                <h2 class="text-center mt-0">Ao Seu Serviço</h2>
                <hr class="divider" />
                <div class="row gx-4 gx-lg-5">
                    <div class="col-lg-3 col-md-6 text-center">
                        <div class="mt-5">
                            <div class="mb-2"><i class="bi bi-star fs-1 text-white"></i></div>
                            <h3 class="h4 mb-2">Avalie Filmes</h3>
                            <p class="text-muted mb-0">Compartilhe sua opinião com o mundo dando notas e escrevendo comentários sobre os filmes que você assiste.</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 text-center">
                        <div class="mt-5">
                            <div class="mb-2"><i class="bi bi-camera-reels-fill fs-1 text-white"></i></div>
                            <h3 class="h4 mb-2">Descubra Novos Títulos</h3>
                            <p class="text-muted mb-0">Navegue pelos filmes cadastrados por outros usuários e encontre sugestões para sua próxima sessão de cinema.</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 text-center">
                        <div class="mt-5">
                            <div class="mb-2"><i class="bi bi-tv-fill fs-1 text-white"></i></div>
                            <h3 class="h4 mb-2">Cadastre Filmes</h3>
                            <p class="text-muted mb-0">Adicione novos filmes à plataforma com título, descrição, diretor e imagem. Deixe o catálogo sempre atualizado!</p>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 text-center">
                        <div class="mt-5">
                            <div class="mb-2"><i class="bi-heart fs-1 text-white"></i></div>
                            <h3 class="h4 mb-2">Veja Avaliações da Comunidade</h3>
                            <p class="text-muted mb-0">Confira o que outros usuários acharam dos filmes, com notas médias e comentários relevantes.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        
        
        


        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- SimpleLightbox plugin JS-->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/SimpleLightbox/2.1.0/simpleLightbox.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
        <!-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *-->
        <!-- * *                               SB Forms JS                               * *-->
        <!-- * * Activate your form at https://startbootstrap.com/solution/contact-forms * *-->
        <!-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *-->
        <script src="https://cdn.startbootstrap.com/sb-forms-latest.js"></script>
    </body>
</html>
