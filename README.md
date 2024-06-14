<h1>Automessager</h1>
<p>Pequeno protótipo para mandar mensagens automaticamente para o twitter</p>

<h2>Como usar</h2>
<ol>
  <li>Instale a versão mais recente do Python com e com o package manager (pip)</li>
  <li>rode o comando pelo terminal, na pasta raiz do projeto <code>pip install -r requirements</code></li>
  <li><a href="https://developer.x.com/en">Crie uma conta de desenvolvedor do Twitter</a> e crie um app Free Tier.</li>
  <li><a href="https://youtu.be/fBFQMp0m41E?si=YEyJGFQc7ayRozAw">Veja esse video para saber como fazer o setup do seu Webhook/App</a></li>
  <li>Dentro do arquivo <code>sender.py</code>, substitua os valores das variáveis em caixa alta de acordo com as informações abaixo: 
    <ul>
      <li> COOMER_KEY = Api Key</li>
      <li> COOMER_SECRET = Api Secret</li>
      <li> BEARER_TOKEN = Bearer Token</li>
      <li> ACCESS_TOKEN = Access Token</li>
      <li> ACCESS_SECRET = Access Secret</li>
    </ul> 
  </li>
</ol>
<p>Caso quiser adicionar novos Tweets: <code>python dbMan.py</code>, o runtime (aquele que vai rodar 24/7) é <code>python sender.py</code>.</p>
:)
