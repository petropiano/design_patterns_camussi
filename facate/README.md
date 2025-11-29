**

## O QUE É O PADRÃO FACADE?

O padrão Facade (ou Fachada) é um padrão de projeto estrutural que fornece uma interface simplificada para uma biblioteca, um framework ou qualquer conjunto complexo de classes.

**Neste projeto:**

-   O Facade atua como um "técnico de som" virtual.
    
-   O cliente não precisa saber ajustar frequências, posicionar microfones ou regular voltagem.
    
-   O produto final é um setup de guitarra completo (Black Metal, Death Metal, etc.) ativado com uma única chamada de método.
    

## PROBLEMAS QUE ELE RESOLVE
Imagine que você precisa fazer seu código trabalhar com um conjunto amplo de objetos que pertencem a uma biblioteca sofisticada ou framework. Normalmente, você precisaria inicializar todos esses objetos um por um, acompanhar as dependências, executar métodos na ordem correta e assim por diante.

Como resultado, a lógica de negócio de suas classes vai ficar fortemente acoplada aos detalhes de implementação de classes de terceiros, tornando o código difícil de compreender e manter.

## COMO ELE RESOLVE

Então, cria-se uma classe Fachada (Facade) que atua como um intermediário simples entre o  código e o sistema complexo.

Pense no Facade como um operador de atendimento telefônico de uma grande loja. Se você quiser fazer um pedido complexo, você não liga para o estoque, depois para o departamento de embalagem e depois para a transportadora. Você liga para o atendente (Facade). Ele sabe exatamente quem chamar e em qual ordem para resolver seu problema.

o _GuitarRigFacade_ é esse atendente. Ele conhece todas as peças soltas (Amp, Pedal, NoiseGate), sabe quais botões girar e em qual sequência ligá-los.

![An example of taking a phone order](https://refactoring.guru/images/patterns/diagrams/facade/live-example-en.png)

## DIAGRAMA UML
![Facade](https://refactoring.guru/images/patterns/diagrams/facade/structure.png?id=258401362234ac77a2aaf1cde62339e7)


1.  O **Facade** fornece acesso conveniente a uma parte específica da funcionalidade do subsistema. Ele sabe para onde direcionar o pedido do cliente e como operar todas as partes móveis.
    
2.  O **Additional Facade** (opcional) pode ser criado para prevenir a poluição de um único facade com funcionalidades não relacionadas.
    
3.  O **Complex Subsystem** consiste em dezenas de objetos variados. Para fazer com que todos sejam úteis, é necessário se aprofundar nos detalhes de implementação do subsistema, tais como inicializar objetos na ordem correta e suprí-los com dados no formato correto.
    
4.  O **Client** usa o facade em vez de chamar os objetos do subsistema diretamente.

## CÓDIGO COMENTADO

```python
class NoiseGate:
    def set_threshold(self, value):
        print(f"NoiseGate: Threshold definido para {value}dB.")
    def enable(self):
        print("NoiseGate: Ligado.")

class DistortionPedal:
    def set_gain(self, level): ...
    def set_tone(self, level): ...
    def turn_on(self): ...

class Amplifier:
    def set_volume(self, level): ...
    def set_eq(self, bass, mid, treble): ...
    def turn_on(self): ...

class CabinetSimulator:
    def set_mic_position(self, position): ...

```

**Classes de Equipamento**: Representam os componentes individuais. Cada um tem métodos específicos (`set_threshold`, `set_eq`, `set_mic_position`) que exigem conhecimento técnico para serem configurados harmonicamente.




```python
class GuitarRigFacade:
    def __init__(self):
        self.noise_gate = NoiseGate()
        self.pedal = DistortionPedal()
        self.amp = Amplifier()
        self.cab = CabinetSimulator()


```



**`__init__`**: O construtor do Facade instancia todos os subsistemas necessários. O cliente não precisa criar `Amplifier` ou `Pedal` manualmente; o Facade já deixa tudo pronto para uso interno.

```python
    def activate_black_metal(self):
        print("\n--- Preset: TRUE NORWEGIAN BLACK METAL ---")
        self.amp.turn_on()
        
        # Configuração complexa encapsulada:
        self.noise_gate.set_threshold(-20) 
        self.noise_gate.enable()
        
        self.pedal.set_gain(10)
        self.pedal.set_tone(10) # Agudos no máximo para som "frio"
        self.pedal.turn_on()
        
        self.amp.set_eq(bass=4, mid=6, treble=10)
        self.amp.set_volume(10)
        
        self.cab.set_mic_position("borda do cone")
        print("--- Rig pronto. ---")

```

**`activate_...`**: Estes métodos são a "fachada". Eles escondem a complexidade da sequência de ativação. Observe que uma única chamada (`activate_black_metal`) dispara mais de 8 ações diferentes nos subsistemas, na ordem exata necessária para obter aquele timbre específico.
