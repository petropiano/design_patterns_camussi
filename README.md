# IMPLEMENTAÇÃO DE PADRÕES DE PROJETO
Todo o conteúdo conceitual e diagramas são baseados no catálogo do Refactoring Guru (refactoring.guru/design-patterns) e no material de aula fornecido.
A implementação do código e a estruturação deste exemplo foram desenvolvidas com auxílio da LLM Google Gemini.

🍔 Padrão Criacional de Projeto : Builder (C++)
1. O que é o Padrão Builder? - O padrão permite que você construa objetos complexos passo a passo. Usando o mesmo código de construção, você pode produzir diferentes tipos e representações de um objeto;

2. O Problema que ele Resolve - Imagine um objeto complexo que exige uma inicialização trabalhosa, com muitos campos e objetos aninhados. Esse código de inicialização geralmente fica "enterrado" dentro de um construtor monstruoso com dezenas de parâmetros. Pior ainda: se diferentes configurações do objeto forem necessárias, muitas vezes recorre-se a criar uma subclasse para cada configuração possível, o que leva a uma "explosão de subclasses".

3. A Solução (A Estrutura Clássica) - O padrão Builder sugere que você extraia o código de construção do objeto de sua própria classe e o mova para objetos separados chamados builders (construtores). O padrão organiza a construção em uma série de etapas. Para criar um objeto, você executa uma série dessas etapas em um objeto construtor. A parte importante é que você não precisa chamar todas as etapas, apenas as necessárias para aquela configuração específica.
