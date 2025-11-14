# **IMPLEMENTAÇÃO DE PADRÕES DE PROJETO**
Todo o conteúdo conceitual e diagramas são baseados no catálogo do [Refactoring Guru](https://refactoring.guru/) e no material de aula fornecido.  
A implementação do código e a estruturação deste exemplo foram desenvolvidas com auxílio da LLM Blackbox AI.  

## 🍔 Padrão Criacional de Projeto : Builder (C++)

1. **O que é o Padrão Builder?** - O padrão permite que você construa objetos complexos passo a passo. Usando o mesmo código de construção, você pode produzir diferentes tipos e representações de um objeto;

2. **O Problema que ele Resolve** - Imagine um objeto complexo que exige uma inicialização trabalhosa, com muitos campos e objetos aninhados. Esse código de inicialização geralmente fica "enterrado" dentro de um construtor monstruoso com dezenas de parâmetros. Pior ainda: se diferentes configurações do objeto forem necessárias, muitas vezes recorre-se a criar uma subclasse para cada configuração possível, o que leva a uma "explosão de subclasses".

3. **A Solução (A Estrutura Clássica)** - O padrão Builder sugere que você extraia o código de construção do objeto de sua própria classe e o mova para objetos separados chamados builders (construtores). O padrão organiza a construção em uma série de etapas. Para criar um objeto, você executa uma série dessas etapas em um objeto construtor. A parte importante é que você não precisa chamar todas as etapas, apenas as necessárias para aquela configuração específica.

### Diagrama UML:

<img width="460" height="580" alt="image" src="https://github.com/user-attachments/assets/d7ce8064-c89a-4f9b-9789-4ca910d7f8d8" />

### Código comentado:

```
#include <iostream> // para entrada/saída (std::cout);
#include <string> // para usar a classe std::string;
#include <map> // para usar a classe std::map;

// A classe complexa que será construída:
class Hamburguer {
private:
    // Atributos do Produto:
    std::string pao;
    std::string carne;
    std::string queijo;

    // Um map é usado para 'extras' para ser flexível;
    // Podemos adicionar "Bacon", "Picles", "Ovo", etc. (Strings) sem mudar a classe;
    std::map<std::string, bool> extras;

    // Construtor PRIVADO;
    // Ninguém de fora pode chamar 'new Hamburguer();
    Hamburguer(const std::string& p, const std::string& c, const std::string& q, const std::map<std::string, bool>& e)
        // Lista de inicialização:
        : pao(p), carne(c), queijo(q), extras(e) {}

public:
    // 'friend' concede ao 'ConstrutorDeHamburguer' acesso aos membros privados;
    friend class ConstrutorDeHamburguer;

    // Método auxiliar para exibir o resultado;
    // 'const' no final implica que o método não modifica o objeto;
    void imprimir() const {
        std::cout << "--- SEU PEDIDO ---" << std::endl;
        std::cout << "Pao: " << (pao.empty() ? "Nenhum" : pao) << std::endl;
        std::cout << "Carne: " << (carne.empty() ? "Nenhum" : carne) << std::endl;
        std::cout << "Queijo: " << (queijo.empty() ? "Nenhum" : queijo) << std::endl;
        
        // Itera sobre o map 'extras'
        for (const auto& extra : extras) {
            // extra.first é a chave (string, ex: "Bacon")
            // extra.second é o valor (bool, ex: true)
            if (extra.second) {
                std::cout << "Extra: " << extra.first << std::endl;
            }
        }
        std::cout << "-------------------\n" << std::endl;
    }
};

// O CONSTRUTOR (Builder);
// Esta classe sabe como construir o 'Hamburguer' passo a passo;
class ConstrutorDeHamburguer {
private:
    // Armazena as partes temporariamente durante a construção;
    std::string pao;
    std::string carne;
    std::string queijo;
    std::map<std::string, bool> extras;

public:
    // Cada método retorna 'ConstrutorDeHamburguer&' (uma referência a si mesmo);
    // 'return *this;' é o que permite o "encadeamento";
    ConstrutorDeHamburguer& set_pao(const std::string& tipo) {
        this->pao = tipo; // 'this->' se refere ao membro da classe;
        return *this; // Retorna o próprio objeto para o encadeamento;
    }

    ConstrutorDeHamburguer& set_carne(const std::string& tipo) {
        this->carne = tipo;
        return *this;
    }

    ConstrutorDeHamburguer& add_queijo(const std::string& tipo) {
        this->queijo = tipo;
        return *this;
    }

    // Método flexível para adicionar qualquer extra ao map;
    ConstrutorDeHamburguer& add_extra(const std::string& nome) {
        this->extras[nome] = true;
        return *this;
    }

    // Limpa o builder (para que possa ser reutilizado para a construção de um novo produto);
    void reset() {
        pao.clear();    // Limpa a string
        carne.clear();
        queijo.clear();
        extras.clear(); // Limpa o map
    }


    // O método 'build()' monta e retorna o produto final;
    Hamburguer build() {
        // Vantagem do Builder: pode-se validar os dados antes ddo objeto ser criado;
        if (pao.empty() || carne.empty()) {
            // Lança uma exceção se os ingredientes mínimos não forem fornecidos;
            throw std::invalid_argument("Pão e carne sao necessarios para um hamburguer!");
        }
        
        // Chama o construtor privado do Hamburguer, passando as partes armazenadas.
        return Hamburguer(pao, carne, queijo, extras);
    }
};


// O 'main' é o código cliente que usa o padrão.
int main() {
    // 1. Cria o objeto construtor.
    ConstrutorDeHamburguer builder;

    // --- Pedido 1: X-Bacon Monstro ---
    // O cliente "dirige" a construção usando a interface fluente.
    Hamburguer xbacon_monstro = builder.set_pao("Brioche")
                                      .set_carne("Picanha 200g")
                                      .add_queijo("Cheddar")
                                      .add_extra("Bacon")
                                      .add_extra("Maionese")
                                      .build(); // 'build()' finaliza e retorna o produto

    xbacon_monstro.imprimir(); // Usa o produto pronto

    // --- Pedido 2: Simples ---
    // 2. Reutiliza o mesmo builder, limpando-o primeiro.
    builder.reset();
    
    // 3. Constrói um produto diferente.
    Hamburguer simples = builder.set_pao("Frances")
                                .set_carne("Bovino 90g")
                                .add_extra("Ketchup")
                                .build();

    simples.imprimir();

    return 0; // Fim do programa
}
```


