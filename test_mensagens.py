import unittest
from mensagens import (
    saudacao,
    mensagem_idade,
    projeto_nome,
    eh_maior_de_idade,
    nome_valido
)


class TestMensagens(unittest.TestCase):

    def test_saudacao(self):
        self.assertEqual(
            saudacao("Henrique"),
            "Olá, Henrique! Bem-vindo ao projeto DevOps."
        )

    def test_mensagem_idade(self):
        self.assertEqual(
            mensagem_idade(24),
            "Você tem 24 anos."
        )

    def test_projeto_nome(self):
        self.assertEqual(
            projeto_nome(),
            "Projeto DevOps em Python!"
        )

    def test_maior_de_idade(self):
        self.assertTrue(eh_maior_de_idade(18))

    def test_nome_valido(self):
        self.assertTrue(nome_valido("Henrique"))


if __name__ == "__main__":
    unittest.main()
