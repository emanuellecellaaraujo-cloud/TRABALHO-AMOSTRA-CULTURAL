import datetime
import os
import platform


def obter_saudacao():
    """Retorna uma saudação com base na hora atual do sistema."""
    hora_atual = datetime.datetime.now().hour

    if 5 <= hora_atual < 12:
        return "Bom dia!"
    elif 12 <= hora_atual < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"


def main():
    # 1. Gera a saudação dinâmica
    saudacao = obter_saudacao()

    # 2. Identifica o Sistema Operacional
    sistema_op = platform.system()
    versao_op = platform.release()

    # 3. Exibe os resultados no terminal de forma organizada
    print("-" * 50)
    print(f"{saudacao} Bem-vindo ao script de verificação.")
    print("-" * 50)
    print(f"Sistema Operacional detectado: {sistema_op} (Versão: {versao_op})")
    print(f"Diretório atual de trabalho: {os.getcwd()}")
    print("-" * 50)
    print("Script executado com sucesso!")


if __name__ == "__main__":
    main()
