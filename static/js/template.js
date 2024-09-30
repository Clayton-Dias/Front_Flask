$(document).ready(function() {
    // Inicializa a aplicação quando o documento estiver pronto
    runApp();
});

function runApp() {
    // Ajusta o menu ao carregar a página
    resizeMenu();

    // Ajusta o menu ao redimensionar a janela
    $(window).resize(resizeMenu);

    // Alterna a visibilidade do menu ao clicar no botão
    $('#toggleMenu').click(toggleMenu);
}

function resizeMenu() {
    // Mostra ou esconde o menu com base na largura da janela
    if (window.innerWidth >= 600) {
        showMenu(true);
    } else {
        hideMenu();
    }
}

function toggleMenu() {
    // Alterna a visibilidade do menu ao clicar no botão
    if ($('#wrap>nav').is(':visible')) {
        hideMenu();
    } else {
        showMenu();
    }
    return false; // Previne o comportamento padrão do clique
}

function showMenu(noSmoke) {
    // Mostra o menu
    $('#wrap>nav').show('fast');

    if (noSmoke) {
        // Esconde o fundo escuro e permite rolagem
        $('#menuSmoke').hide('fast');
        $('body').css('overflow', 'auto');
    } else {
        // Mostra o fundo escuro e desabilita rolagem
        $('#menuSmoke').show('fast');
        $('body').css('overflow', 'hidden');
    }
}

function hideMenu() {
    // Esconde o menu e o fundo escuro, permite rolagem
    $('#wrap>nav').hide('fast');
    $('#menuSmoke').hide('fast');
    $('body').css('overflow', 'auto');
}


/*
Comentado e Otimizado pelo chatGPT

$(document).ready(function() {
    // Inicializa o aplicativo e configura os eventos
    
    initApp();
});

const $nav = $('#wrap>nav');

function initApp() {
    // Ajusta o menu conforme o tamanho da janela
    resizeMenu();

    // Adiciona um listener para o redimensionamento da janela
    $(window).resize(resizeMenu);

    // Adiciona um listener para o clique no botão de alternar menu
    $('#toggleMenu').click(toggleMenu);
}

function resizeMenu() {
    // Exibe ou oculta o menu com base na largura da janela
    if (window.innerWidth >= 600) {
        showMenu(true);
    } else {
        hideMenu();
    }
}

function toggleMenu() {
    // Alterna a visibilidade do menu
    
    if ($nav.is(':visible')) {
        hideMenu();
    } else {
        showMenu();
    }
    return false; // Impede o comportamento padrão do clique
}

function showMenu(noSmoke) {
    // Exibe o menu e ajusta o estilo de acordo com a necessidade
    $($nav).show('fast');

    if (noSmoke) {
        $('#menuSmoke').hide('fast');
        $('body').css('overflow', 'auto');
    } else {
        $('#menuSmoke').show('fast');
        $('body').css('overflow', 'hidden');
    }
}

function hideMenu() {
    // Oculta o menu e o efeito de fumaça, e restaura o overflow da página
    $($nav).hide('fast');
    $('#menuSmoke').hide('fast');
    $('body').css('overflow', 'auto');
} 
    
*Melhorias e Comentários:
*Função initApp: Renomou runApp para initApp para refletir melhor o propósito da função, que é inicializar o aplicativo e configurar os eventos.
*
*Otimização de Seletores: Utilizou a variável const $nav para evitar múltiplas chamadas ao jQuery para o mesmo elemento.
*
*Comentários: Adicionou comentários para explicar o propósito de cada função e alguns detalhes sobre o que cada bloco de código faz.
*
*Impedir Comportamento Padrão: Manteve o return false no final da função toggleMenu para garantir que o clique não siga o comportamento padrão (por exemplo, se o botão for um link).
*
*Encapsulamento de Código: Manteve o código organizado e agrupado para melhorar a legibilidade e manutenção.
*
*/