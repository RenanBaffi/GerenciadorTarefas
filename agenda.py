def adicionar_contato(contatos, nome_contato):
  contato = {"contato": nome_contato, "favorito": False}
  contatos.append(contato)
  print(f"Contato {nome_contato} foi adicionada com sucesso!")
  return

def lista_contatos(contatos):
  print("\nLista de contatos")
  for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["favorito"] else " "
        nome_contato = contato["contato"]
        print(f"{indice}. [{status}] {nome_contato}")
  return

def atualizar_nome_contato(contatos, indice_contato, novo_nome_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
    print(f"Contato {indice_contato} atualizado para {novo_nome_contato}")
  else:
     print("Contato inválido")
  return 

def contato_favorito(contatos, indice_contato):
   indice_contato_ajustado = int(indice_contato) - 1 
   contatos[indice_contato_ajustado]["favorito"] = True
   print(f"Contato {indice_contato} marcado como favorito")
   return 

def deletar_contato(contatos):
    for contato in contatos:
      indice_contato_ajustado = int(indice_contato) - 1
      contatos.remove(contato)
    print(f"Contato {indice_contato} deletado")
    return
   

contatos = []
while True:
  print("\n Menu de opções da agenda:")
  print("1. Adicionar contato")
  print("2. Visualizar lista de contatos")
  print("3. Editar contato")
  print("4. Marcar contato como favorito")
  print("5. Apagar contato")
  
  escolha = input ("Digite sua escolha: ")

  if escolha == "1":
    nome_contato = input("Digite o nome do contato: ")
    adicionar_contato(contatos, nome_contato)

  elif escolha == "2":
    lista_contatos (contatos)

  elif escolha == "3":
     lista_contatos(contatos)
     indice_contato = input("Digite o número do contato que deseja alterar: ")
     novo_nome = input("Digite o novo contato: ")
     atualizar_nome_contato(contatos, indice_contato, novo_nome)

  elif escolha == "4":
     lista_contatos(contatos)
     indice_contato = input("Digite o número do contato que deseja marcar como favorito: ")
     contato_favorito(contatos, indice_contato)
  
  elif escolha == "5":
     lista_contatos(contatos)
     indice_contato = input("Digite o número do contato que deseja deletar: ")
     deletar_contato(contatos)
     
 
