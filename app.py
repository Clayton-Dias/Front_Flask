from flask import Flask, render_template

# Inicializa a aplicação Flask
app = Flask(__name__)

# Dicionário com informações do site
SITE = {
    "name": "Blog Front",  # Nome do site
    "css": "/static/css/template.css",  # Caminho para o CSS
    "js": "/static/js/template.js",  # Caminho para o JS
    "logo": "/static/img/logo.png",  # Caminho para o logo
    # HTML para o botão de menu
    "toogle": '''  
                <span id="toogleMenu"> 
                <i class="fa-solid fa-bars fa-fw"></i> 
                </span> 
            ''',
    # Formulário de busca
    "busca": '''
            <form action="search.html" method="get">
                <input type="search" name="q" id="headerSearch" placeholder="Digite para pesquisar">
                <button type="submit" title="Clique para iniciar a busca">
                    <i class="fa-solid fa-magnifying-glass" fa-fw></i>
                </button>
            </form>
            ''',
    # Menu de navegação
    "menu": {
        "home": '''
                <a href="/" title="Página Inical">
                    <i class="fa-solid fa-house fa-fw"></i>
                    <span>Início</span>
                </a>
            ''',
        "contato": '''
                <a href="/contacts" title="Entre em contato conosco">
                    <i class="fa-solid fa-headset fa-fw"></i>
                    <span>Contatos</span>
                </a>
            ''',
        "sobre": '''
                <a href="/about" title="Informações sobre quem somos">
                    <i class="fa-solid fa-circle-info fa-fw"></i>
                    <span>Sobre</span>
                </a>
            '''
    },
    # Rodapé do site
    "footer": {
        "license": '''
                <div title="Você pode copiar e reutilizar este conteúdo livremente.">
                    <i class="fa-regular fa-copyright fa-flip-horizontal"></i> Copyleft 2024 - Clayton
                </div>
        ''',
        "top": '''
                <a href="#wrap" title="Ir para o topo da página">
                    <i class="fa-solid fa-turn-up fa-fw"></i>
                </a>
        ''',
    },
    # Links das redes sociais
    "redesSociais": {
        "facebook": '''  
                    <a href="https://facebook.com" target="_blank" rel="noopener">
                            <i class="fa-brands fa-facebook fa-fw"></i>
                            <span>Facebook</span>
                    </a>
                ''',
        "x": '''  
            <a href="https://x.com" target="_blank" rel="noopener">
                <i class="fa-brands fa-x-twitter fa-fw"></i>
                <span>Twitter</span>
            </a>
        ''',
        "github": '''  
                <a href="https://github.com" target="_blank" rel="noopener">
                    <i class="fa-brands fa-github fa-fw"></i>
                    <span>Github</span>
                </a>
        '''
    },
    # Links adicionais
    "links": {
        "politica": '''  
                    <a href="/policies">
                        <i class="fa-solid fa-book fa-fw"></i>
                        <span>Políticas</span>
                    </a>
                '''
    }
}

# Rota para a página inicial
@app.route('/')
def home():
    toPage = {
        "site": SITE,
        "title": "Página Inicial",  # Título da página
        "css": "home.css",  # CSS específico da página
    }
    return render_template("home.html", page=toPage)  # Renderiza o template

# Rota para a página "Sobre"
@app.route('/about')
def about():
    toPage = {
        "site": SITE,
        "title": "Quem somos",  # Título da página
        "css": "about.css",  # CSS específico da página
    }
    return render_template("about.html", page=toPage)  # Renderiza o template

# Rota para a página de políticas
@app.route("/policies")
def policies():
    toPage = {
        "site": SITE,
        "title": "Política de Privacidade",  # Título da página
        "css": "policies.css",  # CSS específico da página
    }
    return render_template("policies.html", page=toPage)  # Renderiza o template

# Rota para a página de contato
@app.route("/contacts")
def contact():
    toPage = {
        "site": SITE,
        "title": "Faça contato",  # Título da página
        "css": "contacts.css",  # CSS específico da página
        "qrcode": "/static/img/qrcode.png",  # QR Code
        "redeSocial": '''  # Links para redes sociais
                <a href="https://facebook.com" target="_blank">
                    <i class="fa-brands fa-facebook fa-fw fa-3x" style=" color: #1877f2;"></i>
                </a>
                <a href="https://x.com" target="_blank">
                    <i class="fa-brands fa-x-twitter fa-fw fa-3x" style="color: #14171a;"></i>
                </a>
                <a href="https://github.com" target="_blank">
                    <i class="fa-brands fa-github fa-fw fa-3x" style="color: #6e5494;"></i>
                </a>
                <a href="https://www.instagram.com/" target="_blank" style="color: #c13584;">
                    <i class="fa-brands fa-square-instagram fa-fw fa-3x"></i>
                </a>        
        ''',
    }
    return render_template("contacts.html", page=toPage)  # Renderiza o template

# Tratamento de erros 404 (página não encontrada)
@app.errorhandler(404)
def errors(e):
    return "Página não encontrada."  # Mensagem de erro

# Inicia a aplicação Flask em modo de depuração
if __name__ == '__main__':
    app.run(debug=True)
