import requests
import unittest

## Regra de nomenclatura: teste_Numero/numeroDaFalha_NomeIntuitivo

class TestStringMethods(unittest.TestCase):


    def test_01_get_aluno(self):
        resp = requests.get('http://localhost:5000/alunos')

        if resp.status_code == 404:
            self.fail("página /alunos não encontrada")

        try:
            retorno= resp.json()
        except:
            self.fail("o retorno não saiu como json")

        self.assertEqual(type(retorno),type([]))

    def test_02_get_professores(self):
        resp = requests.get('http://localhost:5000/professores')
        if resp.status_code == 404:
            self.fail("pagina /professores não encontrada")

        try:
            retorno = resp.json()
        except:
            self.fail("o retorno não saiu como json")

        self.assertEqual(type(retorno),type([]))

    def teste_03_get_turmas(self):
        resp = requests.get('http://localhost:5000/turmas')
        if resp.status_code == 404:
            self.fail("pagina /turmas não encontrada")

        try:
            retorno = resp.json()
        except:
            self.fail("retorno não saiu como json")

        self.assertEqual(type(retorno),type([]))
    
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()
