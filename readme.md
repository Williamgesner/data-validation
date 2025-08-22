# 📊 Construindo funções básicas de inscrição para validar novos usuários  

**👤 LinkedIn:** [William Gesner](https://www.linkedin.com/in/william-gesner/)  

---
## 📝 Descrição  
Este projeto tem como foco a criação de **funções Python reutilizáveis para validação de dados de usuários em um processo de cadastro**.  
A implementação dessas funções reduz o número de tentativas inválidas ou incompletas, evitando falhas no aplicativo e garantindo uma melhor experiência para o usuário.  

Embora seja um desafio mais próximo das atribuições de um **desenvolvedor backend**, ele foi extremamente importante para minha curva de aprendizado. A validação e padronização de informações desde o ponto de entrada são etapas fundamentais para garantir a **qualidade, consistência e integridade dos dados** em qualquer sistema.  

## 🎯 Objetivo  
O objetivo principal foi **criar funções em Python para padronizar as verificações de entrada de usuários**, garantindo a consistência dos dados antes da criação de contas.  
As funções implementadas foram:  
- `validate_name()` → Verifica se o nome do usuário é uma string válida e contém mais de dois caracteres.  
- `validate_email()` → Verifica se o e-mail informado contém `@` e possui um domínio válido listado em `top_level_domains`.  

Ambas as funções retornam valores booleanos (`True` ou `False`), facilitando a tomada de decisão no fluxo de cadastro.

## 🔎 Análise  
Durante o desenvolvimento, alguns pontos importantes foram trabalhados:  
- **Validação de strings** para garantir que os dados inseridos atendam a critérios mínimos.  
- **Uso de funções reutilizáveis** para reduzir redundância no código e aumentar a confiabilidade.  
- **Aplicação de listas pré-carregadas (`top_level_domains`)** para validar domínios de e-mail.  
- Aprendizado sobre como **pequenos blocos de código bem estruturados** podem melhorar a robustez de um sistema.  

O desafio principal foi garantir que as funções fossem simples, mas flexíveis o suficiente para serem integradas em sistemas maiores no futuro.

## 🛠️ Ferramentas Utilizadas  
- **Python** 🐍  
- **Validações com strings e listas**  
- **VSCode** como ambiente de desenvolvimento  
- **Markdown** para documentação de projetos no GitHub.  

## 🧩 Tarefas realizadas  
- Criação da função `validate_name()` para validar nomes de usuários.  
- Criação da função `validate_email()` para validar endereços de e-mail.  
- Integração da lista `top_level_domains` no processo de validação.  
- Testes de retorno booleano para entradas válidas e inválidas.  
- Documentação do código e boas práticas para reuso em diferentes cenários.  

## ✅ Conclusão  
O projeto resultou em **funções de validação reutilizáveis que garantem maior segurança e confiabilidade no processo de cadastro de novos usuários**.  
Apesar de estar mais relacionado ao universo de **backend**, ele fortalece habilidades que também são cruciais para **Engenharia de Dados**, já que a integridade começa no ponto de entrada das informações.  

👉 Essa prática reforçou meus conhecimentos em lógica de programação e manipulação de strings, além de mostrar como diferentes áreas da tecnologia se complementam. Projetos como este criam uma base sólida para lidar com dados de forma mais robusta em pipelines e sistemas de maior complexidade.  

---
# data-validation
# data-validation
