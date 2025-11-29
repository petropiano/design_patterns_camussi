**
## O QUE É O PADRÃO BUILDER?
O padrão Builder é um padrão de projeto criacional que permite a construção de objetos complexos passo-a-passo. Frequentemente suporta uma interface fluente (encadeamento de métodos) para legibilidade, e um "diretor" pode orquestrar processos de construção comuns.

**Neste projeto:**
-   O builder permite adicionar ingredientes um de cada vez (ex: `set_pao("Brioche").set_carne("Picanha")`).
-   O diretor define receitas para hambúrgueres padrão (ex: X-Bacon).
-   O produto final é um objeto `Hamburger` totalmente configurado,;


## PROBLEMAS QUE ELE RESOLVE
Imagine um objeto complexo que requer uma inicialização trabalhosa, passo a passo, de muitos campos e objetos aninhados. 
Para construir uma casa simples, você precisa de quatro paredes, um chão, uma porta, janelas e um telhado. Mas e se você quiser uma casa maior, com quintal, piscina, sistema de aquecimento e fiação elétrica?

 ![Lots of subclasses create another problem](https://refactoring.guru/images/patterns/diagrams/builder/problem1.png)
E se alguém quiser Garagem, Piscina e Estátua?
Teríamos que criar: `CasaComGaragemEPiscinaEEstatua`
E assim por diante, para cada combinação.


Ou então, o código de inicialização fica enterrado dentro de um *construtor* monstruoso com muitos parâmetros.
Você pode acabar tornando o programa muito complexo ao tentar criar uma subclasse para cada configuração possível de um objeto.


![The telescoping constructor](https://refactoring.guru/images/patterns/diagrams/builder/problem2.png)

O problema surge na hora de criar o objeto `Casa`:
É difícil saber qual parâmetro pertence à qual variável.


## COMO ELE RESOLVE
O padrão Builder resolve esses problemas extraindo o código de construção do objeto de sua própria classe e o movendo para objetos separados chamados _builders_.


![Applying the Builder pattern](https://refactoring.guru/images/patterns/diagrams/builder/solution1.png)
No caso do objeto _Casa_, não é mais necessário criar um objeto "adivinhando" todos os cômodos de uma só vez. Em vez disso, o padrão nos permite construir o objeto passo a passo. Só se usa os métodos para as características que realmente são relevantes.


![](https://refactoring.guru/images/patterns/content/builder/builder-comic-1-en.png)


## DIAGRAMA UML
![Builder](https://refactoring.guru/images/patterns/diagrams/builder/structure-indexed.png?id=44b3d763ce91dbada5d8394ef777437f)

1. A interface *Builder* declara etapas de construção do produto que      são comuns a todos os tipos de builders.
  
 2.  `Concrete Builders` fornecem diferentes implementações das etapas de construção. Concrete builders podem produzir produtos que      não seguem a interface comum.
  
2.  `Products` são os objetos resultantes. Products construídos por diferentes builders não precisam pertencer à mesma hierarquia de     classe ou interface.

3. A classe `Director` define a ordem na qual chamar as etapas de construção, para que você possa criar e reutilizar configurações      específicas de produtos.
  
4. O `Client` deve associar um dos objetos builder com o director. Geralmente, isso é feito apenas uma vez, via parâmetros do    construtor    do director. Então, o director usa aquele objeto    builder para todas    as construções futuras. No entanto, existe uma    abordagem alternativa    para quando o client passa o objeto builder    para o método de produção    do director. Neste caso, você pode usar    um builder diferente cada vez    que produzir algo com o director.


## CÓDIGO COMENTADO
```python
    class Hamburger:
        def __init__(self):
            self.pao = None
            self.carne = None
            self.queijo = None
            self.bacon = False
            self.salada = False
            self.maionese = False
    
        def __str__(self):
            detalhespedido = [f"Pao: {self.pao}", f"Carne: {self.carne}"]
            if self.queijo: detalhespedido.append(f"Queijo: {self.queijo}")
            if self.bacon: detalhespedido.append("Extra: Bacon")
            if self.salada: detalhespedido.append("Extra: Salada")
            if self.maionese: detalhespedido.append("Extra: Maionese")
            return "\n".join(detalhespedido)
```
  **`__init__`**: Define a estrutura básica do objeto. Inicializa todos os ingredientes como vazios (`None`) ou desligados (`False`) para começar "zerado".
    
  **`__str__`**: Formata a saída de texto para leitura humana. Verifica condicionalmente quais extras foram adicionados e agrupa todas as linhas em um único texto formatado.
```python
    class BuilderHamburger:
        def __init__(self):
            self.hamburger = Hamburger()
    
        def reset(self):
            self.hamburger = Hamburger()
            return self
```
**`__init__`**: Instancia o construtor. Cria imediatamente um objeto `Hamburger` vazio e o guarda dentro do atributo `self.hamburger`.
    
**`reset`**: Reinicia o ciclo de construção. Descarta o hambúrguer atual (se houver) e substitui por uma nova instância limpa. Retorna o próprio construtor para manter a fluidez.
```python
    def set_pao(self, tipo):
            self.hamburger.pao = tipo
            return self
    
        def set_carne(self, tipo):
            self.hamburger.carne = tipo
            return self
        
        def add_queijo(self, tipo):
            self.hamburger.queijo = tipo
            return self
    
        def add_bacon(self):
            self.hamburger.bacon = True
            return self
    
        def add_salada(self):
            self.hamburger.salada = True
            return self
    
        def add_maionese(self):
            self.hamburger.maionese = True
            return self
            
```
Os métodos **(`set_...` / `add_...`)**: Alteram o atributo específico do objeto `Hamburger` que está sendo guardado. Retornam sempre `self` (a própria instância do builder) para permitir o encadeamento de métodos.
```python
    def build(self):
            produto = self.hamburger
            self.reset()
            return produto
```
**`build`**: Recupera o objeto `Hamburger` que estava sendo montado, chama o método `reset()` para limpar o construtor e deixá-lo pronto para o próximo pedido e então, retorna o produto finalizado.

**
