<h1>Automessager</h1>
<p>Pequeno script para mandar mensagens automaticamente para o twitter</p>

<h2>Como usar</h2>
<ol>
  <li>Instale a versão mais recente do Python com e com o package manager (pip)</li>
  <li>Rode o comando pelo terminal, na pasta raiz do projeto <code>pip install -r requirements</code></li>
  <li><a href="https://developer.x.com/en">Crie uma conta de desenvolvedor do Twitter</a> e crie um app Free Tier.</li>
  <li><a href="https://youtu.be/fBFQMp0m41E?si=YEyJGFQc7ayRozAw">Veja esse video para saber como fazer o setup do seu Webhook/App</a></li>
  <li>Crie uma imagem, usando o <code>containerfile</code> no podman desktop</li>
  <li>Edite o arquivo <code>env</code> de acordo com as informações abaixo:
    <ul>
      <li> COOMER_KEY=Api Key</li>
      <li> COOMER_SECRET=Api Secret</li>
      <li> BEARER_TOKEN=Bearer Token</li>
      <li> ACCESS_TOKEN=Access Token</li>
      <li> ACCESS_SECRET=Access Secret</li>
    </ul> 
  </li>
  <li>No podman desktop (ou em algum programa semelhante) crie uma um container, passando o seu arquivo editado <code>env</code> como arquivo de variáveis de ambiente</li>
</ol>
:)
