def criptografar(texto):
    chave = 3
    texto_criptografado = ""

    for char in texto:
        if char.isalpha():
            ascii_code = ord(char)
            ascii_code += chave

            if char.islower():
                if ascii_code > ord("z"):
                    ascii_code -= 26
                elif ascii_code < ord("a"):
                    ascii_code += 26
            elif char.isupper():
                if ascii_code > ord("Z"):
                    ascii_code -= 26
                elif ascii_code < ord("A"):
                    ascii_code += 26

            texto_criptografado += chr(ascii_code)
        elif char.isdigit():
            digit = int(char)
            digit = (digit + chave) % 10
            texto_criptografado += str(digit)
        else:
            texto_criptografado += char

    return texto_criptografado

def descriptografar(texto):
    chave = 3
    texto_descriptografado = ""

    for char in texto:
        if char.isalpha():
            ascii_code = ord(char)
            ascii_code -= chave

            if char.islower():
                if ascii_code > ord("z"):
                    ascii_code -= 26
                elif ascii_code < ord("a"):
                    ascii_code += 26
            elif char.isupper():
                if ascii_code > ord("Z"):
                    ascii_code -= 26
                elif ascii_code < ord("A"):
                    ascii_code += 26

            texto_descriptografado += chr(ascii_code)
        elif char.isdigit():
            # Tratar caracteres numéricos
            digit = int(char)
            digit = (digit - chave) % 10
            texto_descriptografado += str(digit)
        else:
            texto_descriptografado += char

    return texto_descriptografado

def criptografar_mensagem(texto):
    chave = 3
    texto_criptografado = ""

    for char in texto:
        if char.isalpha():
            ascii_code = ord(char)
            ascii_code += chave

            if char.islower():
                if ascii_code > ord("z"):
                    ascii_code -= 26
                elif ascii_code < ord("a"):
                    ascii_code += 26
            elif char.isupper():
                if ascii_code > ord("Z"):
                    ascii_code -= 26
                elif ascii_code < ord("A"):
                    ascii_code += 26

            texto_criptografado += chr(ascii_code)
        elif char.isdigit():
            digit = int(char)
            digit = (digit + chave) % 10
            texto_criptografado += str(digit)
        else:
            texto_criptografado += char

    return texto_criptografado

def descriptografar_mensagem(texto):
    chave = 3
    texto_descriptografado = ""

    for char in texto:
        if char.isalpha():
            ascii_code = ord(char)
            ascii_code -= chave

            if char.islower():
                if ascii_code > ord("z"):
                    ascii_code -= 26
                elif ascii_code < ord("a"):
                    ascii_code += 26
            elif char.isupper():
                if ascii_code > ord("Z"):
                    ascii_code -= 26
                elif ascii_code < ord("A"):
                    ascii_code += 26

            texto_descriptografado += chr(ascii_code)
        elif char.isdigit():
            digit = int(char)
            digit = (digit - chave) % 10
            texto_descriptografado += str(digit)
        else:
            texto_descriptografado += char

    return texto_descriptografado

def ler_arquivo():
    try:
        with open("mensagens.txt", "r") as file:
            conteudo_criptografado = file.read().splitlines()

        print("Conteúdo do arquivo:")

        for linha in conteudo_criptografado:
            mensagem_descriptografada = descriptografar_mensagem(linha)
            print(mensagem_descriptografada)

    except FileNotFoundError:
        print("O arquivo 'mensagens.txt' não foi encontrado.")

    menuArquivo()


def cadastroUser():
    user = input("Digite o nome de usuário para efetuar o cadastro: ")
    pswd = input("Digite a senha para efetuar o cadastro: ")

    user_criptografado = criptografar(user)
    pswd_criptografada = criptografar(pswd)

    with open("usuarios.txt", "a") as file:
        file.write(user_criptografado + "\n")

    with open("senhas.txt", "a") as file:
        file.write(pswd_criptografada + "\n")

    print("Cadastro efetuado com sucesso!")
    menu()


def efetuarLogin():
    user = input("Digite o nome de usuário: ")
    pswd = input("Digite a senha: ")

    with open("usuarios.txt", "r") as file:
        usuarios_criptografados = file.read().splitlines()

    with open("senhas.txt", "r") as file:
        senhas_criptografadas = file.read().splitlines()

    usuarios = [descriptografar(u) for u in usuarios_criptografados]

    for index, senha_criptografada in enumerate(senhas_criptografadas):
        senha_descriptografada = descriptografar(senha_criptografada)
        if user == usuarios[index] and pswd == senha_descriptografada:
            print("Login Successful!")
            menuArquivo()
            return

    print("Nenhum usuário cadastrado com essas credenciais.")
    menu()


def menu():
    print("Bem vindo ao R4zor's Engine!")
    print("Options:")
    print("1. Cadastrar")
    print("2. Login")

    opcao = input("Escolha uma opção (1 ou 2): ")

    if opcao == "1":
        cadastroUser()
    elif opcao == "2":
        efetuarLogin()
    else:
        print("Não há opção válida, digite novamente.")
        menu()

def menuArquivo():
    print("Bem vindo ao R4zor's Writing!")
    print("Options:")
    print("1. Digitar mensagem")
    print("2. Ler arquivo")
    print("3. Sair")

    opcao = input("Escolha uma opção (1 ou 2): ")

    if opcao == "1":
        digitar_text()
    elif opcao == "2":
        ler_arquivo()
    elif opcao == "3":
        print("Software finished.")

    else:
        print("Opção inválida. Por favor, digite novamente.")
        menuArquivo()

def digitar_text():
    mensagem = input("Digite a mensagem: ")

    mensagem_criptografada = criptografar_mensagem(mensagem)

    with open("mensagens.txt", "a") as file:
        file.write(mensagem_criptografada + "\n")

    print("Mensagem gravada com sucesso!")
    menuArquivo()

menu()
