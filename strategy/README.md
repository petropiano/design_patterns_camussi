
## O QUE É O PADRÃO STRATEGY?

O Strategy é um padrão de projeto comportamental que permite que você defina uma família de algoritmos, coloque cada um deles em uma classe separada, e faça os objetos deles intercambiáveis.

![Strategy design pattern](https://refactoring.guru/images/patterns/content/strategy/strategy.png)

**Neste projeto:**

-   O Strategy permite que o jogo suporte múltiplos controles (Xbox, PlayStation, Teclado) sem alterar o código principal do jogo.
    
-   O "algoritmo" aqui é o mapeamento de botões: o jogo pede "Pular", e a estratégia traduz para o botão ('A', 'X' ou 'Espaço').
    
    

## PROBLEMAS QUE ELE RESOLVE

Imagine que você decidiu criar um app de GPS para turistas. A primeira versão era simples: traçava rotas apenas para **carros**. Então, você atualizou o app para traçar rotas a **pé**. Depois, adicionou **transporte público**. Mais tarde, planejou adicionar rotas para **ciclistas** e rotas turísticas. 


![The code of the navigator became very bloated](https://refactoring.guru/images/patterns/diagrams/strategy/problem.png)


Dessa forma, o código da classe principal (`Navigator`) cresceu de forma exponencial. Cada vez que se adiciona um algoritmo novo, o arquivo dobra de tamanho. Qualquer alteração simples na rota de bicicleta podia criar bugs na rota de carro. Além disso, merge conflicts são frequentes quando todo mundo precisava mexer nesse mesmo arquivo gigante ao mesmo tempo.

## COMO ELE RESOLVE

A solução é pegar cada método de rota (Carro, Pé, Ônibus) e extraí-los para classes separadas chamadas **estratégias**.
A classe original (o `Navigator` ou Contexto) deixa de fazer o cálculo. Ela passa a ter apenas um campo que guarda uma referência para uma dessas estratégias. O Contexto "terceiriza" o trabalho: quando precisa de uma rota, ele chama a estratégia que estiver conectada no momento.

O `Navigator` não precisa saber se a rota é de carro ou de bicicleta. Ele trabalha com todas as estratégias através de uma interface genérica (ex: `construirRota`). Isso permite que você adicione novos tipos de transporte ou altere os existentes sem nunca mais precisar tocar no código principal do `Navigator`.


![Route planning strategies](https://refactoring.guru/images/patterns/diagrams/strategy/solution.png)


## DIAGRAMA UML

![Strategy](https://refactoring.guru/images/patterns/diagrams/strategy/structure-indexed.png?id=ff55c5a6273cf82a5667f3cab5b605c7)

1. O **Contexto** mantém uma referência para uma das estratégias concretas e se comunica com esse objeto apenas através da interface da estratégia.
2. A **Interface Strategy** é comum a todas as estratégias concretas. Ela declara um método que o contexto usa para executar uma estratégia.
3. As **Estratégias Concretas** implementam diferentes variações de um algoritmo que o contexto usa.
4. O **Contexto** chama o método de execução no objeto de estratégia vinculado toda vez que precisa rodar o algoritmo. O contexto não sabe com qual tipo de estratégia está trabalhando ou como o algoritmo é executado.
5. O **Cliente** cria um objeto de estratégia específico e o passa para o contexto. O contexto expõe um "setter" que permite aos clientes substituir a estratégia associada ao contexto em tempo de execução.
    
## CÓDIGO COMENTADO


```python
class InputStrategy(ABC):
    @abstractmethod
    def ler_pulo(self):
        pass

    @abstractmethod
    def ler_ataque(self):
        pass

```

**`InputStrategy`**: Define a interface comum (o contrato) para todas as estratégias.
 **`@abstractmethod`**: Este decorador obriga qualquer classe filha a implementar os métodos. O jogo sempre saberá que os métodos `ler_pulo` e `ler_ataque` existem, independente do controle usado.



```python
class ControleXbox(InputStrategy):
    def ler_pulo(self):
        return "Xbox: Botão 'A'"

    def ler_ataque(self):
        return "Xbox: 'X'"

class TecladoPC(InputStrategy):
    def ler_pulo(self):
        return "PC: 'ESPAÇO'"

    def ler_ataque(self):
        return "PC: Click Esquerdo do Mouse."

```


**`ControleXbox` / `TecladoPC`**: Cada classe encapsula a lógica específica de um dispositivo. Elas implementam os métodos exigidos pela interface, retornando as strings correspondentes ao hardware em questão.

```python
class GameContext:
    def __init__(self, strategy: InputStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> InputStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: InputStrategy) -> None:
        self._strategy = strategy

```

**`__init__`**: Inicializa o contexto recebendo uma estratégia padrão (ex: Teclado) e a armazena na variável `self._strategy`. 
**`@strategy.setter`**: Permite substituir o objeto `_strategy` em tempo de execução. Logo, o jogador pode trocar o input de forma muito mais prática.


```python
    def processar_input_jogador(self) -> None:
        print(f"Input: {self._strategy.__class__.__name__}")
        
        resultado_pulo = self._strategy.ler_pulo()
        resultado_ataque = self._strategy.ler_ataque()
        
        print(f" -> Pulo: {resultado_pulo}")
        print(f" -> Ataque: {resultado_ataque}")
        print("-" * 40)

```

**`processar_input_jogador`**: Em vez de usar vários `if/else` para checar o tipo de controle, o método apenas chama `self._strategy.ler_pulo()`. Ele confia que a estratégia atualmente plugada conseguirá retornar o comando correto.
