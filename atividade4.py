# SISTEMA COMPLETO - 4 PROGRAMAS EM 1
# Calculadora, Sistema de Notas, Verificador de Senha e Analisador de Números

def calculadora():
    """1 - CALCULADORA BÁSICA"""
    print("\n=== CALCULADORA BÁSICA ===")
    print("Operações disponíveis:")
    print("+ (Adição)")
    print("- (Subtração)")
    print("* (Multiplicação)")
    print("/ (Divisão)")
    print("Digite 'voltar' para retornar ao menu principal")
    
    while True:
        try:
            entrada = input("\nDigite a operação (ex: 5 + 3) ou 'voltar': ").strip()
            
            if entrada.lower() == 'voltar':
                break
            
            if '+' in entrada:
                nums = entrada.split('+')
                resultado = float(nums[0].strip()) + float(nums[1].strip())
                print(f"Resultado: {resultado}")
            
            elif '-' in entrada:
                nums = entrada.split('-')
                resultado = float(nums[0].strip()) - float(nums[1].strip())
                print(f"Resultado: {resultado}")
            
            elif '*' in entrada:
                nums = entrada.split('*')
                resultado = float(nums[0].strip()) * float(nums[1].strip())
                print(f"Resultado: {resultado}")
            
            elif '/' in entrada:
                nums = entrada.split('/')
                num1 = float(nums[0].strip())
                num2 = float(nums[1].strip())
                
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida!")
                else:
                    resultado = num1 / num2
                    print(f"Resultado: {resultado}")
            
            else:
                print("Operação inválida! Use +, -, * ou /")
        
        except ValueError:
            print("Erro: Digite números válidos!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

def sistema_notas():
    """2 - SISTEMA DE REGISTRO DE NOTAS DOS ALUNOS"""
    print("\n=== SISTEMA DE NOTAS DOS ALUNOS ===")
    
    alunos = {}
    
    while True:
        print("\nOpções:")
        print("1 - Adicionar aluno e nota")
        print("2 - Ver todas as notas")
        print("3 - Calcular média da turma")
        print("4 - Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            try:
                nome = input("Nome do aluno: ").strip()
                if not nome:
                    print("Nome não pode estar vazio!")
                    continue
                
                nota = float(input("Nota do aluno (0-10): "))
                
                if 0 <= nota <= 10:
                    alunos[nome] = nota
                    print(f"Nota de {nome} registrada: {nota}")
                else:
                    print("Nota deve estar entre 0 e 10!")
            
            except ValueError:
                print("Digite uma nota válida!")
        
        elif opcao == '2':
            if alunos:
                print("\n--- NOTAS DOS ALUNOS ---")
                for nome, nota in alunos.items():
                    print(f"{nome}: {nota}")
            else:
                print("Nenhuma nota registrada ainda!")
        
        elif opcao == '3':
            if alunos:
                media = sum(alunos.values()) / len(alunos)
                print(f"\n--- ESTATÍSTICAS DA TURMA ---")
                print(f"Número de alunos: {len(alunos)}")
                print(f"Média da turma: {media:.2f}")
                
                maior_nota = max(alunos.values())
                menor_nota = min(alunos.values())
                print(f"Maior nota: {maior_nota}")
                print(f"Menor nota: {menor_nota}")
            else:
                print("Nenhuma nota registrada para calcular a média!")
        
        elif opcao == '4':
            break
        
        else:
            print("Opção inválida!")

def verificar_senha():
    """3 - VERIFICADOR DE SEGURANÇA DE SENHA"""
    print("\n=== VERIFICADOR DE SEGURANÇA DE SENHA ===")
    print("Critérios de segurança:")
    print("- Pelo menos 8 caracteres")
    print("- Pelo menos um número")
    
    while True:
        senha = input("\nDigite sua senha (ou 'voltar' para menu principal): ")
        
        if senha.lower() == 'voltar':
            break
        
        criterios_atendidos = []
        criterios_nao_atendidos = []
        
        # Critério 1: Pelo menos 8 caracteres
        if len(senha) >= 8:
            criterios_atendidos.append("✓ Possui pelo menos 8 caracteres")
        else:
            criterios_nao_atendidos.append("✗ Deve ter pelo menos 8 caracteres")
        
        # Critério 2: Pelo menos um número
        tem_numero = any(char.isdigit() for char in senha)
        if tem_numero:
            criterios_atendidos.append("✓ Contém pelo menos um número")
        else:
            criterios_nao_atendidos.append("✗ Deve conter pelo menos um número")
        
        # Resultado
        print(f"\n--- ANÁLISE DA SENHA ---")
        print(f"Senha analisada: {'*' * len(senha)}")
        
        if criterios_atendidos:
            print("\nCritérios ATENDIDOS:")
            for criterio in criterios_atendidos:
                print(f"  {criterio}")
        
        if criterios_nao_atendidos:
            print("\nCritérios NÃO ATENDIDOS:")
            for criterio in criterios_nao_atendidos:
                print(f"  {criterio}")
        
        # Veredicto final
        if len(criterios_nao_atendidos) == 0:
            print("\n🔒 SENHA SEGURA! Todos os critérios foram atendidos.")
        else:
            print(f"\n🔓 SENHA INSEGURA! {len(criterios_nao_atendidos)} critério(s) não atendido(s).")
        
        # Dicas adicionais
        print("\n--- DICAS EXTRAS ---")
        if len(senha) < 12:
            print("💡 Para maior segurança, use pelo menos 12 caracteres")
        
        if not any(char.isupper() for char in senha):
            print("💡 Considere adicionar letras maiúsculas")
        
        if not any(char.islower() for char in senha):
            print("💡 Considere adicionar letras minúsculas")
        
        if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in senha):
            print("💡 Considere adicionar símbolos especiais (!@#$%...)")

def analisador_numeros():
    """4 - ANALISADOR DE NÚMEROS PARES E ÍMPARES"""
    print("\n=== ANALISADOR DE NÚMEROS PARES E ÍMPARES ===")
    print("Digite números para análise. Digite 'fim' para ver o resultado final.")
    
    pares = []
    impares = []
    
    while True:
        entrada = input("\nDigite um número (ou 'fim' para terminar, 'voltar' para menu): ").strip()
        
        if entrada.lower() == 'fim':
            # Exibir resultado final
            print("\n" + "="*50)
            print("RESULTADO FINAL DA ANÁLISE")
            print("="*50)
            
            print(f"\n📊 ESTATÍSTICAS:")
            print(f"Total de números analisados: {len(pares) + len(impares)}")
            print(f"Números pares: {len(pares)}")
            print(f"Números ímpares: {len(impares)}")
            
            if pares:
                print(f"\n🔢 NÚMEROS PARES encontrados:")
                print(f"Lista: {pares}")
                print(f"Maior par: {max(pares)}")
                print(f"Menor par: {min(pares)}")
                print(f"Soma dos pares: {sum(pares)}")
            
            if impares:
                print(f"\n🔢 NÚMEROS ÍMPARES encontrados:")
                print(f"Lista: {impares}")
                print(f"Maior ímpar: {max(impares)}")
                print(f"Menor ímpar: {min(impares)}")
                print(f"Soma dos ímpares: {sum(impares)}")
            
            # Percentuais
            if pares or impares:
                total = len(pares) + len(impares)
                perc_pares = (len(pares) / total) * 100
                perc_impares = (len(impares) / total) * 100
                
                print(f"\n📈 PERCENTUAIS:")
                print(f"Pares: {perc_pares:.1f}%")
                print(f"Ímpares: {perc_impares:.1f}%")
            
            if not pares and not impares:
                print("Nenhum número foi analisado!")
            
            input("\nPressione Enter para continuar...")
            continue
        
        elif entrada.lower() == 'voltar':
            break
        
        try:
            numero = int(entrada)
            
            if numero % 2 == 0:
                pares.append(numero)
                print(f"{numero} é PAR")
            else:
                impares.append(numero)
                print(f"{numero} é ÍMPAR")
        
        except ValueError:
            print("Por favor, digite um número inteiro válido!")

def menu_principal():
    """MENU PRINCIPAL DO SISTEMA"""
    while True:
        print("\n" + "="*60)
        print("🔧 SISTEMA COMPLETO - ESCOLHA UMA OPÇÃO")
        print("="*60)
        print("1 - 🧮 Calculadora Básica")
        print("2 - 📚 Sistema de Notas dos Alunos")
        print("3 - 🔒 Verificador de Segurança de Senha")
        print("4 - 🔢 Analisador de Números (Pares/Ímpares)")
        print("5 - ❌ Sair do Sistema")
        print("="*60)
        
        opcao = input("Digite sua opção (1-5): ").strip()
        
        if opcao == '1':
            calculadora()
        
        elif opcao == '2':
            sistema_notas()
        
        elif opcao == '3':
            verificar_senha()
        
        elif opcao == '4':
            analisador_numeros()
        
        elif opcao == '5':
            print("\n👋 Obrigado por usar o sistema! Até logo!")
            break
        
        else:
            print("\n❌ Opção inválida! Escolha uma opção de 1 a 5.")

# EXECUTAR O SISTEMA COMPLETO
if __name__ == "__main__":
    print("🚀 Iniciando Sistema Completo...")
    menu_principal()