def registrar_pedido(pedidos):
  id_pedidos = len(pedidos) + 1
  descricao = input("Descreva o problema: ")
  estado = "Pendente"
  pedidos[id_pedidos] = {"descricao": descricao, "estado": estado}
  print (f"O pedido #{id_pedidos} foi registrado.")

def consultar_pedido(pedidos):
  id_pedido = int(input("ID do pedido a consultar: "))
  if id_pedido in pedidos:
      pedido = pedidos[id_pedido]
      print(f"Pedido #{id_pedido} - Descrição: {pedido['descricao']}, Estado: {pedido['estado']}")
  else:
      print("Pedido não encontrado.")


def atualizar_estado(pedidos):
    id_pedido = int(input("ID do pedido a atualizar: "))
    if id_pedido in pedidos:
        novo_estado = input("Novo estado (Pendente/Em Andamento/Concluído): ")
        if novo_estado in ["Pendente", "Em Andamento", "Concluído"]:
            pedidos[id_pedido]["estado"] = novo_estado
            print(f"Estado do pedido #{id_pedido} atualizado para '{novo_estado}'.")
        else:
            print("Estado inválido.")
    else:
        print("Pedido não encontrado.")
  

def exibir_pedidos(pedidos):
  print("\nLista de Pedidos:")
  print("ID\tDescrição\t\tEstado")
  print("-" * 40)
  for id_pedido, info in pedidos.items():
      print(f"{id_pedido}\t{info['descricao'][:15]}\t\t{info['estado']}")

def eliminar_pedidos(pedidos):
    id_pedido = int(input("ID do pedido que quer eliminar: "))
    if id_pedido in pedidos:
        pedidos.pop (id_pedido)
        print (f"O pedido #{id_pedido} foi eliminado com sucesso.")
    else: 
        print ("Pedido não encontrado.")

def main():
  pedidos = {}
  while True:
    print("\nSistema de Gestão de Pedidos - Manutenção")
    print("1. Registar Pedido.")
    print("2. Consultar Pedido.")
    print("3. Atualizar Estado.")
    print("4. Exibir Todos os Pedidos.")
    print("5. Eliminar pedido.")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_pedido(pedidos)
    elif opcao == "2":
        consultar_pedido(pedidos)
    elif opcao == "3":
        atualizar_estado(pedidos)
    elif opcao == "4":
        exibir_pedidos(pedidos)
    elif opcao == "5":
        eliminar_pedidos(pedidos)
    elif opcao == "6":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
