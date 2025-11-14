#include <iostream>
#include <string>
#include <map>

class Hamburguer {
private:
    std::string pao;
    std::string carne;
    std::string queijo;
    std::map<std::string, bool> extras;

    Hamburguer(const std::string& p, const std::string& c, const std::string& q, const std::map<std::string, bool>& e)
        : pao(p), carne(c), queijo(q), extras(e) {}

public:
    friend class ConstrutorDeHamburguer;

    void imprimir() const {
        std::cout << "--- SEU PEDIDO ---" << std::endl;
        std::cout << "Pão: " << (pao.empty() ? "Nenhum" : pao) << std::endl;
        std::cout << "Carne: " << (carne.empty() ? "Nenhum" : carne) << std::endl;
        std::cout << "Queijo: " << (queijo.empty() ? "Nenhum" : queijo) << std::endl;
        for (const auto& extra : extras) {
            if (extra.second) {
                std::cout << "Extra: " << extra.first << std::endl;
            }
        }
        std::cout << "-------------------\n" << std::endl;
    }
};

class ConstrutorDeHamburguer {
private:
    std::string pao;
    std::string carne;
    std::string queijo;
    std::map<std::string, bool> extras;

public:
    ConstrutorDeHamburguer& set_pao(const std::string& tipo) {
        this->pao = tipo;
        return *this;
    }

    ConstrutorDeHamburguer& set_carne(const std::string& tipo) {
        this->carne = tipo;
        return *this;
    }

    ConstrutorDeHamburguer& add_queijo(const std::string& tipo) {
        this->queijo = tipo;
        return *this;
    }

    ConstrutorDeHamburguer& add_extra(const std::string& nome) {
        this->extras[nome] = true;
        return *this;
    }

    void reset() {
        pao.clear();
        carne.clear();
        queijo.clear();
        extras.clear();
    }

    Hamburguer build() {
        if (pao.empty() || carne.empty()) {
            throw std::invalid_argument("Pão e carne são necessários para um hamburguer!");
        }
        return Hamburguer(pao, carne, queijo, extras);
    }
};

int main() {
    ConstrutorDeHamburguer builder;

    Hamburguer xbacon_monstro = builder.set_pao("Brioche")
                                     .set_carne("Picanha 200g")
                                     .add_queijo("Cheddar")
                                     .add_extra("Bacon")
                                     .add_extra("Maionese")
                                     .build();

    xbacon_monstro.imprimir();

    builder.reset();
    Hamburguer simples = builder.set_pao("Frances")
                              .set_carne("Bovino 90g")
                              .add_extra("Ketchup")
                              .build();

    simples.imprimir();

    return 0;
}
