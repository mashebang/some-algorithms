# Dict

Dict (ou dicionário) é uma estrutura de dados (assim como as listas) que nos ajuda a lidar com coleções de dados. A diferença de um Dicionário e uma Lista é que as listas usam índices numéricos gerados automáticamente para identificar seus elementos, já no dicionário usamos uma estruturas de chave e valor.

Estruturas de chave e valor são amplamente conhecidas na programação, tendo várias formas de representá-las. Os dicionários da vida real (Aurélio e cia) são exemplos simples do dia a dia de uma estrutura `chave-valor`. As palavras são os identificadores e os significados são os valores. Quando queremos achar o significado, procuramos pela palavra e mesmo que ela tenha vários significados, vamos encontrar todos no mesmo lugar.

Se o aurélio fosse escrito na linguagem de programação python, teríamos o seguinte exemplo:
```python
significado_arroz = Aurelio['arroz']

print(significado_arroz)

'''
### substantivo masculinoangiospermas

    1. erva ereta de até 1 m ( Oryza sativa ) da fam. das gramíneas, com flores em espiguetas e cariopses coriáceas, prov. de origem asiática e cultivada há mais de 5.000 anos, com inúmeras variedades, pelos grãos, que constituem a dieta básica de grande parte da população mundial, esp. da Ásia.

'''
```


Uma representação chave e valor se caracteriza por ter um idetificador único e um valor associado a ele. Acessamos os valores de uma estrutura chave-valor através desse identificador e não por índice inteiro. Esse identificador único pode ser customizado por quem está escrevendo o código e pode facilitar a leitura e o entendimento do código.

Podemos descrever uma pessoa e seus dados básicos com um estrutura de chave e valor. Sendo os nomes dos dados o identificador único e os valores representando os valores para cada pessoa. No Python temos o seguinte codigo como exemplo:

```python
pessoa = {
  "nome": "Paulo",
  "idade": 30,
  "profissao": "Programador"
}

# para acessar o nome da pessoa:

print(pessoa['nome'])  # 'Paulo'
# outra forma de recuperar o valor é usando o método 'get'
print(pessoa.get('nome'))  # 'Paulo'
```

Neste caso, `nome` é um identificador único, não podendo ter outra entrada no dicionário. Sempre que acessarmos o nome, ela será `Paulo`. Se tentarmos adicionar outra entrada duplicada, o que vai acontecer é a sobrescrita. Exemplo:

```python
pessoa['nome'] = 'Jose'
# ou usando o metodo 'update' que os dicionarios nos fornecem
pessoa.update({'nome': 'Jose'})

print(pessoa['nome']) # pessoa['nome'] agora tem o valor de 'Jose'
```

O maior benefício do dicionário é justamente seu poder semântico, pois podemos atribuir a ele significados menos abstratos e dar nomes personalizados para nossas chaves, o que nos ajuda a organizar melhor nosso código e fazer com que ele fique mais legível. Em listas, nos referenciamos a um valor pelo seu index. Isso pode funcionar muito bem para certos casos, mas em outros casos, pode dificultar nossa leitura. Num programa feito para registrar a avalição dos clientes de um estabelecimento, eles poderiam votar em 'bom', 'regular' e 'ruim'. O programador decidiu usar uma lista para guardar todos os votos dos clientes, resultando no fim do dia com o seguinte resultado:

```python
avaliacoes = (10, 20, 30)
```

Uma array com valor 10, 20 e 30 respectivamente. Usando um pouco de lógica e senso comum, podemos tentar concluir que os valores estão em ordem crescentes e que o restaurante recebeu 10 avaliações 'ruim', 20 'regular' e 30 'boas'. Mas não há nada que nos prove de verdade que foi isso que aconteceu. É aí que entra o papel semântico dos dicionários. Se fossemos representar esse mesmo problema com um Dict, teríamos algo como:


```python
avaliacoes = {
  "bom": 10,
  "regular": 30,
  "ruim": 20
}
```

Nesta versão do código não há dúvidas de quais valores correspondem a quais avaliações, sendo um exemplo prático de uso onde o dicionário cai melhor que uma Lista. 

Exercícios:

Baseado nos exemplos, crie um script para ser utilizado num restaurante, onde os clientes podem digitar uma nota para avaliar o atendimento, de 0 a 10. Menor que 3 consideramos uma avaliação ruim, maior que 3 e menor ou igual 7 é um avaliação regular. Maior que 7 é considerada uma avaliação boa. O programa só deve parar quando receber uma resposta com o valor 'sair', então o programa mostra um relatório com o numero de clientes para cada categoria de avaliação.

dica:
- use a estrutura de repetição while para que o programa rode até que o usuário digite 'sair'
- use dicionarios para guardar os valores de cada votação


