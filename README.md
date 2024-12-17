# 1I-PSI-M3-14687-EXPA04
<h1>Descrição do Código - Sistema de Gestão de Pedidos</h1>
    <p>Este código implementa um sistema de gestão de pedidos em Python, permitindo ao utilizador registrar, consultar, atualizar, exibir e eliminar pedidos de manutenção.</p>
    <h2>Como Funciona</h2>
    <ol>
        <li>O programa define várias funções para gerenciar os pedidos:</li>
        <ul>
            <li><code>registrar_pedido(pedidos)</code>: Registra um novo pedido, atribuindo um ID único e guardando a descrição e o estado inicial como "Pendente".</li>
            <li><code>consultar_pedido(pedidos)</code>: Permite ao utilizador consultar um pedido específico pelo seu ID, mostrando a descrição e o estado do pedido.</li>
            <li><code>atualizar_estado(pedidos)</code>: Permite ao utilizador atualizar o estado de um pedido existente, com opções para "Pendente", "Em Andamento" ou "Concluído".</li>
            <li><code>exibir_pedidos(pedidos)</code>: Mostra uma lista de todos os pedidos registrados, mostrando o ID, a descrição e o estado de cada um.</li>
            <li><code>eliminar_pedidos(pedidos)</code>: Permite ao usuário eliminar um pedido pelo seu ID.</li>
        </ul>
        <li>A função <code>main()</code> controla o programa, mostrando um menu com opções para o usuário:</li>
        <ul>
            <li>Registrar Pedido</li>
            <li>Consultar Pedido</li>
            <li>Atualizar Estado</li>
            <li>Exibir Todos os Pedidos</li>
            <li>Eliminar Pedido</li>
            <li>Sair</li>
        </ul>
        <li>O programa continua em execução até que o utilizador escolha a opção de sair.</li>
    </ol>
