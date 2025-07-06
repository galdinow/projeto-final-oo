% rebase("base.tpl", title="login")

<h1>Usuario novo?</h1>

<form action="/login" method="post">
    <div>
    <label for="username">Username</label>
    <input type="text" id="username" placeholder="Username" name="username" required>
    </div>

    <div>
    <label for="email">Email</label>
    <input type="email" id="email" placeholder="firstname@gmail.com"  name="email" required>
    </div>

    <div>
    <label for="password">Password</label>
    <input type="password" id="password" placeholder="123456789" name="password" required>
    </div>

    <div>
        <input type="submit">
    </div>
</form>

<p>Ja possui uma conta?</p>
<a href="/logon">Entrar</a>
