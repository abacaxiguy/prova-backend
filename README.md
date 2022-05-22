<br>
<div align="center">
  <p>
    <img alt="LCCV Logo" src="./img/Logo.png" height="200" />
  </p>

# Projeto Sumé LCCV (Vaga Back-end) - Edital 3/2022

</div>

<p align="center">
  <img alt="Last Commit" src="https://img.shields.io/github/last-commit/abacaxiguy/prova-backend" />
  <img alt="License" src="https://img.shields.io/github/license/abacaxiguy/prova-backend" />
  <a href="https://github.com/abacaxiguy" target="_blank"><img alt="Follow Me" src="https://img.shields.io/github/followers/abacaxiguy.svg?style=social&label=Follow&maxAge=2592000" /></a>
</p>

---

## 🌎 Online!

Essa [api está no ar](https://abacaxiguy-lccv.ml) neste momento!<br>
Deploy feito na [Digital Ocean 🌊](https://www.digitalocean.com/) com Gunicorn 🦄 e Nginx 🟩!

Se você quiser entrar na área administrativa desse servidor,<br>

<details>
  <summary><b>As credenciais são essas:</b></summary>

```
Usuário: admin
Senha: root12345
```

</details>

<details>
  <summary><b>Confira aqui as rotas da api:</b></summary>

<br>

-   [/admin](https://abacaxiguy-lccv.ml/admin)<br>
-   [/api/ufs](https://abacaxiguy-lccv.ml/api/ufs)<br>
-   [/api/cidades](https://abacaxiguy-lccv.ml/api/cidades)<br>
-   [/api/enderecos](https://abacaxiguy-lccv.ml/api/enderecos)<br>
-   [/api/pessoas](https://abacaxiguy-lccv.ml/api/pessoas)<br>
-   [/api/ocorrencias](https://abacaxiguy-lccv.ml/api/ocorrencias)<br>
-   [/api/contas](https://abacaxiguy-lccv.ml/api/contas)<br>
-   [/api/users](https://abacaxiguy-lccv.ml/api/users)

<br>

</details>

---

## 🛠️ Requisitos

-   Docker Compose
-   Docker Engine ou Docker Desktop

---

## 🚀 Modo de uso

Primeiramente, estabeleça suas credenciais no arquivo `.env`, tendo base no [.env_example](.env_example).

Após criado, rode o Docker Compose:

```
  docker-compose up -d --build
```

Quando criado a imagem, rode:

```
  docker-compose up --build
```

E pronto 🥳️! Seu docker foi inicializado e está rodando em http://localhost:8000/api/

---

## 📋 Documentação da API

-   [Insomnia](insomnia.json) 🧿️

---

## 📝 Licença

Copyright © 2022 [João Lucas](https://github.com/abacaxiguy).<br />
Este projeto é licenciado pelo [MIT](https://github.com/abacaxiguy/prova-backend/blob/master/LICENSE).

---

## 🧪 Testado em

-   Linux [Ubuntu 22.04 LTS] ☑️

---

<h4  align="center">Developed by 🍍</h4>
